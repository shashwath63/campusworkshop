"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host=" dpg-chaai067avj5o48vjaf0-a.oregon-postgres.render.com",
        database="todo_app_wdik",
        user="todo_app_wdik_user",
        password="V2bBgQk4pVtSqvpIk9lEbJnsYd6ahuGT")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
