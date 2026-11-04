#!/usr/bin/env node
/** Screenshot and smoke-check helper. Requires Playwright in the target environment; never auto-installs. */
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(path.join(process.cwd(), 'package.json')); // Resolve Playwright from target app
function arg(k, fallback) { const i=process.argv.indexOf(k); return i>=0 ? process.argv[i+1] : fallback; }
const url=arg('--url', 'http://localhost:3000');
const out=path.resolve(arg('--out', './artifacts/visual-audit'));
if (!/^https?:\/\/(localhost|127\.0\.0\.1|\[::1\])(?::\d+)?(?:\/|$)/i.test(url)) {
 console.error('For safety, --url must point to localhost / 127.0.0.1.'); process.exit(2);
}
let chromium;
try { chromium=require('playwright').chromium; }
catch { try { chromium=require('@playwright/test').chromium; }
catch { console.error('Playwright unavailable. Install it in the target app after approval: npm i -D @playwright/test && npx playwright install chromium'); process.exit(2); } }
const sizes=[{w:375,h:812},{w:768,h:1024},{w:1440,h:900},{w:1920,h:1080}];
await mkdir(out,{recursive:true});
let browser; const results=[]; let failed=false;
try {
 browser=await chromium.launch({headless:true});
 for (const {w,h} of sizes) {
  const page=await browser.newPage({viewport:{width:w,height:h},reducedMotion:'reduce'});
  const errors=[];
  page.on('pageerror', e=>errors.push(e.message));
  page.on('console', m=>{if(m.type()==='error') errors.push(m.text());});
  try {
   const response=await page.goto(url,{waitUntil:'networkidle',timeout:30000});
   const title=await page.title();
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
   const name=`${w}x${h}.png`;
   await page.screenshot({path:path.join(out,name),fullPage:true,animations:'disabled'});
   const item={viewport:`${w}x${h}`,status:response?.status()??null,title,overflow,errors,screenshot:name};
   if (!response?.ok() || overflow || errors.length) failed=true;
   results.push(item);
  } catch(e) {failed=true;results.push({viewport:`${w}x${h}`,failure:String(e)});}
  finally {await page.close();}
 }
} catch(e) { console.error(`Browser launch failed: ${e.message}`);process.exitCode=2; }
finally {if(browser) await browser.close();}
await writeFile(path.join(out,'report.json'),JSON.stringify({url,generatedAt:new Date().toISOString(),scope:'smoke-check, overflow, console errors, screenshots; not full a11y/performance validation',results},null,2)+'\n');
console.log(JSON.stringify({out,results},null,2));
if(failed)process.exitCode=1;
