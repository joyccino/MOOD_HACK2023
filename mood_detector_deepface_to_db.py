import cv2 as cv
from deepface import DeepFace
import math

from pymongo import MongoClient
client = MongoClient('mongodb+srv://joy:4hackathon@clusterforhackathon.5s924x7.mongodb.net/?retryWrites=true&w=majority')

db = client.emotion_storage

cap = cv.VideoCapture(0)

space_pressed = False
esc_pressed = False

while True:
    ret, frame = cap.read()

    img_path = 'output/capture.jpg'
    cv.imwrite(img_path, frame)

    try:
        predictions = DeepFace.analyze(img_path, actions=['emotion'])[0]
        print(predictions)
        dominant_emotion = predictions['dominant_emotion']
        dominant_emotion_probability = predictions['emotion'][dominant_emotion]
        dominant_emotion_probability = math.ceil(dominant_emotion_probability)

        print("Dominant Emotion:", dominant_emotion)
        print("Probability:", dominant_emotion_probability)

        doc = {'emotion':dominant_emotion,'probability':dominant_emotion_probability} # 데이터 하나
        db.mood_collection.insert_one(doc)

        cv.imshow('frame', frame)
        key = cv.waitKey(1)

        if key == ord(' '):
            space_pressed = True
        if key == 27:  # ASCII code value of ESC
            esc_pressed = True

        if space_pressed and esc_pressed:
            cap.release()
            cv.destroyAllWindows()
            exit()

    except:
        continue

cap.release()
cv.destroyAllWindows()
