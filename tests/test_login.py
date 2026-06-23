import time
from pages.transactions_page import Transactionpage

from selenium import webdriver
from pages.home_page import DashboardPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
import pytest
import allure


class TestLogin:

    @allure.feature("Authentication")
    @allure.title("TC001 - Login with valid admin credentials")
    @allure.description("Verify that an administrator can access the dashboard using valid credentials.")
    def test_tc001_login_success(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Navigate to login page"):
            login_page.open()
        with allure.step("Enter admin credentials"):
            login_page.write_user_password("admin", "admin123")
        with allure.step("Submit login form"):
            login_page.click_login()
        with allure.step("Validate dashboard page is displayed"):
            login_page.validate_URL()
        assert driver.current_url == "https://qaplayground.com/bank/dashboard"

    @allure.feature("Authentication")
    @allure.title("TC002 - Login with an invalid user")
    @allure.description("Verify that a user cannot log in with an invalid username.")
    def test_tc002_login_with_invalid_user(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Navigate to login page"):
            login_page.open()
        with allure.step("Enter an invalid user"):
            login_page.write_user_password("invalid_user", "admin123")
        with allure.step("Submit login form"):
            login_page.click_login()
        with allure.step("Validate a login failed message"):
            assert (login_page.get_error_message() == "⚠️ Invalid username or password. Please try again.")

    @allure.feature("Authentication")
    @allure.title("TC003 - Login with an invalid password")
    @allure.description("Verify that a user cannot log in with an invalid password")
    def test_tc003_login_with_invalid_password(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Navigate to login page"):
            login_page.open()
        with allure.step("Enter an invalid password"):
            login_page.write_user_password("admin", "invalid_password")
        with allure.step("Submit login form"):
            login_page.click_login()
        with allure.step("Validate a login failed message"):
            assert (login_page.get_error_message() == "⚠️ Invalid username or password. Please try again.")

    @allure.feature("Accounts")
    @allure.title("TC004 - Create a saving account")
    @allure.description("Create a Saving account on the Account section")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc004_create_saving_account(self, login_as):
        with allure.step("Navigate to Dashboard page"):
            dashboard = DashboardPage(login_as)
        with allure.step("Select create account button"):
            dashboard.click_create_account()
        with allure.step("Insert an account name"):
            dashboard.enter_account_name("Saving account")
        with allure.step("Select the account type"):
            dashboard.select_account_type()
        with allure.step("Insert the account amount"):
            dashboard.enter_inicial_balance("500.00")
        dashboard.enable_overdraft()
        dashboard.create_account()
        with allure.step("Validate a successfull message"):
            assert dashboard.get_success_message() == "Account created successfully!"

    @allure.feature("Accounts")
    @allure.title("TC005 - Create a Checking account")
    @allure.description("Create a Checking account on the Account section")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc005_create_checking_account(self, login_as):
        with allure.step("Navigate to Dashboard page"):
            dashboard = DashboardPage(login_as)
        with allure.step("Select create account button"):
            dashboard.click_create_account()
        with allure.step("Insert an account name"):
            dashboard.enter_account_name("Checking account")
        with allure.step("Select the account type"):
            dashboard.select_account_type()
        with allure.step("Insert the account amount"):
            dashboard.enter_inicial_balance("4444.00")
        dashboard.enable_overdraft()
        dashboard.create_account()
        with allure.step("Validate a successfull message"):
            assert dashboard.get_success_message() == "Account created successfully!"

    @allure.feature("Accounts")
    @allure.title("TC006 - Create a Credit account")
    @allure.description("Create a Credit account on the Account section")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc006_create_credit_card(self, login_as):
        with allure.step("Navigate to Dashboard page"):
            dashboard = DashboardPage(login_as)
        with allure.step("Select create account button"):
            dashboard.click_create_account()
        with allure.step("Insert an account name"):
            dashboard.enter_account_name("Credit card")
        with allure.step("Select the account type"):
            dashboard.select_account_type()
        with allure.step("Insert the account amount"):
            dashboard.enter_inicial_balance("777.00")
        dashboard.enable_overdraft()
        dashboard.create_account()
        with allure.step("Validate a successfull message"):
            assert dashboard.get_success_message() == "Account created successfully!"

    @allure.feature("Accounts")
    @allure.title("TC007 - Edit a Primary Savings account")
    @allure.description("Validate the user is capable to edit a Primary Savings account")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc007_edit_account(self, login_as):
        with allure.step("Log in as an admin user"):
            account = AccountPage(login_as)
        with allure.step("Navigate to Account page"):
            account.clic_account_page()
        with allure.step("Select the account to edit"):
            account.click_edit_by_account_name("Primary Savings")
        with allure.step("Edit the account name"):
            account.change_account_name("Credit card")
        with allure.step("Edit the account amount"):
            account.change_account_amount("444.00")
        account.click_save_button()
        with allure.step("Validate successful account update message"):
            assert account.get_update_message() == "Account updated successfully!"

    @allure.feature("Accounts")
    @allure.title("TC008 - Delete a Primary Savings account")
    @allure.description("Validate the user is capable to delete a Primary Savings account")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc008_delete_account(self, login_as):
        with allure.step("Log in as an admin user"):
            account = AccountPage(login_as)
        with allure.step("Navigate to Account page"):
            account.clic_account_page()
        with allure.step("Select the account to delete"):
            account.click_delete_button("Primary Savings")
        with allure.step("Confirm the delete action"):
            account.click_confirm_delete_btn()
        with allure.step("Validate successful account delete message"):
            assert account.get_deleted_message() == "Account deleted successfully."

    @allure.feature("Transfer")
    @allure.title("TC009 - Create a deposit transfer")
    @allure.description("Validate the user is capable to create a deposit transfer")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc009_create_deposit_transfer(self, login_as):
        with allure.step("Log in as an admin user"):
            dashboard = DashboardPage(login_as)
        with allure.step("Select the New transaction button"):
            dashboard.click_transaction_type_btn()
        with allure.step("Select the transaction type"):
            dashboard.select_transfer_deposit_type()
        with allure.step("Select the account"):
            dashboard.click_from_account()
        with allure.step("Insert the transfer amount"):
            dashboard.enter_transfer_amount("777.00")
        with allure.step("Insert the transfer description"):
            dashboard.enter_description("We create the description of the transfer")
        with allure.step("Select the creation transfer button"):
            dashboard.click_submit_btn()
        with allure.step("Validate successful transfer creation message"):
            assert dashboard.get_create_transfer_message() == "Transaction completed successfully!"

    @allure.feature("Transfer")
    @allure.title("TC010 - Create a withdrawal transfer")
    @allure.description("Validate the user is capable to create a withdrawal transfer")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc010_create_withdrawal_transfer(self, login_as):
        with allure.step("Log in as an admin user"):
            dashboard = DashboardPage(login_as)
        with allure.step("Select the New transaction button"):
            dashboard.click_transaction_type_btn()
        with allure.step("Select the transaction type"):
            dashboard.select_transfer_withdrawal_type()
        with allure.step("Select the account"):
            dashboard.click_from_account()
        with allure.step("Insert the transfer amount"):
            dashboard.enter_transfer_amount("888.00")
        with allure.step("Insert the transfer description"):
            dashboard.enter_description("We create the description of the transfer")
        with allure.step("Select the creation transfer button"):
            dashboard.click_submit_btn()
        with allure.step("Validate successful transfer creation message"):
            assert dashboard.get_create_transfer_message() == "Transaction completed successfully!"

    @allure.feature("Transfer")
    @allure.title("TC011 - Create a transfer transaction")
    @allure.description("Validate the user is capable to create a transfer transaction")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc011_create_transfer_transfer(self, login_as):
        with allure.step("Log in as an admin user"):
            dashboard = DashboardPage(login_as)
        with allure.step("Select the New transaction button"):
            dashboard.click_transaction_type_btn()
        with allure.step("Select the transaction type"):
            dashboard.select_transfer_transfer_type()
        with allure.step("Select the from account"):
            dashboard.click_from_account()
        with allure.step("Select the to account"):
            dashboard.click_to_account()
        with allure.step("Insert the transfer amount"):
            dashboard.enter_transfer_amount("999.00")
        with allure.step("Insert the transfer description"):
            dashboard.enter_description("We create the description of the transfer")
        with allure.step("Select the creation transfer button"):
            dashboard.click_submit_btn()
        with allure.step("Validate successful transfer creation message"):
            assert dashboard.get_create_transfer_message() == "Transaction completed successfully!"

    @allure.feature("Accounts")
    @allure.title("TC012 - Edit a transfer transaction with a viewer user")
    @allure.description("Validate a viewer user is not capable to edit a transfer transaction")
    @pytest.mark.parametrize("login_as", ["viewer"], indirect=True)
    def test_tc012_read_only_user_cannot_edit_account(self, login_as):
        with allure.step("Log in as an admin user"):
            account = AccountPage(login_as)
        with allure.step("Navigate to account page"):
            account.clic_account_page()
        with allure.step("Validate the edit button is not available"):
            assert account.is_edit_button_present("Primary Savings") is False

    @allure.feature("Accounts")
    @allure.title("TC013 - Delete a transfer transaction with a viewer user")
    @allure.description("Validate a viewer user is not capable to delete a transfer transaction")
    @pytest.mark.parametrize("login_as", ["viewer"], indirect=True)
    def test_tc013_read_only_user_cannot_delete_account(self, login_as):
        with allure.step("Log in as an admin user"):
            account = AccountPage(login_as)
        with allure.step("Navigate to account page"):
            account.clic_account_page()
        with allure.step("Validate the edit button is not available"):
            assert account.is_delete_button_present("Primary Savings") is False

    @allure.feature("Filters")
    @allure.title("TC014 - Validate account filter")
    @allure.description("Verify that transactions can be filtered correctly by account")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc014_filter_by_account(self, login_as):
        with allure.step("Log in as an admin user"):
            tx = Transactionpage(login_as)
        with allure.step("Navigate to transaction page"):
            tx.click_transaction_page()
        with allure.step("Select the filter"):
            tx.click_account_filter()
        with allure.step("Select the filter option"):
            tx.select_primary_saving_account()
        with allure.step("Apply the filter selection"):
            tx.click_apply_filter_btn()
        with allure.step("Validate the correct functionality of the account filter"):
            tx.validate_all_accounts_are_primary_savings()

    @allure.feature("Filters")
    @allure.title("TC015 - Validate type filter")
    @allure.description("Verify that transactions can be filtered correctly by type")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc015_filter_by_type(self, login_as):
        with allure.step("Log in as an admin user"):
            tx = Transactionpage(login_as)
        with allure.step("Navigate to transaction page"):
            tx.click_transaction_page()
        with allure.step("Select the filter"):
            tx.click_type_filter()
        with allure.step("Select the filter option"):
            tx.select_deposit_type()
        with allure.step("Apply the filter selection"):
            tx.click_apply_filter_btn()
        with allure.step("Validate the correct functionality of the type filter"):
            tx.validate_all_types_are_deposit()

    @allure.feature("Filters")
    @allure.title("TC016 - Validate date filter")
    @allure.description("Verify that transactions can be filtered correctly by date")
    @pytest.mark.parametrize("login_as", ["admin"], indirect=True)
    def test_tc016_validate_date_filter(self, login_as):
        with allure.step("Log in as an admin user"):
            tx = Transactionpage(login_as)
        with allure.step("Navigate to transaction page"):
            tx.click_transaction_page()
        with allure.step("Select the calendar date filter"):
            tx.select_date_from("25/6/2026")
        with allure.step("Apply the filter selection"):
            tx.click_apply_filter_btn()
        with allure.step("Validate the correct functionality of the date filter"):
            assert tx.get_not_found_records() == "No transactions found"
