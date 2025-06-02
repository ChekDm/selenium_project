import time
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.order_page import Order_page


# @pytest.mark.run(order=1)                    # Очередность теста
def test_buy_product(set_up):
    """Процедура покупки товаров (pytest)"""

    # options = webdriver.FirefoxOptions()      # Параметры для запуска браузера
    # options.add_argument("--headless")        # Запуск браузера в headless режиме
    # driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    lp = Login_page(driver)                     # Создание экземпляра класса Login_page
    lp.authorization()                          # Запуск метода Авторизация в системе
    mp = Main_page(driver)                      # Создание экземпляра класса Main_page
    mp.open_category_os()                       # Запуск метода Открытие категории Операционные системы
    mp.set_filters_os()                         # Включение фильтров сортировки товаров в категории Операционные системы
    p1_values = mp.product_1_add_to_cart()      # Добавление товара 1 в корзину, сохранение данных о товаре 1 в p1_values
    p2_values = mp.product_2_add_to_cart()      # Добавление товара 2 в корзину, сохранение данных о товаре 2 в p2_values
    mp.open_cart()                              # Переход в корзину

    cp = Cart_page(driver)                      # Создание экземпляра класса Cart_page
    cp.card_values_check(p1_values, p2_values)  # Проверка соответствия артикула, названия и цены выбранных товаров с товарами в корзине
    cp.card_sum_check(p1_values, p2_values)     # Проверка суммы товаров и суммы в корзине
    cp.product_confirmation()                   # Подтверждение товара в корзине

    op = Order_page(driver)                     # Создание экземпляра класса Order_page
    op.card_values_check(p1_values, p2_values)  # Проверка соответствия артикула, названия и цены выбранных товаров с товарами на странице подтв. заказа
    op.order_page_confirmation()                # Заполнение и подтверждение данных на Странице заказа
    op.card_sum_check(p1_values, p2_values)     # Проверка суммы выбранных товаров и суммы на странице подтв. заказа

    fp = Finish_page(driver)                    # Создание экземпляра класса Finish_page
    fp.finish()                                 # Проверка данных заказа на финальной странице и создание скриншота

    time.sleep(3)
    driver.close()