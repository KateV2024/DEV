import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


# Medium level
def test_dropdown_options():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Шаг 1: Перейти на страницу
        driver.get("https://omayo.blogspot.com/")

        # Шаг 2: Работа с выпадающим списком
        dropdown = driver.find_element(By.ID, "drop1")
        dropdown1 = Select(dropdown)

        # Шаг 3: Выбрать опцию 3
        dropdown1.select_by_visible_text('doc 3')
        assert dropdown1.first_selected_option.text == "doc 3", "Option 'doc 3' was not selected!"

    finally:
        # Закрытие браузера
        driver.quit()
