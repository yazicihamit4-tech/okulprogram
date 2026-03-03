from playwright.sync_api import Page, expect, sync_playwright
import os

def test_salary_modal_open(page: Page):
    # Load the modified file directly
    page.goto("file:///app/kulup_paneli_yedekli_guncel.html")

    # Click the manage salaries button
    btn = page.locator("#btnManageSalaries")
    btn.click()

    # Change Inputs to User Scenario
    # 1 Hour, 1 Group, 1 Work Day, 64 TL Rate
    page.fill("#salDailyHours", "1")
    page.fill("#salWorkDays", "1")
    page.fill("#salGroupCount", "1")
    page.fill("#salHourlyRate", "64")

    # Click calculate
    calc_btn = page.locator("#btnCalcSalaries")
    calc_btn.click()
    page.wait_for_timeout(500)

    # Scroll the container to see the inputs and table properly
    page.evaluate("document.querySelector('#salaryModalOverlay .modal-box').scrollTo(0, 0)")
    page.screenshot(path="/home/jules/verification/salary_modal_auto_pool.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        try:
            test_salary_modal_open(page)
            print("Successfully verified the calculations!")
        finally:
            browser.close()
