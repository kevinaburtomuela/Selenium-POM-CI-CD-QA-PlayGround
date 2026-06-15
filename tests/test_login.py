import time

from selenium import webdriver
from pages.home_page import DashboardPage
from pages.login_page import LoginPage


class TestLogin:

    def test_tc001_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.write_user_password("admin","admin123")
        login_page.click_login()
        login_page.validate_URL()
        assert (
            driver.current_url == "https://qaplayground.com/bank/dashboard"
        )

    def test_tc002_login_with_invalid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.write_user_password("invalid_user", "admin123")
        login_page.click_login()
        assert (
                login_page.get_error_message() == "⚠️ Invalid username or password. Please try again."
        )

    def test_tc003_login_with_invalid_password(self, driver):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.write_user_password("admin", "invalid_password")
            login_page.click_login()
            assert (
                    login_page.get_error_message() == "⚠️ Invalid username or password. Please try again."
            )

    def test_tc004_create_a_saving_account(self, driver):
            login_page = LoginPage(driver)
            dashboard_page = DashboardPage(driver)
            login_page.login_admin_user("admin","admin123")
            dashboard_page.click_create_account()
            dashboard_page.enter_account_name("Saving account")
            dashboard_page.select_account_type()
            dashboard_page.enter_inicial_balance("500.00")
            dashboard_page.enable_overdraft()
            dashboard_page.create_account()
            assert dashboard_page.get_success_message() == "Account created successfully!"

    def test_tc005_create_a_checking_account(self, driver):
            login_page = LoginPage(driver)
            dashboard_page = DashboardPage(driver)
            login_page.login_admin_user("admin","admin123")
            dashboard_page.click_create_account()
            dashboard_page.enter_account_name("Checking account")
            dashboard_page.select_account_type()
            dashboard_page.enter_inicial_balance("4444.00")
            dashboard_page.enable_overdraft()
            dashboard_page.create_account()
            assert dashboard_page.get_success_message() == "Account created successfully!"

    def test_tc006_create_a_credit_card(self, driver):
            login_page = LoginPage(driver)
            dashboard_page = DashboardPage(driver)
            login_page.login_admin_user("admin","admin123")
            dashboard_page.click_create_account()
            dashboard_page.enter_account_name("Credit card")
            dashboard_page.select_account_type()
            dashboard_page.enter_inicial_balance("777.00")
            dashboard_page.enable_overdraft()
            dashboard_page.create_account()
            assert dashboard_page.get_success_message() == "Account created successfully!"