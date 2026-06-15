
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    USER_NAME = (By.ID, "username-display")
    ADD_ACCOUNT_BUTTON = (By.ID, "add-account-link")
    ACCOUNT_NAME_INPUT = (By.ID, "account-name")
    ACCOUNT_TYPE_DROPDOWN = (By.ID, "account-type")
    INITIAL_BALANCE_INPUT = (By.ID, "initial-balance")
    OVERDRAFT_CHECKBOX = (By.ID, "enable-overdraft")
    CREATE_ACCOUNT_BUTTON = (By.ID, "save-account-btn")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'Account created successfully!')]")

    def __init__(self, driver):
        self.driver = driver

    def get_user(self):
        return self.driver.find_element(*self.USER_NAME).text

    def click_create_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_ACCOUNT_BUTTON)).click()

    def enter_account_name(self,account_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ACCOUNT_NAME_INPUT)).send_keys(account_name)

    def select_account_type(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCOUNT_TYPE_DROPDOWN)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and contains(.,'Savings Account')]"))).click()
        # Validación para ver qué quedó seleccionado
        print("Tipo seleccionado:",self.driver.find_element(*self.ACCOUNT_TYPE_DROPDOWN).text)

    def enter_inicial_balance(self, balance):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.INITIAL_BALANCE_INPUT)).send_keys(balance)

    def enable_overdraft(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.OVERDRAFT_CHECKBOX)).click()

    def create_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_BUTTON)).submit()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
