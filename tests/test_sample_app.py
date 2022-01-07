import time

import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_1():
    driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost:8000/aut-devops/SampleApp.html')
    terms = driver.find_element(By.ID, 'terms').text
    next_btn = driver.find_element(By.ID, 'btn')
    assert (next_btn.is_enabled() is False)
    driver.close()

def test_2():
    driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost:8000/aut-devops/SampleApp.html')
    terms = driver.find_element(By.ID, 'terms').text
    next_btn = driver.find_element(By.ID, 'btn')
    driver.find_element(By.ID, 'agree').click()
    next_btn_afterclick = driver.find_element(By.ID, 'btn')
    assert (next_btn_afterclick.is_enabled() is True)


def test_3():
    driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost:8000/aut-devops/SampleApp.html')
    terms = driver.find_element(By.ID, 'terms').text
    next_btn = driver.find_element(By.ID, 'btn')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'agree').click()
    next_btn_afterclick = driver.find_element(By.ID, 'btn')
    assert (next_btn_afterclick.is_enabled() is False)