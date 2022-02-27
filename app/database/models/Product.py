from database.db import db

class Product(db.Model):
  __tablename__ = 'product'
  id          = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
  name        = db.Column("name", db.String(100))
  price       = db.Column("price", db.String(100))
  image       = db.Column("image", db.String(400))
  description = db.Column("description", db.String(400))

  def __init__(self, id, name, price, image, description):
    self.id = id
    self.name = name
    self.price = price
    self.image = image
    self.description = description
  
  def toJson(self):
    return {
      "id": self.id,
      "name": self.name,
      "price": self.price,
      "image": self.image,
      "description": self.description
    }