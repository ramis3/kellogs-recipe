from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)


from app import kellogs_rest_api