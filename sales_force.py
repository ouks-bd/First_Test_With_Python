import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest_html


class TestTeslaFunctionality:
    @pytest.fixture()
    def test_setup(self):
        global driver
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://sf.bdbizhub.com/")
        driver.maximize_window()

        yield
        driver.close()
        driver.quit()

        print("Test Completed Sucessfully")

    @pytest.mark.smoke
    def test_login_with_correct_credential(self, test_setup):

        driver.find_element(By.ID, "UserName").send_keys("test")
        driver.find_element(By.ID, "Password").send_keys("test")
        driver.find_element(By.CLASS_NAME, "col-xs-4").click()
        time.sleep(5)
        print(driver.title)
    @pytest.mark.sanity
    def test_login_with_correct_user_incorrect_pass(self, test_setup):
        driver.find_element(By.ID, "UserName").send_keys("test")
        driver.find_element(By.ID, "Password").send_keys("test")
        driver.find_element(By.CLASS_NAME, "col-xs-4").click()
        time.sleep(5)
        print(driver.current_url)
    @pytest.mark.regression
    def test_login_with_incorrect_user_incorrect_pass(self, test_setup):
        driver.find_element(By.ID, "UserName").send_keys("oyed")
        driver.find_element(By.ID, "Password").send_keys("defauogin")
        driver.find_element(By.CLASS_NAME, "col-xs-4").click()
        time.sleep(5)
        print(driver.current_url)

    @pytest.mark.regression
    def test_login_with_blank_user_blank_pass(self, test_setup):
        driver.find_element(By.ID, "UserName").send_keys("o")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.CLASS_NAME, "col-xs-4").click()
        time.sleep(5)
        print(driver.current_url)