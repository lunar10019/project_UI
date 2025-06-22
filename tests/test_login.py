import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Авторизация")
class TestLogin:
    @allure.title("Успешная авторизация")
    @allure.story("Позитивный сценарий авторизации")
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url

    @allure.title("Неуспешная авторизация с неверным паролем")
    @allure.story("Негативный сценарий авторизации")
    def test_failed_login_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "wrong_password")

        assert login_page.is_error_message_displayed()

    @pytest.mark.parametrize(
        "username,password",
        [
            ("locked_out_user", "secret_sauce"),
            ("", "secret_sauce"),
            ("standard_user", ""),
            ("", ""),
        ],
    )
    @allure.title("Неуспешная авторизация с параметрами: {username}, {password}")
    @allure.story("Негативные сценарии авторизации с параметризацией")
    def test_failed_login_params(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        assert login_page.is_error_message_displayed()
