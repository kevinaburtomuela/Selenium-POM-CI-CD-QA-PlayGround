# QA Playground - Selenium Automation Framework

## Overview

This project is an automated testing framework built using Python, Selenium WebDriver, and Pytest.

The framework validates the functionality of the QA Playground Banking Application and follows the Page Object Model (POM) design pattern to improve maintainability, scalability, and readability.

## Technologies Used

* Python 3.9+
* Selenium WebDriver
* Pytest
* Allure Reports
* Page Object Model (POM)

## Project Structure

```text
QA-PlayGround/
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── account_page.py
│   └── transactions_page.py
│
├── tests/
│   └── test_login.py
│
├── reports/
│   └── allure-results/
│
├── conftest.py
├── pytest.ini
├── .gitignore
├── requirements.txt
└── README.md
```

## Test Coverage

### Authentication

* Login with valid credentials
* Login with invalid username
* Login with invalid password

### Accounts

* Create a savings account
* Create a checking account
* Create a credit card account
* Edit an existing account
* Delete an existing account
* Verify read-only user cannot edit accounts
* Verify read-only user cannot delete accounts

### Transactions

* Create a deposit transaction
* Create a withdrawal transaction
* Transfer funds between accounts
* Filter transactions by account
* Filter transactions by transaction type
* Filter transactions by date

## Installation

Clone the repository:

```bash
git clone https://github.com/kevinaburtomuela/Selenium-POM-CI-CD-QA-PlayGround.git
cd QA-PlayGround
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_login.py::TestLogin::test_tc001_login_success
```

Run tests with detailed output:

```bash
pytest -v
```

## Allure Reporting

Generate Allure results:

```bash
pytest --alluredir=reports/allure-results
```

Open the report:

```bash
allure serve reports/allure-results
```

## Framework Features

* Page Object Model (POM)
* Explicit Waits
* Pytest Fixtures
* Parameterized User Roles
* Allure Reporting
* Reusable Page Classes
* Readable and Maintainable Test Structure

## Author

Kevin Aburto

QA Automation Engineer Portfolio Project
