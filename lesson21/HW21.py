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

@pytest.fixture()
def driver():
    """Pytest fixture to set up and tear down the WebDriver instance."""
    download_dir = "C:/Users/volch/Downloads"

    # Chrome options with download preferences
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=chrome_options)
    yield config_driver
    config_driver.quit()


def test_task4_2(driver):
    """Test to download a file and verify the download."""
    download_dir = "C:/Users/volch/Downloads"
    file_name = "file-sample_100kB.doc"

    # Set up explicit wait
    wait = WebDriverWait(driver, 10)

    # Open the website
    driver.get("https://file-examples.com/")

    # Close the cookie window
    close_cookie_window(driver)
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-27"))).click()
    assert "index.php/sample-documents-download/" in driver.current_url, "Failed to navigate to documents page"

    # Scroll to and click the first file link
    files = driver.find_elements(By.CSS_SELECTOR, ".text-right.file-link > a")
    actions = ActionChains(driver)
    actions.move_to_element(files[0]).perform()
    files[0].click()
    close_ads(driver)

    # Verify navigation to the file page
    assert "index.php/sample-documents-download/sample-doc-download/" in driver.current_url, "Failed to navigate to file page"

    # Click the download button
    file_sizes = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-orange.btn-outline.btn-xl.page-scroll.download-button")
    actions.move_to_element(file_sizes[0]).perform()
    file_sizes[0].click()

    # Check if the file is downloaded
    check_download(wait, download_dir, file_name)


def close_cookie_window(driver):
    """Close the cookie banner if present."""
    try:
        cookie_close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-button.fc-cta-consent.fc-primary-button"))
        )
        cookie_close_button.click()
    except Exception:
        print("No cookie banner to close.")


def check_download(wait, download_dir, file_name):
    """Wait for the file to appear in the download directory."""
    wait.until(lambda driver: os.path.exists(os.path.join(download_dir, file_name)), "File not downloaded")
    print("Download completed!")


def close_ads(driver):
    """Перебирает все рекламные iframes, ищет кнопку 'Close' и закрывает рекламу."""
    try:
        # Находим все iframes на странице
        all_iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"Found {len(all_iframes)} iframes on the page.")

        for iframe in all_iframes:
            try:
                iframe_id = iframe.get_attribute("id")
                if not iframe_id or not iframe_id.startswith("aswift"):
                    continue  # Пропускаем не относящиеся к рекламе iframes

                print(f"Trying to switch to iframe: {iframe_id}")
                driver.switch_to.frame(iframe)

                # Проверяем кнопку закрытия сразу в этом iframe
                try:
                    ad_close_button = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.ID, "dismiss-button"))
                    )
                    ad_close_button.click()
                    print("Ad banner closed in main iframe.")
                    driver.switch_to.default_content()
                    return  # Выходим из функции сразу

                except Exception:
                    print("No close button found in main iframe, checking nested iframe.")

                # Ищем вложенный iframe с рекламой
                try:
                    nested_iframe = driver.find_element(By.TAG_NAME, "iframe")
                    driver.switch_to.frame(nested_iframe)
                    print("Switched to nested ad_iframe.")

                    # Проверяем кнопку закрытия внутри вложенного iframe
                    ad_close_button = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.ID, "dismiss-button"))
                    )
                    ad_close_button.click()
                    print("Ad banner closed in nested iframe.")
                    driver.switch_to.default_content()
                    return  # Выходим из функции сразу

                except Exception:
                    print(f"No ad found in nested iframe of {iframe_id}, switching back.")

            except Exception as e:
                print(f"Error switching to iframe {iframe_id}: {e}")

            finally:
                driver.switch_to.default_content()  # Возвращаемся в основной контент

        print("No ads found in any iframe.")

    except Exception as e:
        print(f"General error while handling ads: {e}")

    finally:
        driver.switch_to.default_content()
        print("Returned to main content.")

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
