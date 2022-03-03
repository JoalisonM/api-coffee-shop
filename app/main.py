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

# Select all products
@app.route("/products", methods=["GET"])
def getAllProducts():
  products = ProductRepo.getAll()

  return products

# Select product by id
@app.route("/products/<int:id>", methods=["GET"])
def getProductById(id):
  try:
    product = ProductRepo.getById(id=id)

    if (len(product) > 0):
      return product

  except:
    return response(400, "Não tem nenhum produto com esse id")

# Create product
@app.route("/products", methods=["POST"])
def createProduct():
  body = request.get_json()
  
  if ("name" not in body):
    return response(400, "O name é obrigatório")
  
  if ("price" not in body):
    return response(400, "O price é obrigatório")
  
  if ("image" not in body):
    return response(400, "O image é obrigatório")
  
  if ("description" not in body):
    return response(400, "O description é obrigatório")

  product = ProductRepo.create(
    name = body["name"],
    price = body["price"],
    image = body["image"],
    description = body["description"], 
  )

  return response(201, "Produto criado com sucesso", "product", product)

# Update product
@app.route("/products/<int:id>", methods=["PUT"])
def updateProduct(id):
  try:
    body = request.get_json()

    product = ProductRepo.update(
      id,
      body["name"],
      body["price"],
      body["image"],
      body["description"], 
    )

    return response(201, "Produto atualizado com sucesso", "product", product)

  except:
    return (400, "Erro ao atualizar produto", "products", {})

# Update product name
@app.route("/products/<int:id>", methods=["PATCH"])
def updateProductName(id):
  try:
    body = request.get_json()

    product = ProductRepo.updateName(
      id,
      body["name"]
    )

    return response(201, "Nome do produto atualizado com sucesso", "product", product)
  except:
    return (400, "Erro ao atualizar nome do produto", "products", {})

# Delete product
@app.route("/products/<int:id>", methods=["DELETE"])
def deleteProduct(id):
  try:
    ProductRepo.delete(id)

    return response(201, "Produto deletado com sucesso")

  except Exception as e:
    print("Erro: ",e)
    return response(400, "Erro ao deletar produto", "products", {})

def response(status, message, nameContent=False, content=False):
  response = {}
  response["status"] = status
  response["message"] = message

  if(nameContent and content):
    response[nameContent] = content

  return response

app.run()