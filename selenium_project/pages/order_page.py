import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from base.base_class import Base



class Order_page(Base):
    """Класс содержит локаторы и методы для страницы оформления заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    order_page_header = "//div[@class='page-title']/h1"                 # Заголовок страницы Оформление заказа

    product_1_article = "(//div[@class='bx-scu-container'])[1]/div[2]"  # Артикул товара 1
    product_1_name = "(//div[@class='bx-soa-item-title'])[1]/a"         # Наименование товара 1
    product_1_price = "(//strong[@class='bx-price all'])[1]"            # Цена товара 1

    product_2_article = "(//div[@class='bx-scu-container'])[2]/div[2]"  # Артикул товара 2
    product_2_name = "(//div[@class='bx-soa-item-title'])[2]/a"         # Наименование товара 2
    product_2_price = "(//strong[@class='bx-price all'])[2]"            # Цена товара 2

    radio_person_type = "(//input[@name='PERSON_TYPE'])[2]"             # Переключатель Профиль покупателя (Физ. лицо)
    button_next_person_type = "//div[@id='bx-soa-region']//a[contains(@class, 'pull-right btn')]" # Кнопка Далее в разделе Профиль покупателя

    full_name = "//input[@id='soa-property-16']"    # ФИО
    phone_number = "//input[@id='soa-property-18']" # Телефон
    e_mail = "//input[@id='soa-property-17']"       # E-mail
    button_next_contacts = "//div[@id='bx-soa-properties']//a[contains(@class, 'pull-right btn')]"  # Кнопка Далее в разделе Данные покупателя
    button_next_delivery = "//div[@id='bx-soa-delivery']//a[contains(@class, 'pull-right btn')]"    # Кнопка Далее в разделе Доставка

    cart_total_price = "(//div[@class='bx-soa-cart-total-line bx-soa-cart-total-line-total'])[2]/span[@class='bx-soa-cart-d']"  # Сумма товаров к оплате

    checkout_button = "(//div[@class='bx-soa-cart-total-button-container'])[2]/a" # Кнопка Оформить заказ


    # Getters

    def get_order_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.order_page_header)))

    def get_product_1_article(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_article)))

    def get_product_1_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_name)))

    def get_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_price)))

    def get_product_2_article(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_article)))

    def get_product_2_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_name)))

    def get_product_2_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_price)))

    def get_radio_person_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_person_type)))

    def get_button_next_person_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_next_person_type)))

    def get_full_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_e_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail)))

    def get_button_next_contacts(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_next_contacts)))

    def get_button_next_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_next_delivery)))

    def get_cart_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.cart_total_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def click_radio_person_type(self):
        """Нажатие на переключатель в разделе Профиль покупателя"""

        self.get_radio_person_type().click()
        print("Нажатие на переключатель в разделе Профиль покупателя")

    def click_button_next_person_type(self):
        """Нажатие на Кнопку Далее в разделе Профиль покупателя"""

        self.get_button_next_person_type().click()
        print("Нажатие на Кнопку Далее в разделе Профиль покупателя")

    def input_full_name(self, full_name):
        """Ввод ФИО"""

        self.get_full_name().send_keys(full_name)
        print("Ввод ФИО")

    def input_phone_number(self, phone_number):
        """Ввод Телефона"""

        self.get_phone_number().send_keys(phone_number)
        print("Ввод Телефона")

    def input_e_mail(self, e_mail):
        """Ввод E-mail"""

        self.get_e_mail().send_keys(e_mail)
        print("Ввод E-mail")

    def click_button_next_contacts(self):
        """Нажатие на Кнопка Далее в разделе Данные покупателя"""

        self.get_button_next_contacts().click()
        print("Нажатие на Кнопка Далее в разделе Данные покупателя")

    def click_button_next_delivery(self):
        """Нажатие на Кнопка Далее в разделе Доставка"""

        self.get_button_next_delivery().click()
        print("Нажатие на Кнопка Далее в разделе Доставка")

    def click_checkout_button(self):
        """Нажатие на кнопку Оформить заказ"""

        self.get_checkout_button().click()
        print("Нажатие на кнопку Оформить заказ")

    # Methods

    def card_values_check(self, product_1_values, product_2_values):
        """Сравнение значений для товаров"""

        product_1_values_to_check = self.get_product_1_article(), self.get_product_1_name(), self.get_product_1_price().text
        self.products_values_check(product_1_values_to_check, product_1_values)

        product_2_values_to_check = self.get_product_2_article(), self.get_product_2_name(), self.get_product_2_price().text
        self.products_values_check(product_2_values_to_check, product_2_values)

    def card_sum_check(self, product_1_values, product_2_values):
        """Проверка суммы товаров и суммы в корзине"""

        self.sum_cart_total_check(product_1_values, product_2_values, self.get_cart_total_price().text)

    def order_page_confirmation(self):
        """Заполнение и подтверждение данных на Странице заказа"""

        self.assert_url("https://www.softmagazin.ru/personal/order/")              # Проверка URL
        self.assert_word(self.get_order_page_header(), "Оформление заказа")  # Проверка заголовка

        self.click_radio_person_type()          # Нажатие на переключатель Профиль покупателя (Физ. лицо)
        time.sleep(1)
        self.click_button_next_person_type()    # Нажатие на кнопку Далее в Профиль покупателя

        # Генерация данных покупателя в библиотеке Faker

        faker_ru = Faker('ru_RU')
        full_name = faker_ru.name()
        phone_number = faker_ru.phone_number()
        e_mail = faker_ru.email()

        # Заполение полей формы данными покупателя

        self.input_full_name(full_name)
        self.input_phone_number(phone_number)
        self.input_e_mail(e_mail)

        time.sleep(1)
        self.click_button_next_contacts()  # Нажатие на кнопку Далее в разделе Контакты
        self.click_button_next_delivery()  # Нажатие на кнопку Далее в разделе Доставка

        self.click_checkout_button()       # Нажатие на кнопку Оформить заказ

