import os
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

USERS = {
    "admin": ("admin", "admin123"),
    "viewer": ("viewer", "viewer123")
}

@pytest.fixture
def driver():
    options = Options()

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    if not os.getenv("CI"):
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