from pymongo import MongoClient
import passw

password = passw.PASSWORD
cluster = "mongodb+srv://kalle:"+password+"@cluster0.fnmyz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client.AlbumDB
albums = db.Albums
