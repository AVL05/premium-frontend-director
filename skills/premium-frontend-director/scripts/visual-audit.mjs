#!/usr/bin/env node
/** Local-only Playwright frontend evidence collector. No auto-install, no external URL navigation. */
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(path.join(process.cwd(), 'package.json'));
function option(key, fallback) {
  const index = process.argv.indexOf(key);
  if (index < 0) return fallback;
  if (!process.argv[index + 1] || process.argv[index + 1].startsWith('--')) {
    throw new Error(`Missing value for ${key}`);
  }
  return process.argv[index + 1];
}
let url, out;
try {
  url = new URL(option('--url', 'http://localhost:3000'));
  out = path.resolve(option('--out', './artifacts/visual-audit'));
} catch (error) {
  console.error(error.message);
  process.exit(2);
}
if (!['http:', 'https:'].includes(url.protocol) ||
    !['localhost', '127.0.0.1', '[::1]'].includes(url.hostname) ||
    url.username || url.password) {
  console.error('Only HTTP(S) loopback URLs without credentials are allowed.');
  process.exit(2);
}
let chromium;
try {
  chromium = require('playwright').chromium;
} catch {
  try { chromium = require('@playwright/test').chromium; }
  catch {
    console.error('Playwright is not installed in the target project. Install after approval: npm i -D @playwright/test && npx playwright install chromium');
    process.exit(2);
  }
}
const viewports = [{w:375,h:812},{w:768,h:1024},{w:1440,h:900},{w:1920,h:1080}];
const results = [];
let browser;
let failed = false;
try {
  await mkdir(out, {recursive:true});
  browser = await chromium.launch({headless:true});
  for (const {w,h} of viewports) {
    const page = await browser.newPage({viewport:{width:w,height:h}, reducedMotion:'reduce'});
    const errors = [];
    const failedRequests = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('console', message => {if (message.type()==='error') errors.push(message.text());});
    page.on('requestfailed', request => failedRequests.push({url:request.url(),error:request.failure()?.errorText ?? 'unknown'}));
    try {
      const response = await page.goto(url.toString(), {waitUntil:'networkidle',timeout:30000});
      const metrics = await page.evaluate(() => {
        const imgs = [...document.images];
        const allControls = [...document.querySelectorAll('input, textarea, select')];
        return {
          overflow: document.documentElement.scrollWidth > window.innerWidth + 1,
          brokenImages: imgs.filter(img => !img.complete || img.naturalWidth === 0).map(img => img.currentSrc || img.src),
          missingImageAlt: imgs.filter(img => !img.hasAttribute('alt')).length,
          unlabeledControls: allControls.filter(el => !el.labels?.length && !el.getAttribute('aria-label') && !el.getAttribute('aria-labelledby')).length,
          missingTitle: !document.title.trim(),
          missingMain: !document.querySelector('main'),
          headingCount: document.querySelectorAll('h1').length,
        };
      });
      const screenshot = `${w}x${h}.png`;
      await page.screenshot({path:path.join(out,screenshot),fullPage:true,animations:'disabled'});
      const item = {viewport:`${w}x${h}`,status:response?.status() ?? null,title:await page.title(),...metrics,errors,failedRequests,screenshot};
      item.passed = Boolean(response?.ok()) && !metrics.overflow && metrics.brokenImages.length===0 &&
        metrics.missingImageAlt===0 && metrics.unlabeledControls===0 && !metrics.missingTitle &&
        !metrics.missingMain && metrics.headingCount===1 && errors.length===0 && failedRequests.length===0;
      if (!item.passed) failed=true;
      results.push(item);
    } catch(error) {
      failed=true;
      results.push({viewport:`${w}x${h}`,passed:false,failure:String(error)});
    } finally {await page.close();}
  }
} catch(error) {
  failed=true;
  console.error(`Browser audit failed: ${error.message}`);
} finally {
  if (browser) await browser.close();
}
await mkdir(out,{recursive:true});
await writeFile(path.join(out,'report.json'), JSON.stringify({
  url:url.toString(), generatedAt:new Date().toISOString(),
  scope:'Browser smoke checks, layout, missing accessible names on form controls, image integrity and screenshots. Not a WCAG, visual similarity, interaction or performance certification.',
  results
},null,2)+'\n');
console.log(JSON.stringify({out,passed:!failed,results},null,2));
if (failed) process.exitCode=1;
