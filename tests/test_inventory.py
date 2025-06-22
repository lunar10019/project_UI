import pytest
import allure
from pages.inventory_page import InventoryPage


@allure.feature("Страница товаров")
class TestInventory:
    @allure.title("Проверка загрузки страницы товаров")
    @allure.story("Основная функциональность страницы товаров")
    def test_inventory_page_loaded(self, login):
        inventory_page = InventoryPage(login)
        assert inventory_page.is_page_loaded()

    @pytest.mark.parametrize(
        "item_name",
        ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"],
    )
    @allure.title("Добавление товара {item_name} в корзину")
    @allure.story("Функциональность работы с корзиной")
    def test_add_to_cart(self, login, item_name):
        inventory_page = InventoryPage(login)
        initial_count = inventory_page.get_cart_items_count()

        inventory_page.add_item_to_cart(item_name)
        new_count = inventory_page.get_cart_items_count()

        assert new_count == initial_count + 1

    @pytest.mark.parametrize(
        "sort_option,expected_order",
        [
            ("A to Z", True),
            ("Z to A", False),
        ],
    )
    @allure.title("Проверка сортировки товаров по {sort_option}")
    @allure.story("Функциональность сортировки товаров")
    def test_sort_items(self, login, sort_option, expected_order):
        inventory_page = InventoryPage(login)
        inventory_page.sort_items(sort_option)

        if "price" in sort_option:
            items = inventory_page.get_item_prices()
        else:
            items = inventory_page.get_item_names()

        if expected_order:
            assert items == sorted(items)
        else:
            assert items == sorted(items, reverse=True)
