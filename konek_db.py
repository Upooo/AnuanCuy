from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

anu = "mongodb+srv://arya22062:1paPdTSovW5wu6dT@cluster0.9zizz7v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
jembut = MongoClient(anu, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    jembut.admin.command('ping')
    print("KALO ADA TEXT INI TAU KAN ARTINYA APA? UDAH KONEK JING!")
except Exception as ewean:
    print(ewean)