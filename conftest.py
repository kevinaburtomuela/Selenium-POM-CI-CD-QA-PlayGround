import pytest
from selenium import webdriver
from pages.login_page import LoginPage

USERS = {
    "admin": ("admin", "admin123"),
    "viewer": ("viewer", "viewer123")
}

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_as(driver, request):
    role = request.param
    username, password = USERS[role]

    login_page = LoginPage(driver)
    login_page.login_admin_user(username, password)

    return driver