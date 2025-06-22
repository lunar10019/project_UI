from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверить, что страница с товарами загружена")
    def is_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        return True

    @allure.step("Добавить товар {item_name} в корзину")
    def add_item_to_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.driver.find_element(By.XPATH, item_xpath).click()

    @allure.step("Удалить товар {item_name} из корзины")
    def remove_item_from_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button[text()='Remove']"
        self.driver.find_element(By.XPATH, item_xpath).click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge[0].text) if cart_badge else 0

    @allure.step("Открыть корзину")
    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Сортировать товары по {sort_option}")
    def sort_items(self, sort_option):
        self.driver.find_element(By.CLASS_NAME, "product_sort_container").click()
        options = {
            "A to Z": "az",
            "Z to A": "za",
            "Low to High": "lohi",
            "High to Low": "hilo",
        }
        self.driver.find_element(
            By.CSS_SELECTOR, f"option[value='{options[sort_option]}']"
        ).click()

    @allure.step("Получить список названий товаров")
    def get_item_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    @allure.step("Получить список цен товаров")
    def get_item_prices(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(price.text.replace("$", "")) for price in prices]
