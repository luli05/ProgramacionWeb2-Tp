from fastapi import FastAPI
from models import products
from cart import cart, add_to_cart, remove_from_cart, get_total

app = FastAPI()

@app.get("/products")
def list_products():
    return products


@app.post("/cart/{product_id}")
def add_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        add_to_cart(product)
        return {"message": "Producto agregado"}
    return {"error": "Producto no encontrado"}


@app.delete("/cart/{product_id}")
def remove_product(product_id: int):
    remove_from_cart(product_id)
    return {"message": "Producto eliminado"}


@app.get("/cart")
def view_cart():
    return cart


@app.get("/cart/total")
def total():
    return {"total": get_total()}