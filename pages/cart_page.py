from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверить, что страница корзины загружена")
    def is_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cart_contents_container"))
        )
        return True

    @allure.step("Получить список товаров в корзине")
    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    @allure.step("Удалить товар {item_name} из корзины")
    def remove_item(self, item_name):
        item_xpath = (
            f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button"
        )
        self.driver.find_element(By.XPATH, item_xpath).click()

    @allure.step("Нажать кнопку 'Continue Shopping'")
    def continue_shopping(self):
        self.driver.find_element(By.ID, "continue-shopping").click()

    @allure.step("Нажать кнопку 'Checkout'")
    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
