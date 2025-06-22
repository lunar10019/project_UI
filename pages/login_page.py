from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ввести логин {username} и пароль {password}")
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Проверить отображение ошибки")
    def is_error_message_displayed(self):
        error_element = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        return error_element.is_displayed()
