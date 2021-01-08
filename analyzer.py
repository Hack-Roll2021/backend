import os
import cv2
import requests

AZURE_KEY = os.getenv("AZURE_KEY_1")

endpoint = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/detect"

# API Call Config
headers = {'Ocp-Apim-Subscription-Key': AZURE_KEY, 'Content-Type': 'application/octet-stream'}
params = {
    'returnFaceAttributes': 'emotion',
    'returnFaceId': 'true',
    'detectionModel': 'detection_01'
}

def analyze_video(url):
    # Opens the Video file
    cap = cv2.VideoCapture(url)
    fps = cap.get(cv2.CAP_PROP_FPS)
    # store the emotions of people in the video
    res = []
    i = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # process frames every 4 seconds
        # make sure we don't bust azure's free tier
        if i % (4*fps) == 0:
            # to write frames to disk
            # cv2.imwrite('test_' + str(i) + '.jpg', frame)
            ret, buf = cv2.imencode('.jpg', frame)
            # Azure API Call
            response = requests.post(endpoint, headers=headers, params=params, data=buf.tobytes())
            response.raise_for_status()
            output = response.json()
            # discard frames without faces
            if len(output) != 0:
                res.append(output)
        i += 1

    cap.release()
    cv2.destroyAllWindows()
    return res


def analyze_emotions(data):
    # TODO
    pass
