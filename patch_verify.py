from playwright.sync_api import Page, expect, sync_playwright

def test_salary_modal_open(page: Page):
    # Load the modified file directly
    page.goto("file:///app/kulup_paneli_yedekli_guncel.html")

    # Click the manage salaries button
    btn = page.locator("#btnManageSalaries")
    btn.click()

    page.fill("#salCoefficient", "1.39")
    page.fill("#salIndicator", "140")
    page.wait_for_timeout(500)

    val = page.locator("#salCivilServant").input_value()
    print(f"Calculated Civil Servant Value: {val}")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_salary_modal_open(page)
        finally:
            browser.close()
