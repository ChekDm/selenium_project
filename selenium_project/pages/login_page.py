import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):
    """Класс с локаторами и методами для авторизации"""

    url = 'https://www.softmagazin.ru/' # URL тестируемого сайта


    # Locators

    login_link = "//div[@class='login']"                            # Ссылка для авторизации в системе
    login_window_header = "//div[contains(@class, 'popup-title')]"  # Заголовок всплывающего окна авторизации
    username = "//input[@name='USER_LOGIN']"                        # Поле Логин
    password = "//input[@name='USER_PASSWORD']"                     # Поле Пароль
    login_button = "//input[@name='Login']"                         # Кнопка Авторизоваться

    login_menu = "//div[contains(@class, 'user-profile-block')]"  # Меню входа в ЛК
    login_menu_header = "//div[@class='title-drop']"                # Заголовок меню входа в ЛК


    # Getters

    def get_login_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_link)))

    def get_login_window_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window_header)))

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_menu)))

    def get_login_menu_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_menu_header)))

    # Actions

    def click_login_link(self):
        """Нажатие на ссылку Вход в меню"""

        self.get_login_link().click()
        print("Нажатие на ссылку Вход в меню")

    def input_username(self, username):
        """Ввод имени подльзователя"""

        self.get_username().send_keys(username)
        print("Ввод имени подльзователя")

    def input_password(self, password):
        """Ввод пароля"""

        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_login_button(self):
        """Нажатие на кнопку Авторизоваться"""

        self.get_login_button().click()
        print("Нажатие на кнопку Авторизоваться")

    def move_to_login_menu(self):
        """Наведение на меню ЛК пользователя"""

        action = ActionChains(self.driver)
        action.move_to_element(self.get_login_menu()).perform()
        print("Наведение на меню ЛК пользователя")


    # Methods

    def authorization(self):
        """Авторизация в системе"""

        self.driver.get(self.url)                                              # Передача в драйвер URL сайта
        self.driver.maximize_window()                                          # Максимизация окна браузера
        self.get_current_url()                                                 # Получение текущей URL
        self.click_login_link()                                                # Нажатие на кнопку "Вход" в меню для акторизации
        self.assert_word(self.get_login_window_header(), "Авторизация")  # Проверка заголовка в окне Авторизация

        self.input_username("testmail@testmail.com")                           # Ввод логина
        self.input_password("Testpass123")                                     # Ввод пароля
        self.click_login_button()                                              # Нажатие кнопки "Авторизоваться"

        self.move_to_login_menu()                                              # Переход к меню ЛК (для проверки)
        self.assert_word(self.get_login_menu_header(), "Личный кабинет") # Проверка заголовка меню ЛК (успешная авторизация)

        print("Успешная авторизация")