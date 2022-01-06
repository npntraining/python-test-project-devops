import time

import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_simple():
    driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost:8000/SampleApp.html')
    terms = driver.find_element(By.ID, 'terms').text
    print(terms)
    next_btn = driver.find_element(By.ID, 'btn')
    time.sleep(5)
    assert (next_btn.is_enabled() is False)
    driver.find_element(By.ID, 'agree').click()
    time.sleep(5)
    next_btn_afterclick = driver.find_element(By.ID, 'btn')
    assert (next_btn_afterclick.is_enabled() is True)
