import allure
import pytest
from selenium import webdriver
from pages.shop_page import CartPage
from pages.shop_page import MainShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("SauceDemo Shop")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Покупка трёх товаров в SauceDemo с проверкой итоговой суммы")
@allure.description("Тест выполняет полный сценарий: авторизация на сайте, добавление трёх "
                    "товаров в корзину (рюкзак, футболка, комбинезон), переход в корзину, "
                    "оформление заказа с заполнением данных покупателя и проверку, что "
                    "итоговая сумма равна $58.29."
                    )
def test_shop(driver):
    with allure.step("Открыть главную страницу и авторизоваться"):
        shop_page = MainShopPage(driver, "https://www.saucedemo.com/")
        shop_page.open()
        shop_page.authorization()

    with allure.step("Добавить три товара в корзину"):
        shop_page.get_add_product()

    with allure.step("Перейти в корзину"):
        shop_page = CartPage(driver, "https://www.saucedemo.com/cart.html")
        shop_page.get_shopping_card()
        shop_page.get_checkout()

    with allure.step("Заполнить форму данных покупателя"):
        shop_page.get_form()

    with allure.step("Нажать Continue и дождаться итоговой суммы"):
        shop_page.get_continue()
        shop_page.get_total()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        result = shop_page.get_result()
        assert shop_page.get_result() == "Total: $58.29", (
            f"Ожидалась сумма 'Total: $58.29', получено '{result}'"
            )
