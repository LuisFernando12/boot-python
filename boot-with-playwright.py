import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://theonegenerator.com/pt/geradores/documentos/gerador-de-email/")
        await page.click('#app-content > section > div.container > div > div.col > div.generator-container > div > div > div > div.generator > form > button')
        email = await page.get_attribute('#copyToClipboard-email')
        print(email)
        
asyncio.run(main())