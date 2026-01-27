import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


# определение драйвера до теста
@pytest.fixture(scope='session')
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# определение страницы как источник 
@pytest.fixture
def record_page(browser):
    file_path =  Path('record.html').resolve().as_uri() 
    browser.get(file_path)
    assert 'мои записи' in browser.page_source
    return browser