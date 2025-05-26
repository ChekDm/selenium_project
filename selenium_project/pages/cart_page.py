from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):
    """Класс содержит локаторы и методы для страницы подтверждения товара в корзине"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_header = "//div[@class='basket-items-list-header']//h1"                                                             # Заголовок страницы Корзина

    product_1_article = "(//div[@class='basket-item-property-custom-value'])[1]"                                             # Артикул товара 1
    product_1_name = "(//a[@class='basket-item-info-name-link'])[1]"                                                         # Наименование товара 1
    product_1_price_cart = "(//td[@class='basket-items-list-item-price'])[1]//span[@class='basket-item-price-current-text']" # Цена товара 1

    product_2_article = "(//div[@class='basket-item-property-custom-value'])[2]"                                             # Артикул товара 2
    product_2_name = "(//a[@class='basket-item-info-name-link'])[2]"                                                         # Наименование товара 2
    product_2_price_cart = "(//td[@class='basket-items-list-item-price'])[2]//span[@class='basket-item-price-current-text']" # Цена товара 2

    cart_total_price = "//div[@class='basket-coupon-block-total-price-current']"         # Сумма товаров в корзине

    checkout_button = "//button[@class='basket-checkout-order-btn basket-btn-checkout']" # Кнопка Оформить заказ

    # Getters

    def get_cart_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_header)))

    def get_product_1_article(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_article)))

    def get_product_1_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_name)))

    def get_product_1_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_price_cart)))

    def get_product_2_article(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_article)))

    def get_product_2_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_name)))

    def get_product_2_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_price_cart)))

    def get_cart_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.cart_total_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def click_checkout_button(self):
        """Нажатие на кнопку Оформить заказ"""

        self.get_checkout_button().click()
        print("Нажатие на кнопку Оформить заказ")


    # Methods

    def card_values_check(self, product_1_values, product_2_values):
        """Сравнение значений для товаров"""

        # Получение для товара 1: Артикул товара, Название товара, Цена товара
        product_1_values_to_check = self.get_product_1_article(), self.get_product_1_name(), self.get_product_1_price_cart().text
        # Сравнение значений для товара 1
        self.products_values_check(product_1_values_to_check, product_1_values)

        # Получение для товара 2: Артикул товара, Название товара, Цена товара
        product_2_values_to_check = self.get_product_2_article(), self.get_product_2_name(), self.get_product_2_price_cart().text
        # Сравнение значений для товара 2
        self.products_values_check(product_2_values_to_check, product_2_values)

    def card_sum_check(self, product_1_values, product_2_values):
        """Проверка суммы товаров и суммы в корзине"""

        self.sum_cart_total_check(product_1_values, product_2_values, self.get_cart_total_price().text)

    def product_confirmation(self):
        """Подтверждение товаров в корзине"""

        self.assert_url("https://www.softmagazin.ru/personal/basket/")  # Проверка URL
        self.assert_word(self.get_cart_header(), "Ваша корзина")  # Проверка заголовка
        self.click_checkout_button()                                    # Нажатие на кнопку Оформить заказ

