import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_login_and_add_to_cart():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Шаг 1: Перейти на страницу логина
        driver.get("https://www.saucedemo.com")

        # Шаг 2: Ввести данные для авторизации
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # Шаг 3: Проверить, что пользователь на странице инвентаря
        assert "inventory" in driver.current_url, "Не удалось перейти на страницу инвентаря"

        # Шаг 4: Добавить товар в корзину
        product_name = "Sauce Labs Backpack"  # Название товара
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()

        # Шаг 5: Проверить, что товар добавлен (значок корзины)
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "Товар не добавлен в корзину"

        # Шаг 6: Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Шаг 7: Проверить, что в корзине отображается добавленный товар
        cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert cart_item_name == product_name, f"Ожидался товар '{product_name}', но найден '{cart_item_name}'"

        # Шаг 8: Проверить, что пользователь на странице инвентаря
        assert "cart" in driver.current_url, "Не удалось перейти на страницу cart"

        # Шаг 9: Добавить товар в корзину
        checkout = driver.find_element(By.ID, "checkout")
        checkout.click()

        # Шаг 3: Проверить, что пользователь на странице инвентаря
        assert "git checkout-step-one" in driver.current_url, "Не удалось перейти на страницу checkout"

        # Шаг 2: Ввести данные для авторизации
        firstName = driver.find_element(By.ID, "first-name")
        lastName  = driver.find_element(By.ID, "last-name")
        postalCode = driver.find_element(By.ID, "postal-code")
        continue_icon = driver.find_element(By.ID, "continue")

        firstName.send_keys("standard_user")
        lastName.send_keys("secret_sauce")
        postalCode.send_keys("223223")
        continue_icon.click()

    finally:
        # Закрытие браузера
        driver.quit()
