
from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://pubudu093:g05cHBrMMbglU7YW@cluster0.e1gwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
uri = "mongodb+srv://pubudu093:PubuduKuka123@cluster0.e1gwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    
