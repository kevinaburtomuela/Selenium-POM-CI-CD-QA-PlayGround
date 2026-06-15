from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://qaplayground.com/bank"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.ID, "alert-message")

    def open(self):
        self.driver.get(self.URL)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text

    def write_user_password(self, username, password):
        self.enter_username(username)
        self.enter_password(password)

    def login(self):
        self.click_login()

    def validate_URL(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url == "https://qaplayground.com/bank/dashboard"
        )

    def login_admin_user(self, username, password):
        self.driver.get(self.URL)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()