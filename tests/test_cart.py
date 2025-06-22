import pytest
import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.feature("Корзина")
class TestCart:
    @pytest.mark.parametrize(
        "item_name",
        ["Sauce Labs Bolt T-Shirt"],
    )
    @allure.title("Удаление товара {item_name} из корзины")
    @allure.story("Функциональность работы с корзиной")
    def test_remove_from_cart(self, login, item_name):
        inventory_page = InventoryPage(login)
        cart_page = CartPage(login)

        inventory_page.add_item_to_cart(item_name)
        initial_count = inventory_page.get_cart_items_count()

        inventory_page.open_cart()
        cart_page.remove_item(item_name)

        new_count = inventory_page.get_cart_items_count()
        assert new_count == initial_count - 1

    @allure.title("Продолжение покупок из корзины")
    @allure.story("Функциональность работы с корзиной")
    def test_continue_shopping(self, login):
        inventory_page = InventoryPage(login)
        cart_page = CartPage(login)

        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.open_cart()

        cart_page.continue_shopping()

        assert "inventory.html" in login.current_url
