from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.goto("file:///app/kulup_paneli_yedekli_guncel.html")

        # Call the click event manually on the button, which triggers the actual app logic
        page.evaluate("document.getElementById('btnManageSalaries').click();")

        page.evaluate("document.getElementById('salaryModalOverlay').style.display = 'flex';")

        # Take a screenshot
        page.screenshot(path="/home/jules/verification/salary_modal_final2.png")
        print("Captured final salary modal screenshot")

        browser.close()

if __name__ == "__main__":
    verify()
