import cv2 as cv
# Importing the libraries
from deepface import DeepFace
import math

# Open you default camera
cap = cv.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  img_path = 'output/capture.jpg'
  
  cv.imwrite(img_path, frame)

  try:
    predictions = DeepFace.analyze(img_path, actions = ['emotion'])
  
  except:
    continue

  print(predictions)
  
  cv.imshow('frame', frame)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
  cv.imwrite(img_path, frame)

  predictions = DeepFace.analyze(img_path, actions = ['emotion'])[0]

 # Extract dominant emotion and its probability
  dominant_emotion = predictions['dominant_emotion']
  dominant_emotion_probability = predictions['emotion'][dominant_emotion]
  dominant_emotion_probability = math.ceil(dominant_emotion_probability)

  # Print the dominant emotion and its probability
  print("Dominant Emotion:", dominant_emotion)
  print("Probability:", dominant_emotion_probability)
  
  cv.imshow('frame', frame)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
  
cap.release()
cv.destroyAllWindows()