from Service.Driver import Amazon
from flask import Blueprint
import json
from Model.Produto import Product
from Service.Driver import Amazon
from Service.DataFormat import Data
from Service.DataBase import Cursor


PdtController = Blueprint("ProductController", __name__)

class ProductController:

    @PdtController.route('/get/product/<serial>', methods=['GET'])
    def get(serial):
        n = Amazon()
        p = Product(*n.get(serial))
        p = p.__dict__
        p["data"] = Data.get_data()
        return json.dumps(p)


    @PdtController.route('/create/product/<serial>')
    def post(serial):
        c = Cursor("teste_db_final")
        
        try:
            c.criar_tabela("Produtos")
        except:
            pass

        n = Amazon()
        p = Product(*n.get(serial))
        c.salva_produto(*p.get_args())

        return f"<p>Produto {p.name} salvo com sucesso!</p>"