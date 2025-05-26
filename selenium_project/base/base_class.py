import datetime


class Base:
    """Базовый класс, содержит универсальные методы"""

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод получения текущей URL"""

        get_url = self.driver.current_url
        print("Текущая URL " + get_url)

    def assert_word(self, word, result):
        """Метод сравнения текстовых значений (заголовки/названия товаров и т.д.)"""

        value_word = word.text
        assert value_word == result
        print("Текст совпадает:", result)

    def assert_num(self, num, result):
        """Метод сравнения числовых значений (цены товаров, сумма в корзине и т.д.)"""

        value_num = num
        assert value_num == result
        print("Числа совпадают:", result)

    def assert_url(self, result):
        """Метод сравнения URL"""

        get_url = self.driver.current_url
        assert get_url == result
        print("URL сопадают: ", result)

    def text_to_num(self, text):
        """Метод перевода цены в виде текста в число (напр. '1 000 руб.' -> '1000')"""

        num_text = ''.join(text.split()).replace('руб.', '').strip() # Удаление лишних символов и пробелов
        try:
            result = int(num_text)
            return result
        except ValueError:
            print("Ошибка конвертации текста в число")

    def products_values_check(self, product_values_to_check, product_values):
        """Сравнение значений для товара"""

        aricle_to_check, name_to_check, price_to_check = product_values_to_check  # Набор значений для проверки
        aricle, name, price = product_values                                      # Исходный набор значений

        print("Артикул: ", aricle)
        self.assert_word(aricle_to_check, aricle)             # Сравнение артикула

        print("Наименование: ", name)
        self.assert_word(name_to_check, name)                 # Сравнение наименования

        print("Цена: ", price)
        num_price_to_check = self.text_to_num(price_to_check)  # Конвертация текстового значения цены в число
        num_price = self.text_to_num(price)                   # Конвертация текстового значения цены в число

        self.assert_num(num_price_to_check, num_price)        # Сравнение цен товаров

    def sum_cart_total_check(self, p1_values, p2_values, cart_total):
        """Проверка суммы товаров с суммой в корзине"""

        aricle_1, name_1, price_1 = p1_values # Набор значений для товара 1
        aricle_2, name_2, price_2 = p2_values # Набор значений для товара 2

        # Конвертация текстовых значений цен в число
        num_price_1 = self.text_to_num(price_1)
        num_price_2 = self.text_to_num(price_2)
        num_cart_total = self.text_to_num(cart_total)

        print("Сумма корзины: ", cart_total)

        sum_price = num_price_1 + num_price_2
        self.assert_num(sum_price, num_cart_total)  # Сравнение суммы цен выбранных товаров и суммы в корзине

    def get_screenshot(self):
        """Метод создания скриншота"""

        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}") # Создание скриншота в папке screen (уже должна существовать)