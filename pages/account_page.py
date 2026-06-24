from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:

    ACCOUNT_PAGE_BUTTON = (By.ID, "nav-accounts")
    ACCOUNT_NAME_INPUT = (By.ID, "account-name")
    ACCOUNT_TYPE_DROPDOWN = (By.ID, "account-type")
    INITIAL_BALANCE_INPUT = (By.ID, "initial-balance")
    OVERDRAFT_CHECKBOX = (By.ID, "enable-overdraft")
    SAVE_ACCOUNT_BUTTON = (By.ID, "save-account-btn")
    UPDATE_MESSAGE = (By.XPATH, "//*[contains(text(),'Account updated successfully!')]")
    CONFIRM_DELETE_BUTTON = (By.ID, "confirm-delete-btn")
    DELETE_MESSAGE = (By.XPATH, "//div[contains(text(),'Account deleted successfully')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def clic_account_page(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ACCOUNT_PAGE_BUTTON)
        ).click()

    def click_edit_by_account_name(self, account_name):
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//button[contains(@aria-label,'{account_name}')]"
                )
            )
        ).click()

    def change_account_name(self, account_name):
        self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_NAME_INPUT)
        ).send_keys(account_name)

    def change_account_amount(self, balance):
        self.wait.until(
            EC.visibility_of_element_located(self.INITIAL_BALANCE_INPUT)
        ).send_keys(balance)

    def click_save_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SAVE_ACCOUNT_BUTTON)
        ).click()

    def get_update_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.UPDATE_MESSAGE)
        ).text

    def click_delete_button(self, account_name):
        row = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//tr[td[contains(.,'{account_name}')]]"
                )
            )
        )

        row.find_element(
            By.XPATH,
            ".//button[@data-action='delete']"
        ).click()

    def click_confirm_delete_btn(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON)
        ).click()

    def get_deleted_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DELETE_MESSAGE)
        ).text

    def is_edit_button_present(self, account_name):
        try:
            button = self.driver.find_element(
                By.XPATH,
                f"//button[contains(@aria-label,'{account_name}') and contains(@data-action,'edit')]"
            )
            return button.is_enabled()
        except:
            return False

    def is_delete_button_present(self, account_name):
        try:
            button = self.driver.find_element(
                By.XPATH,
                f"//button[contains(@aria-label,'{account_name}') and contains(@data-action,'delete')]"
            )
            return button.is_enabled()
        except:
            return False