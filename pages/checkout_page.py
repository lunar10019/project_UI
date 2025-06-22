from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверить, что страница оформления заказа загружена")
    def is_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "checkout_info_container"))
        )
        return True

    @allure.step(
        "Заполнить информацию для оформления заказа: {first_name}, {last_name}, {zip_code}"
    )
    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    @allure.step("Нажать кнопку 'Continue'")
    def continue_to_overview(self):
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Нажать кнопку 'Finish'")
    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()

    @allure.step("Проверить сообщение об успешном оформлении заказа")
    def is_order_complete(self):
        complete_header = self.driver.find_element(By.CLASS_NAME, "complete-header")
        return complete_header.text == "Thank you for your order!"

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self):
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return float(total.replace("Total: $", ""))
