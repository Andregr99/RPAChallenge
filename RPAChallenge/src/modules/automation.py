from playwright.sync_api import Page
from src.config.settings import SUBMIT_TIMEOUT

class RPAAutomation:
    FIELDS_MAPPING = {
        "First Name": "First Name",
        "Last Name": "Last Name",
        "Company Name": "Company Name",
        "Role in Company": "Role in Company",
        "Address": "Address",
        "Email": "Email",
        "Phone Number": "Phone Number",
    }
    
    def __init__(self, page: Page):
        self.page = page
    
    def start_challenge(self):
        self._click_button("Start")
    
    def fill_form(self, row):
        for field, column in self.FIELDS_MAPPING.items():
            self._fill_field(field, str(row[column]))
        self._submit_form()
    
    def _fill_field(self, label: str, value: str):
        locator = f"xpath=//label[contains(text(),'{label}')]/following-sibling::input"
        self.page.locator(locator).fill(value)
    
    def _click_button(self, text: str):
        locator = f"xpath=//button[contains(text(),'{text}')]"
        self.page.locator(locator).click()
    
    def _submit_form(self):
        self.page.locator("xpath=//input[@type='submit']").click(timeout=SUBMIT_TIMEOUT)