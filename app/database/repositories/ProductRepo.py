import json
from database.db import db
from database.models.Product import Product

class ProductRepo:

  def getAll():
    products = Product.query.all()
    jsonProducts = []
    for i in range(len(products)):
      jsonProducts.append(products[i].toJson())

    return json.dumps(jsonProducts)
  
  def getById(id):
    product = Product.query.filter_by(id=id).first()

    return json.dumps(product.toJson())

  def create(name, price, image, description):
    product = Product(name, price, image, description)
    db.session.add(product)
    db.session.commit()

    return product.toJson()
  
  def update(id, name, price, image, description):
    product = Product.query.filter_by(id=id).first()

    print("product: ",product)
    product.name = name
    product.price = price
    product.image = image
    product.description = description

    db.session.add(product)
    db.session.commit()

    return product.toJson()

  def delete(id):
    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()