class Product:
    def __init__(self, loja, serial, name, price):
        self.loja = loja
        self.serial = serial
        self.name = name
        self.price = price
    

    def get_args(self):
        return self.loja, self.serial, self.name, self.price