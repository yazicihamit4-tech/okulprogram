from playwright.sync_api import Page, expect, sync_playwright

def test_salary_modal_open(page: Page):
    # Load the modified file directly
    page.goto("file:///app/kulup_paneli_yedekli_guncel.html")

    # Click the manage salaries button
    btn = page.locator("#btnManageSalaries")
    btn.click()

    # Change Inputs to User Scenario
    # 64 TL Rate, 2 Hours, 15 Work Days, 85 Students, 1 Group
    page.fill("#salDailyHours", "2")
    page.fill("#salWorkDays", "15")
    page.fill("#salHourlyRate", "64")
    page.fill("#salStudentCount", "85")
    page.fill("#salGroupCount", "1")

    # Wait to ensure inputs register
    page.wait_for_timeout(500)

    # Click calculate
    calc_btn = page.locator("#btnCalcSalaries")
    calc_btn.click()
    page.wait_for_timeout(500)

    page.screenshot(path="/home/jules/verification/salary_modal_new_formula.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        try:
            test_salary_modal_open(page)
        finally:
            browser.close()
