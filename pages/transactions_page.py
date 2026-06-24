
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Transactionpage:

    TRANSACTION_PAGE_BUTTON = (By.ID, "nav-transactions")
    ACCOUNT_DROPDOWN_FILTER = (By.ID, "filter-account")
    PRIMARY_SAVINGS_OPTION = (By.XPATH, "//div[@role='option' and contains(., 'Primary Savings')]")
    APPLY_FILTER_BUTTON = (By.ID, "apply-filters-btn")
    ACCOUNT_COLUMN_CELLS = (By.CSS_SELECTOR, '[data-testid="transaction-account"]')
    TYPE_DROPDOWN_FILTER = (By.ID, "filter-transaction-type")
    DEPOSIT_OPTION = (By.XPATH, '//div[@role="option" and normalize-space()="Deposit"]')
    TYPE_COLUMN_CELLS = (By.XPATH, '//span[normalize-space()="Deposit"]')
    FROM_DATE = (By.ID, 'date-from')
    TO_DATE = (By.ID, 'date-to')
    NOT_FOUND_MESSAGE = (By.ID, 'empty-transactions-message')

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_transaction_page(self):
        self.wait.until(EC.element_to_be_clickable(self.TRANSACTION_PAGE_BUTTON)).click()

    def click_account_filter(self):
        self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_DROPDOWN_FILTER)).click()

    def select_primary_saving_account(self):
        self.wait.until(EC.element_to_be_clickable(self.PRIMARY_SAVINGS_OPTION)).click()

    def click_apply_filter_btn(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.APPLY_FILTER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()

    def validate_all_accounts_are_primary_savings(self):
        account_cells = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.ACCOUNT_COLUMN_CELLS))

        for cell in account_cells:
            assert cell.text.strip() == "Primary Savings", (f"Se encontró '{cell.text}' en lugar de 'Primary Savings'")

    def click_type_filter(self):
        self.wait.until(EC.element_to_be_clickable(self.TYPE_DROPDOWN_FILTER)).click()

    def select_deposit_type(self):
        self.wait.until(EC.element_to_be_clickable(self.DEPOSIT_OPTION)).click()

    def validate_all_types_are_deposit(self):
        account_cells = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.TYPE_COLUMN_CELLS))
        for cell in account_cells:
            print(cell.text)
        for cell in account_cells:
            assert cell.text.strip() == "Deposit", (f"Se encontro '{cell.text}' en lugar de 'Deposit'")

    def select_date_from(self, day):
        print("Abriendo calendario")
        from datetime import datetime

        date_obj = datetime.strptime(day, "%d/%m/%Y")
        # Formato M/D/YYYY sin ceros: 6/25/2026
        formatted_day = f"{date_obj.month}/{date_obj.day}/{date_obj.year}"

        from_date = self.wait.until(
            EC.element_to_be_clickable(self.FROM_DATE)
        )
        from_date.click()

        day_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[@data-day='{formatted_day}']")
            )
        )
        day_button.click()

    def select_date_to(self,day):
        self.wait.until(EC.element_to_be_clickable(self.TO_DATE)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@data-day='{day}']"))).click()

    def get_not_found_records(self):
        msg = self.wait.until(EC.visibility_of_element_located(self.NOT_FOUND_MESSAGE))
        return msg.text.strip()





