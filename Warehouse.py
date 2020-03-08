class warehouse:
    def __init__(self,product,product_type,inventry):
        self.product = product
        self.product_type= product_type
        self.inventory = inventory
        
items = {}

class product:
    def __init__(self, prdt_name, prdt_id, prdt_type):
        self.prdt_id=prdt_id
        self.prdt_name=prdt_name
        self.prdt_type=prdt_type

def add_product(product):
    if not items.get(product.prdt_id):
        items[product.prdt_id] = 1
        
    else:
        items[product.prdt_id] =+ 1
        
product = product('Furniture',100, 'Table' )


add_product(product)
print(items)


class inventory:
    def __init__(self, prdt_id, quantity):
        self.prdt_id=prdt_id
        self.quantity=quantity
        
def add_product(product):
    if not items.get(product.prdt_id):
        items[product.prdt_id] = 1
        
    else:
        items[product.prdt_id] =+ 1
        
product = inventory('Furniture',100, )


add_product(product)
print(items)
