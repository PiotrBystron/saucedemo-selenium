# Selenium UI Tests with Pytest

Automated UI tests for the **SauceDemo** - https://www.saucedemo.com/ website using **Selenium**, **Pytest**, and the **Page Object Model** design pattern.

## Features

- Page Object Model structure
- Positive and negative login test cases
- Headless Chrome WebDriver fixture
- Easy setup with webdriver-manager

## How to run

### 1. Clone repository

```bash
git clone https://github.com/PiotrBystron/saucedemo-selenium.git
```

```bash
cd saucedemo-selenium
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the tests

```bash
pytest -v
```

A detailed report will be generated as report.html in the project folder.
The console output will also show detailed test names and their results (PASS/FAIL).
