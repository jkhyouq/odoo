class Product:
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription
class PropertyChargeAct:
    def __init__(self, source_warehouse, destination_warehouse, product, quantity, status):
        self.source_warehouse = source_warehouse
        self.destination_warehouse = destination_warehouse
        self.product = product
        self.quantity = quantity
        self.status = status
def apply(self):
    if self.status == "Покупка":
        self.create_marked_products()
    else:
        self.update_market_product_properties()
def create_marked_products(self):
    pass
def update_market_product_properties(self):
    pass


