import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    """Класс содержит локаторы и методы для главной страницы с товарами"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    menu_soft = "//ul[@class='top-level']/li[2]"                            # Главное меню - Программное обеспечение
    submenu_os = "//li[@class='dropdown Ioperatsionnye-sistemy']"           # Подменю - Операционные системы

    page_header = "//div[@class='section-soft-custom-top-block']/h1"        # Заголовок страницы

    filter_os_producer = "(//span[@class='bx-filter-input-checkbox'])[3]/span"   # Фильтр - Производитель (Базальт СПО)
    filter_type_soft = "(//span[@class='bx-filter-input-checkbox'])[17]/span"    # Фильтр - Тип поставки (Электронная)
    filter_lic_type = "(//span[@class='bx-filter-input-checkbox'])[23]/span"     # Фильтр - Тип лицензии (Базовая)
    filter_in_stock = "(//span[@class='bx-filter-input-checkbox'])[27]/span"     # Фильтр - Статус товара по наличию (В наличии)
    filter_lic_period = "(//span[@class='bx-filter-input-checkbox'])[31]/span"   # Фильтр - Срок действия лицензии (Бессрочная)

    button_set_filter = "//input[@id='set_filter']"                         # Кнопка - Показать (применение фильтров)

    product_1_list = "(//div[@class='wrapper-info-product'])[1]//span[@class='toggler']"             # Элемент раскрытия вып. списка для товара 1
    product_1_article_1 = "((//div[@class='wrapper-info-product'])[1]//span[@class='articul'])[1]"   # Артикул 1 товара в вып. списке
    product_1_name_1 = "((//div[@class='wrapper-info-product'])[1]//a[@class='name'])[1]"            # Имя 1 товара в вып. списке
    product_1_price_1 = "((//div[@class='wrapper-info-product'])[1]//span[@class='price'])[1]"       # Цена 1 товара в вып. списке
    product_1_add_to_cart_1 = "((//div[@class='wrapper-info-product'])[1]//span[@class='button-buy btn-offer-buy '])[1]" # Кнопка Добавить в корзину для 1 товара в вып. списке

    product_2_list = "(//div[@class='wrapper-info-product'])[2]//span[@class='toggler']"             # Элемент раскрытия вып. списка для товара 2
    product_2_article_1 = "((//div[@class='wrapper-info-product'])[2]//span[@class='articul'])[1]"   # Артикул 1 товара в вып. списке
    product_2_name_1 = "((//div[@class='wrapper-info-product'])[2]//a[@class='name'])[1]"            # Имя 1 товара в вып. списке
    product_2_price_1 = "((//div[@class='wrapper-info-product'])[2]//span[@class='price'])[1]"       # Цена 1 товара в вып. списке
    product_2_add_to_cart_1 = "((//div[@class='wrapper-info-product'])[2]//span[@class='button-buy btn-offer-buy '])[1]" # Кнопка Добавить в корзину для 1 товара в вып. списке

    add_to_cart_window_header = "//form[@id='ajax_buy']/div" # Заголовок окна успешного добавления в корзину
    button_continue = "//input[@name='button_reset']"        # Кнопка Продолжить покупки в окне Добавлено в корзину

    button_cart = "//div[contains(@class, 'user-basket-block')]"    # Кнопка Корзина в верхнем меню

    # Getters

    def get_menu_soft(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_soft)))

    def get_submenu_os(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submenu_os)))

    def get_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_header)))

    def get_filter_os_producer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_os_producer)))

    def get_filter_type_soft(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_type_soft)))

    def get_filter_lic_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_lic_type)))

    def get_filter_in_stock(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_in_stock)))

    def get_filter_lic_period(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_lic_period)))

    def get_button_set_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_set_filter)))

    def get_product_1_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_list)))

    def get_product_1_article_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_article_1)))

    def get_product_1_name_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_name_1)))

    def get_product_1_price_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_price_1)))

    def get_product_1_add_to_cart_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_add_to_cart_1)))

    def get_product_2_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_list)))

    def get_product_2_article_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_article_1)))

    def get_product_2_name_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_name_1)))

    def get_product_2_price_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_price_1)))

    def get_product_2_add_to_cart_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_add_to_cart_1)))

    def get_add_to_cart_window_header(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.add_to_cart_window_header)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))


    # Actions

    def move_to_menu_soft(self):
        """Наведение на главное меню - Программное обеспечение"""

        action = ActionChains(self.driver)
        action.move_to_element(self.get_menu_soft()).perform()
        print("Наведение на главное меню - Программное обеспечение")

    def move_to_submenu_os(self):
        """Открытие подменю - Операционные системы"""

        self.get_submenu_os().click()
        print("Открытие подменю - Операционные системы")

    def click_filter_os_producer(self):
        """Установка фильтра Производитель"""

        self.get_filter_os_producer().click()
        print("Установка фильтра Производитель (BaseALT)")

    def click_filter_type_soft(self):
        """Установка фильтра Тип поставки"""

        self.get_filter_type_soft().click()
        print("Установка фильтра Тип поставки (Электронная лицензия)")

    def click_filter_lic_type(self):
        """Установка фильтра Тип лицензии"""

        self.get_filter_lic_type().click()
        print("Установка фильтра Тип лицензии (Базовая)")

    def click_filter_in_stock(self):
        """Установка фильтра Статус товара по наличию"""

        self.get_filter_in_stock().click()
        print("Установка фильтра Статус товара по наличию (в наличии)")

    def click_filter_lic_period(self):
        """Установка фильтра Срок действия лицензии"""

        self.get_filter_lic_period().click()
        print("Установка фильтра Срок действия лицензии (Бессрочная)")

    def click_button_set_filter(self):
        """Нажатие на кнопку Показать (применение фильтров)"""

        self.get_button_set_filter().click()
        print("Нажатие на кнопку Показать (применение фильтров)")

    def click_product_1_list(self):
        """Нажатие на Элемент раскрытия вып. списка для товара 1"""

        self.get_product_1_list().click()
        print("Нажатие на Элемент раскрытия вып. списка для товара 1")

    def click_product_1_add_to_cart_1(self):
        """Нажатие на Кнопку Добавить в корзину для 1 товара в вып. списке"""

        self.get_product_1_add_to_cart_1().click()
        print("Нажатие на Кнопку Добавить в корзину для 1 товара в вып. списке")

    def click_product_2_list(self):
        """Нажатие на Элемент раскрытия вып. списка для товара 2"""

        self.get_product_2_list().click()
        print("Нажатие на Элемент раскрытия вып. списка для товара 2")

    def click_product_2_add_to_cart_1(self):
        """Нажатие на Кнопку Добавить в корзину для 1 товара в вып. списке"""

        self.get_product_2_add_to_cart_1().click()
        print("Нажатие на Кнопку Добавить в корзину для 1 товара в вып. списке")

    def click_button_continue(self):
        """Нажатие на Кнопку Продолжить Покупки в окне Добавлено в корзину"""

        self.get_button_continue().click()
        print("Нажатие на Кнопку Продолжить Покупки в окне Добавлено в корзину")

    def click_button_cart(self):
        """Нажатие на кнопку Корзины"""

        self.get_button_cart().click()
        print("Нажатие на кнопку Корзины")


    # Methods

    def open_category_os(self):
        """Открытие категории в меню Программное обеспечение - Операционные системы"""

        self.move_to_menu_soft()
        self.move_to_submenu_os()
        self.assert_word(self.get_page_header(), "Операционные системы")    # Проверка заголовка страницы
        self.assert_url("https://www.softmagazin.ru/soft/operatsionnye-sistemy/") # Проверка URL страницы


    def set_filters_os(self):
        """Включение фильтров сортировки товаров в категории Операционные системы"""

        self.click_filter_os_producer() # Установка фильтра Производитель (BaseALT)
        self.click_filter_type_soft()   # Установка фильтра Тип поставки (Электронная лицензия)
        self.click_filter_lic_type()    # Установка фильтра Тип лицензии (Базовая)
        self.click_filter_in_stock()    # Установка фильтра Статус товара по наличию (в наличии)
        self.click_filter_lic_period()  # Установка фильтра Срок действия лицензии (Бессрочная)
        self.click_button_set_filter()  # Нажатие на кнопку Показать (применение фильтров)

    def product_1_add_to_cart(self):
        """Добавление товара 1 в корзину"""

        self.click_product_1_list()                                     # Нажатие на Элемент раскрытия вып. списка для товара 1
        product_1_article_value = self.get_product_1_article_1().text   # Значение артикула товара
        product_1_name_value = self.get_product_1_name_1().text         # Значение названия товара
        product_1_price_value = self.get_product_1_price_1().text       # Значение цены товара
        print("Артикул товара 1 - ", product_1_article_value)
        print("Название товара 1 - ", product_1_name_value)
        print("Цена товара 1 - ", product_1_price_value)

        self.click_product_1_add_to_cart_1()                                                 # Нажатие на Кнопку Добавить в корзину для 1 товара в вып. списке
        self.assert_word(self.get_add_to_cart_window_header(), "Добавлено в корзину")  # Проверка заголовка страницы
        self.click_button_continue()                                                         # Нажатие на Кнопку Продолжить Покупки в окне Добавлено в корзину
        time.sleep(1)                                                                        # Задержка до исчезновения всплывающего окна
        self.click_product_1_list()                                                          # Нажатие на Элемент скрытия вып. списка для товара 1

        return product_1_article_value, product_1_name_value, product_1_price_value          # Возврат значений Артикул товара, Название товара Цена товара 1

    def product_2_add_to_cart(self):
        """Добавление товара 2 в корзину"""

        self.click_product_2_list()                                     # Нажатие на Элемент раскрытия вып. списка для товара 2
        product_2_article_value = self.get_product_2_article_1().text   # Значение артикула товара
        product_2_name_value = self.get_product_2_name_1().text         # Значение названия товара
        product_2_price_value = self.get_product_2_price_1().text       # Значение цены товара
        print("Артикул товара 1 - ", product_2_article_value)
        print("Название товара 1 - ", product_2_name_value)
        print("Цена товара 1 - ", product_2_price_value)

        self.click_product_2_add_to_cart_1()                                                 # Нажатие на Кнопку Добавить в корзину для 1 товара в вып. списке
        self.assert_word(self.get_add_to_cart_window_header(), "Добавлено в корзину")  # Проверка заголовка страницы
        self.click_button_continue()                                                         # Нажатие на Кнопку Продолжить Покупки в окне Добавлено в корзину
        time.sleep(1)                                                                        # Задержка до исчезновения всплывающего окна
        self.click_product_2_list()                                                          # Нажатие на Элемент скрытия вып. списка для товара 2

        return product_2_article_value, product_2_name_value, product_2_price_value          # Возврат значений Артикул товара, Название товара Цена товара 2

    def open_cart(self):
        """Открытие страницы Корзина"""

        self.click_button_cart()    # Нажатие на кнопку Корзины

