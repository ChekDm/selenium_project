from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Finish_page(Base):
    """Класс содержит локаторы и методы для финальной страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    order_number = "//div[@class='container-confirm-custom']/div[2]"            # Сообщение с номером заказа - "Ваш заказ №XXXXXX"
    order_success_msg = "//div[@class='container-confirm-custom']/div[3]/span"  # Сообщение об успешном завершении заказа - "успешно создан."


    # Getters

    def get_order_number(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.order_number)))

    def get_order_success_msg(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.order_success_msg)))

    # Actions

    # Methods

    def finish(self):
        """Проверка данных заказа на финальной странице и создание скриншота"""

        order_number = self.get_order_number().text.replace("Ваш заказ №", "")      # Получение номера заказа и удаление лишних символов
        self.assert_url(f"https://www.softmagazin.ru/personal/order/?ORDER_ID={order_number}")  # Проверка URL (содержит номер заказа)
        self.assert_word(self.get_order_success_msg(), "успешно создан.")                 # Проверка заголовка
        self.get_screenshot()                                                                   # Создание скриншота
        print("Screen OK")