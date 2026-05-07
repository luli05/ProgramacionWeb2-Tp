cart = []

def add_to_cart(product):
    cart.append(product)

def remove_from_cart(product_id):
    global cart
    cart = [p for p in cart if p["id"] != product_id]

def get_total():
    return sum(p["price"] for p in cart)