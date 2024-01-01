# ================= Main Package ====================
from flask_restful import Resource, Api
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask import Response
import requests
import psutil
import time
import threading
from multiprocessing import Process,Queue
# ==================================================
path_system = "http://127.0.0.1:6111"
# path_system = "http://192.168.117.9:6111"
# ==================================================

app = Flask(__name__)
CORS(app)
api = Api(app)
