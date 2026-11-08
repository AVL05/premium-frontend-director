#!/usr/bin/env node
/** Local-only negative fixtures. Browser checks detect deliberately broken cases; G11 remains manual. */
import path from 'node:path';
import { mkdir, writeFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(path.join(process.cwd(), 'package.json'));
let chromium;
try { chromium = require('playwright').chromium; }
catch {
  try { chromium = require('@playwright/test').chromium; }
  catch { console.error('Playwright is required in the test workspace (no auto-install).'); process.exit(2); }
}
const out = path.join(root, 'artifacts', 'failing-fixtures');
const base = path.join(root, 'examples', 'failing-fixtures');
const url = relative => pathToFileURL(path.join(base, relative)).href;
const checks = [];
const record = (id, passed, observed, expected) => checks.push({ id, passed: Boolean(passed), observed, expected });
let browser;
try {
  await mkdir(out, { recursive: true });
  browser = await chromium.launch({ headless: true });
  // G11 screenshots are only comparable evidence, NOT a subjective score.
  for (const width of [375, 1440]) {
    const dom = [];
    for (const [name, file] of [['before', 'visual-ambition/before.html'], ['after-cosmetic', 'visual-ambition/after-cosmetic.html']]) {
      const page = await browser.newPage({ viewport: { width, height: width === 375 ? 812 : 900 }, reducedMotion: 'reduce' });
      try {
        await page.goto(url(file));
        dom.push(await page.locator('main').evaluate(el => el.innerHTML));
        await page.screenshot({ path: path.join(out, 'g11-' + name + '-' + width + '.png'), fullPage: true, animations: 'disabled' });
      } finally { await page.close(); }
    }
    record('G11 controlled fixture structure at ' + width + 'px', dom.length === 2 && dom[0] === dom[1],
      'Same main DOM; screenshot pair captured', 'Same structural content. No automatic aesthetic verdict.');
  }
  // Keyboard failure: mouse activates both, only the native button supports Tab+Enter.
  for (const [name, file, shouldWork] of [['broken','keyboard-accessibility/broken.html',false],['fixed','keyboard-accessibility/fixed.html',true]]) {
    const page = await browser.newPage({ viewport: { width: 750, height: 850 } });
    try {
      await page.goto(url(file));
      await page.locator('#start-link').focus();
      await page.keyboard.press('Tab');
      const focused = await page.evaluate(() => document.activeElement?.id || '');
      await page.keyboard.press('Enter');
      const keyboard = (await page.locator('#status').textContent()) === 'Activated';
      await page.locator('#action').click();
      const mouse = (await page.locator('#status').textContent()) === 'Activated';
      const observed = { focused, keyboard, mouse };
      record('G4/G6 ' + name + ' Tab+Enter', focused === (shouldWork?'action':'end-link') && keyboard === shouldWork && mouse,
        observed, shouldWork ? 'Keyboard and mouse work' : 'Keyboard skips action; mouse still works');
    } finally { await page.close(); }
  }
  // Responsive defect: 375px overflow in broken case only, desktop never overflows.
  for (const [name, file, shouldFailMobile] of [['broken','responsive-overflow/broken.html',true],['fixed','responsive-overflow/fixed.html',false]]) {
    for (const width of [375, 1440]) {
      const page = await browser.newPage({ viewport: { width, height: width === 375 ? 812 : 900 }, reducedMotion: 'reduce' });
      try {
        await page.goto(url(file));
        const observed = await page.evaluate(() => ({
          scrollWidth: document.documentElement.scrollWidth,
          viewportWidth: window.innerWidth,
          overflow: document.documentElement.scrollWidth > window.innerWidth + 1
        }));
        const expected = { overflow: shouldFailMobile && width === 375 };
        record('G5 ' + name + ' at ' + width + 'px', observed.overflow === expected.overflow, observed, expected);
        await page.screenshot({ path: path.join(out, 'g5-' + name + '-' + width + '.png'), fullPage: true, animations: 'disabled' });
      } finally { await page.close(); }
    }
  }
} catch (error) {
  record('runtime', false, String(error), 'No browser errors');
} finally { if (browser) await browser.close(); }
const report = {
  scope: 'Offline negative regression cases; not aesthetic, WCAG, or general responsive certification.',
  g11: { automatedGateStatus: 'NOT RUN', expectedReviewedStatus: 'FAIL', reason: 'Cosmetic-only change does not meet the Immersive brief; reviewer must inspect images and missing signature interaction.' },
  checks,
  passed: checks.length === 8 && checks.every(x => x.passed)
};
await mkdir(out, { recursive: true });
await writeFile(path.join(out, 'report.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
if (!report.passed) process.exitCode = 1;
