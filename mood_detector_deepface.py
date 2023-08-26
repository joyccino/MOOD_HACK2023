import cv2 as cv
from deepface import DeepFace
import math
import time
cap = cv.VideoCapture(0)

space_pressed = False
esc_pressed = False

textFile = open("emotionCodes.txt","w")

while True:
    ret, frame = cap.read()

    img_path = 'output/capture.jpg'
    cv.imwrite(img_path, frame)

    try:
        predictions = DeepFace.analyze(img_path, actions=['emotion'])[0]
        #print(predictions)
        dominant_emotion = predictions['dominant_emotion']
        dominant_emotion_probability = predictions['emotion'][dominant_emotion]
        dominant_emotion_probability = math.ceil(dominant_emotion_probability)

        # print("Dominant Emotion:", dominant_emotion)
        # print("Probability:", dominant_emotion_probability)

        cv.imshow('frame', frame)
        key = cv.waitKey(1)

        if key == ord(' '):
            space_pressed = True
        if key == 27:  # ASCII code value of ESC
            esc_pressed = True

        emotion_code = 0
        if (dominant_emotion == "happy") :
            emotion_code = 1
        elif (dominant_emotion == "sad" or dominant_emotion == "angry"):
            emotion_code = 2
        elif (dominant_emotion == "neutral") :
            emotion_code = 0
        print(emotion_code)
        textFile.write(str(emotion_code) + '\n')
        textFile.flush()
        time.sleep(2)


        if space_pressed and esc_pressed:
            cap.release()
            cv.destroyAllWindows()
            exit()

    except:
        break
        



cap.release()
cv.destroyAllWindows()
textFile.close()
