from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('C:/bin/chromedriver.exe', chrome_options=chrome_options)

class Aliexpress(Driver):
    loja = "Aliexpress"

    def __init__(self):
        super().__init__()

    def get(self, serial):
        self.driver.get(f'https://www.aliexpress.com/item/{serial}.html')
        price = self.driver.find_element_by_class_name('product-price-value').text
        name = self.driver.find_element_by_class_name('product-title-text').text
        return self.loja, serial, name, price


class Amazon(Driver):
    loja = "Amazon"

    def __init__(self):
        super().__init__()

    def get(self, serial):
        self.driver.get((f'https://www.amazon.com.br/dp/{serial}/'))
        price = self.driver.find_element_by_id('price_inside_buybox').text
        name = self.driver.find_element_by_id('productTitle').text
        return self.loja, serial, name, price

#n = Amazon()
#print(n)
#produto = Product(*n.get("B085FXDTTX"))
#print(produto)
#print(produto.loja, produto.serial, produto.name, produto.price)

""" print(produto.name)
print(produto.price)
print(produto.serial)
print(produto.loja)
 """

""" a = Aliexpress()
print(a)
print(a.get("33058450105"))
print(produto)
 """


