
from flask import Flask
from flask_restx import Api, Resource, fields
from products import products
from cart import cart


app = Flask(__name__)


api = Api(
    app,
    title="Carrito Blanqueria API",
    version="1.0",
    description="API para gestionar productos y carrito de compras"
)

# listar productos
@api.route("/products")
class Products(Resource):
    def get(self):
        return products


# agregar al carrito
@api.route("/cart")
class Cart(Resource):

    def get(self):
        return cart

    def post(self):
        from flask import request

        data = request.json
        product_id = data["product_id"]

        product = next((p for p in products if p["id"] == product_id), None)

        if product:
            cart.append(product)
            return {"message": "Producto agregado", "cart": cart}

        return {"error": "Producto no encontrado"}, 404


# eliminar producto
@api.route("/cart/<int:product_id>")
class RemoveProduct(Resource):

    def delete(self, product_id):
        global cart
        cart[:] = [p for p in cart if p["id"] != product_id]

        return {"message": "Producto eliminado", "cart": cart}


# calcular total
@api.route("/cart/total")
class CartTotal(Resource):

    def get(self):
        total = sum(p["price"] for p in cart)
        return {"total": total}


