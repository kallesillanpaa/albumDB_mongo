from pymongo import MongoClient
import passw

password = passw.PASSWORD
cluster = "mongodb+srv://kalle:"+password+"@cluster0.fnmyz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client.AlbumDB
albums = db.Albums


def add_album(artist,album,year,genre):
    albums.insert_one({
        "artist":artist,
        "album": album,
        "year": year,
        "genre": genre
    })

def fetch_albums():
    result = []
    for row in albums.find():
        result.append(
            row["artist"]+
            " - " +
            row["album"]+
            " - " +
            row["year"]+
            " - " +
            row["genre"]
        )
    return result 
