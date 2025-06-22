import pytest
import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
class TestCheckout:
    @allure.title("Успешное оформление заказа")
    @allure.story("Полный процесс оформления заказа")
    def test_complete_checkout(self, login):
        inventory_page = InventoryPage(login)
        cart_page = CartPage(login)
        checkout_page = CheckoutPage(login)

        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.open_cart()
        cart_page.checkout()

        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_to_overview()

        checkout_page.finish_checkout()

        assert checkout_page.is_order_complete()

    @pytest.mark.parametrize(
        "first_name,last_name,zip_code",
        [
            ("", "Doe", "12345"),
            ("John", "", "12345"),
            ("John", "Doe", ""),
            ("", "", ""),
        ],
    )
    @allure.title(
        "Попытка оформления с неполными данными: {first_name}, {last_name}, {zip_code}"
    )
    @allure.story("Негативные сценарии оформления заказа")
    def test_checkout_with_missing_info(self, login, first_name, last_name, zip_code):
        inventory_page = InventoryPage(login)
        cart_page = CartPage(login)
        checkout_page = CheckoutPage(login)

        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.open_cart()
        cart_page.checkout()

        checkout_page.fill_checkout_info(first_name, last_name, zip_code)
        checkout_page.continue_to_overview()

        assert "checkout-step-one.html" in login.current_url
