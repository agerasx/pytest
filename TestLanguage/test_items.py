import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exist(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(lambda d: d.find_element(By.CLASS_NAME, "btn-add-to-basket"))
    assert "Añadir al carrito" in button.text, "Language not ES"
