from app import app
import pyrebase
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

api = Api(app)

config = {
    "apiKey": "AIzaSyAPFjcbSU9AcY3pVaUpsr5t-Fai-PPS3KI",
    "authDomain": "kellog-s-recipe-api.firebaseapp.com",
    "databaseURL": "https://kellogg-s-recipe-api.firebaseio.com/",
    "storageBucket": "kellogg-s-recipe-api.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
st = firebase.storage()

class Recipe_List(Resource):
    def get(self):
        recipe_list = db.child("recipe-list").get().val()
        response = jsonify(recipe_list)
        response.status_code = 200
        return response

class Cereal_List(Resource):
    def get(self):
        cereal_list = db.child("cereal-list").get().val()
        response = jsonify(cereal_list)
        response.status_code = 200
        return response

class Image(Resource):
    def get(self, image_name):
        image_title = db.child("images").child(image_name.title()).get().key()
        image_url = db.child("images").child(image_name.title()).get().val()
        response = { image_title:image_url}
        response = jsonify(response)
        response.status_code = 200
        return response


api.add_resource(Recipe_List, '/recipe')
api.add_resource(Cereal_List, '/cereal')
api.add_resource(Image, '/image/<image_name>')

