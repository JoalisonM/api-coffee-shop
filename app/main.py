from database.db import db
from flask import Flask, request
from database.repositories.ProductRepo import ProductRepo

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
app.app_context().push()

with app.app_context():
  db.create_all()

# Select all
@app.route("/products", methods=["GET"])
def getAllProducts():
  products = ProductRepo.getAll
  print("products: ",products)
  return products

@app.route("/products/<id>", methods=["GET"])
def getProductById(id):
  product = ProductRepo.getById(id=id)

  if (not len(product)):
    return response(400, "Não tem nenhum produto com esse id")

  print("product: ",product)
  return product

#create product
@app.route("/products", methods=["POST"])
def createProduct():
    body = request.get_json()

    product = ProductRepo.create(
      body["name"],
      body["price"],
      body["image"],
      body["description"], 
    )

    print("PRODUCT: ",product)

    return response(200, "Usuário criado", "product", product)

def response(status, message, nameContent=False, content=False):
  response = {}
  response["status"] = status
  response["message"] = message

  if(nameContent and content):
    response[nameContent] = content

  return response

app.run()