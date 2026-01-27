import os
import pytest
import time 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# добавление сценария
scenarios('../features/record.feature')

@given('I am on the records page')
def open_record_page(record_page):
    assert 'мои записи' in record_page.page_source.lower()
    
@when(parsers.parse('I add a record: "{text}"'))
def add_record(record_page, text):
    # """добавить запись"""
    input = record_page.find_element(By.NAME, 'new-todo')
    input.clear()
    input.send_keys(text + Keys.ENTER)
    # input.send_keys(Keys.ENTER)
    # time.sleep(1)
    # явное ожидание появления элемента
    WebDriverWait(record_page, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.todo-list li'))
    )

@when(parsers.parse('I mark the record: "{text}" as completed'))
def done_record(record_page, text):
    # """отмеченно завершенной"""
    records = record_page.find_elements(By.CSS_SELECTOR, '.todo-list li label')
    items = record_page.find_elements(By.CSS_SELECTOR, '.todo-list li')
    for item in items:
        label = item.find_element(By.TAG_NAME, 'label')
        if text in label.text:
            checkbox = item.find_element(By.TAG_NAME, 'input')
            checkbox.click()
            break

@then(parsers.parse('the list contains: "{text}"'))
def check_in_records(record_page, text):
    # """наличие записи в списке"""
    records = record_page.find_elements(By.CSS_SELECTOR, '.todo-list li label')
    assert any(text in record.text for record in records), f"пункт '{text}' не существует"

@then('the record is marked as completed')
def completed(record_page):
    # """проверка на отмеченное выполненным пунктом"""
    complete = record_page.find_elements(By.CSS_SELECTOR, '.todo-list li.completed')
    assert len(complete)>0, "нет выполненных пунктов"