from importlib.metadata import files
from operator import contains

import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()


def test_task1(driver):
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID, "tabButton").click()
    opened_handles = driver.window_handles
    driver.switch_to.window(opened_handles[1])
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page", \
        "Текст не соответствует"
    driver.close()
    driver.switch_to.window(opened_handles[0])
    assert driver.current_window_handle == opened_handles[0]


def test_task2(driver):
    driver.get("https://demoqa.com/frames")
    driver.switch_to.frame("frame1")
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page"
    driver.switch_to.default_content()
    driver.switch_to.frame("frame2")
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page"


def test_task3(driver):
    driver.get("https://demoqa.com/alerts")
    alert_button1 = driver.find_element(By.ID, "alertButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button1)
    alert_button1.click()
    alert1 = driver.switch_to.alert
    assert alert1.text == "You clicked a button"
    alert1.accept()
    alert_button2 = driver.find_element(By.ID, "confirmButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button2)
    alert_button2.click()
    alert2 = driver.switch_to.alert
    assert alert2.text == "Do you confirm action?"
    alert2.dismiss()
    alert_button3 = driver.find_element(By.ID, "promtButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button3)
    alert_button3.click()
    alert3 = driver.switch_to.alert
    assert alert3.text == "Please enter your name"
    alert3.send_keys("Selenium Test")
    alert3.accept()
    result = driver.find_element(By.ID, "promptResult")
    assert "Selenium Test" in result.text


def test_task4(driver):
    driver.get("https://www.google.com")
    available_services = driver.find_element(By.ID, "SIvCob")
    assert "Google offered in: polski" in available_services.text
    driver.quit()

# Настройте папку загрузок, загрузите файл PDF с сайта https://file-examples.com,
# и убедитесь, что файл сохранён в указанную папку.

def close_cookie_window(driver):
    """Attempts to close cookie consent popups or overlays."""
    try:
        wait = WebDriverWait(driver, 5)
        overlay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fc-dialog-overlay")))
        driver.execute_script("arguments[0].remove();", overlay)  # Remove the overlay
        print("Cookie overlay removed.")
    except:
        print("No cookie overlay found. Continuing.")

def close_ads(driver):
    """Close any ads that appear on the page."""
    try:
        WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "aswift_3"))
        )
        WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe"))
        )
        print("Switched to ad iframe.")

        ad_close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "dismiss-button"))
        )
        ad_close_button.click()
        print("Ad banner closed.")
    except Exception as e:
        print("Ad not found or not clickable:", e)
    finally:
        driver.switch_to.default_content()
        print("Returned to main content.")

def check_download(download_dir, file_name, timeout=15):
    """Check if the file has been downloaded to the specified directory."""
    file_path = os.path.join(download_dir, file_name)
    start_time = time.time()

    while not os.path.exists(file_path):
        if time.time() - start_time > timeout:
            raise TimeoutError(f"File {file_name} not downloaded in {timeout} seconds.")
        time.sleep(1)
    print(f"File {file_name} downloaded successfully.")

def test_task4_2():
    download_dir = "C:/Users/volch/Downloads"
    file_name = "file-sample_100kB.doc"

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://file-examples.com/")
        close_cookie_window(driver)

        # Navigate to the documents page
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-27"))).click()
        assert "index.php/sample-documents-download/" in driver.current_url, "Не удалось перейти на страницу с документами"

        close_ads(driver)

        # Click the first available document link
        files = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".text-right.file-link > a")))
        actions = ActionChains(driver)
        actions.move_to_element(files[0]).click().perform()

        assert "index.php/sample-documents-download/sample-doc-download/" in driver.current_url, "Не удалось перейти на страницу документа"

        close_ads(driver)

        # Click the first download button
        file_sizes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn.btn-orange.btn-outline.btn-xl.page-scroll.download-button")))
        actions.move_to_element(file_sizes[0]).click().perform()

        # Verify the file download
        check_download(download_dir, file_name)

    finally:
        driver.quit()

# Run the test
test_task4_2()


def test_work_with_actions(driver):
    try:
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
        source_element = driver.find_element(By.ID, "draggable")
        target_element = driver.find_element(By.ID, "droppable")
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()
        assert "Dropped" in target_element.text, "Drag and drop action failed"

    finally:
        driver.quit()
