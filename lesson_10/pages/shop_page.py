from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def __init__(self, driver, url):
    self.driver = driver
    self.url = url
    self.wait = WebDriverWait(self.driver, 10)


class MainShopPage:

    """Page Object для главной страницы магазина SauceDemo.

    Отвечает за авторизацию и добавление товаров в корзину.
    URL: https://www.saucedemo.com/
    """

    LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ADD_sauce_labs_backpack_BUTTON = (
        By.NAME, 'add-to-cart-sauce-labs-backpack')
    ADD_sauce_labs_bolt_t_shirt_BUTTON = (
        By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_to_cart_sauce_labs_onesie_BUTTON = (
        By.NAME, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver, url):
        """Инициализирует главную страницу магазина.

        :param driver: экземпляр WebDriver для управления браузером.
        :param url: URL главной страницы.
        :param timeout: таймаут ожидания элементов в секундах.
        :return: None
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    def open(self):
        """Открывает главную страницу магазина.
        :return: None
        """
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-one.html"
            )

    def authorization(self):
        """Выполняет вход в магазин по логину и паролю.

        :param login: логин пользователя.
        :param password: пароль пользователя.
        :return: None
        """
        login_input = self.wait.until(EC.presence_of_element_located(
            self.LOGIN_INPUT
        ))
        login_input.send_keys("standard_user")

        password_input = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD_INPUT
        ))
        password_input.send_keys("secret_sauce")

        login_button = self.wait.until(EC.presence_of_element_located(
            self.LOGIN_BUTTON
        ))
        login_button.click()

    def get_add_product(self):
        """Добавляет в корзину три товара: рюкзак, футболку и комбинезон.

        :return: None
        """
        self.wait.until(
          EC.presence_of_element_located(self.ADD_sauce_labs_backpack_BUTTON)
        ).click()
        self.wait.until(
            EC.presence_of_element_located(
                self.ADD_sauce_labs_bolt_t_shirt_BUTTON
                )
        ).click()
        self.wait.until(
            EC.presence_of_element_located(
                self.ADD_to_cart_sauce_labs_onesie_BUTTON
                )
        ).click()


class CartPage:
    """Page Object для корзины и оформления заказа в SauceDemo.

    Отвечает за переход в корзину, заполнение формы checkout
    и проверку итоговой суммы заказа.
    """
    SHOPPING_CART_BUTTON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        """Инициализирует страницу корзины.

        :param driver: экземпляр WebDriver.
        :param url: базовый URL (для возможного перехода).
        :param timeout: таймаут ожидания элементов.
        :return: None
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    def get_shopping_card(self):
        """Кликает по иконке корзины в правом верхнем углу.
        :return: None
        """
        self.wait.until(
            EC.presence_of_element_located(self.SHOPPING_CART_BUTTON)
        ).click()

    def get_checkout(self):
        """Нажимает кнопку Checkout на странице корзины.
        :return: None
        """
        self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BUTTON)
        ).click()

    def get_form(self):
        """Заполняет форму данными покупателя.

        :param first_name: имя покупателя.
        :param last_name: фамилия покупателя.
        :param postal_code: почтовый индекс.
        :return: None"""
        fist_name_input = self.wait.until(EC.presence_of_element_located(
            self.FIRST_NAME_INPUT
        ))
        fist_name_input.send_keys("Kirill")

        last_name_input = self.wait.until(EC.presence_of_element_located(
            self.LAST_NAME_INPUT
        ))
        last_name_input.send_keys("Stanin")

        postal_code_input = self.wait.until(EC.presence_of_element_located(
            self.POSTAL_CODE_INPUT
        ))
        postal_code_input.send_keys("456537")

    def get_continue(self):
        """Нажимает кнопку Continue на форме оформления заказа.
        :return: None
        """
        self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BUTTON)
        ).click()

    def get_total(self):
        """Дожидается появления элемента с итоговой суммой на странице.
        :return: None
        """
        self.wait.until(EC.presence_of_element_located(
            self.TOTAL_VALUE
        ))

    def get_result(self):
        """Дожидается нужного текста суммы и возвращает его.

        :return: строка с итоговой суммой, например «Total: $58.29».
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.TOTAL_VALUE, "Total: $58.29"
            ))
        result_element = self.driver.find_element(*self.TOTAL_VALUE)
        return result_element.text
