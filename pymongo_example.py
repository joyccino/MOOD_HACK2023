from pymongo import MongoClient
client = MongoClient('mongodb+srv://joy:4hackathon@clusterforhackathon.5s924x7.mongodb.net/?retryWrites=true&w=majority')

db = client.emotion_storage

doc = {'emotion':'happy','probability':100} # 데이터 하나
db.mood_collection.insert_one(doc)