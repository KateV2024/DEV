import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_adding_new_record():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Шаг 1: Перейти на страницу и нажать "Добавить запись в таблицу"
        driver.get("https://demoqa.com/webtables")
        addNewRecord = driver.find_element(By.ID, "addNewRecordButton")
        addNewRecord.click()

        # Шаг 2: Добавить строчку в таблицу
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "age").send_keys("30")
        driver.find_element(By.ID, "salary").send_keys("50000")
        driver.find_element(By.ID, "department").send_keys("IT")
        driver.find_element(By.ID, "submit").click()

        # Шаг 3: Ожидать добавления новой строки в таблицу
        time.sleep(5)

        # Шаг 4: Проверить, что строчка добавилась
        rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
        added_row = None
        for row in rows:
            if "John" in row.text and "Doe" in row.text:
                added_row = row
                break

        assert added_row is not None, "John is not added"

    finally:
        # Закрытие браузера
        driver.quit()
