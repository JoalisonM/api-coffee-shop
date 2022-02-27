from database.db import db
from database.models import Product

class ProductRepo:

  def create(name, price, image, description):
    product = Product(name, price, image, description)
    db.session.add(product)
    db.session.commit()

    return product.toJson()
  
  def getAll():
    products = db.session.query(Product).all()
    jsonProducts = []
    for i in range(len(products)):
      jsonProducts.append(products[i].toJson())

    return jsonProducts
  
  def getById(id):
    products = db.session.query(Product).filter(Product.id == id).first()
    jsonProducts = []
    for i in range(len(products)):
      jsonProducts.append(products[i].toJson())

    return jsonProducts