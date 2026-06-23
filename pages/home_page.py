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
    NEW_TRANSACTION_BUTTON = (By.ID, "new-transaction-link")
    TRANSFER_TYPE_DROPDOWN = (By.ID, "transaction-type")
    SELECT_DEPOSIT_OPTION = (By.XPATH, "//div[@role='option' and contains(normalize-space(.), 'Deposit')]")
    SELECT_WITHDRAWAL_OPTION = (By.XPATH, "//div[@role='option' and contains(normalize-space(.), 'Withdrawal')]")
    SELECT_TRANSFER_OPTION = (By.XPATH, "//div[@role='option' and contains(normalize-space(.), 'Transfer')]")
    FROM_ACCOUNT_DROPDOWN = (By.ID, "from-account")
    SELECT_PRIMARY_ACCOUNT_OPTION = (By.XPATH, "//div[@role='option' and contains(., 'Primary Savings')]")
    AMOUNT_TRANSFER_INPUT = (By.ID, "transaction-amount")
    DESCRIPTION_INPUT = (By.ID, "transaction-description")
    SUBMIT_TRANSACTION_BUTTON = (By.ID, "submit-transaction-btn")
    CREATE_TRASNFER_MESSAGE = (By.XPATH, "//div[contains(text(),'Transaction completed successfully!')]")
    TO_ACCOUNT_DROPDOWN = (By.ID, "to-account")
    SELECT_CHECKING_ACCOUNT_OPTION = (By.XPATH, "//div[@role='option' and contains(., 'Checking Account')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_user(self):
        return self.driver.find_element(*self.USER_NAME).text

    def click_create_account(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_ACCOUNT_BUTTON)).click()

    def enter_account_name(self, account_name):
        self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_NAME_INPUT)).send_keys(account_name)

    def select_account_type(self):
        self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_TYPE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and contains(.,'Savings Account')]"))).click()

    def enter_inicial_balance(self, balance):
        self.wait.until(EC.element_to_be_clickable(self.INITIAL_BALANCE_INPUT)).send_keys(balance)

    def enable_overdraft(self):
        self.wait.until(EC.element_to_be_clickable(self.OVERDRAFT_CHECKBOX)).click()

    def create_account(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_BUTTON)).submit()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text

    def click_transaction_type_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_TRANSACTION_BUTTON)).click()

    def select_transfer_deposit_type(self):
        self.wait.until(EC.element_to_be_clickable(self.TRANSFER_TYPE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_DEPOSIT_OPTION)).click()

    def select_transfer_withdrawal_type(self):
        self.wait.until(EC.element_to_be_clickable(self.TRANSFER_TYPE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_WITHDRAWAL_OPTION)).click()

    def select_transfer_transfer_type(self):
        self.wait.until(EC.element_to_be_clickable(self.TRANSFER_TYPE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_TRANSFER_OPTION)).click()

    def click_from_account(self):
        self.wait.until(EC.element_to_be_clickable(self.FROM_ACCOUNT_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_PRIMARY_ACCOUNT_OPTION)).click()

    def enter_transfer_amount(self, amount):
        self.wait.until(EC.visibility_of_element_located(self.AMOUNT_TRANSFER_INPUT)).send_keys(amount)

    def enter_description(self, description):
        self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION_INPUT)).send_keys(description)

    def click_submit_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_TRANSACTION_BUTTON)).click()

    def get_create_transfer_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.CREATE_TRASNFER_MESSAGE)).text

    def click_to_account(self):
        self.wait.until(EC.element_to_be_clickable(self.TO_ACCOUNT_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CHECKING_ACCOUNT_OPTION)).click()
