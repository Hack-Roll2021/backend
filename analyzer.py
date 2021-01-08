import os
import cv2
import requests
import pprint
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

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
    is_first_frame = True
    first_frame_faces = []
    result = {}
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
            if is_first_frame:
                response = requests.post(endpoint, headers=headers, params=params, data=buf.tobytes())
                response.raise_for_status()
                output = response.json()
                first_frame_faces = list(map(lambda x: x["faceId"], output))
                for x in first_frame_faces:
                    curr_result = {}
                    for y in output:
                        if y["faceId"] == x:
                            curr_result = y
                            break
                    result[x] = []
                    result[x].append(curr_result["faceAttributes"]["emotion"])
                is_first_frame = False
            else:
                response = requests.post(endpoint, headers=headers, params=params, data=buf.tobytes())
                response.raise_for_status()
                output = response.json()
                curr_frame_faces = list(map(lambda x: x["faceId"], output))
                face_client = FaceClient("https://instance-01.cognitiveservices.azure.com/", CognitiveServicesCredentials(AZURE_KEY))
                similar_faces = False
                for x in first_frame_faces:
                    similar_faces = face_client.face.find_similar(face_id=x, face_ids=curr_frame_faces)
                    confidence = 0
                    face_id = "null"
                    for face in similar_faces:
                        if face.confidence > confidence:
                            face_id = face.face_id
                    if face_id != "null":
                        for y in output:
                            if y["faceId"] == face_id:
                                result[x].append(y["faceAttributes"]["emotion"])
                                break
            
            # discard frames without faces
            if len(output) != 0:
                res.append(output)
        i += 1

    print("")
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(result)
    cap.release()
    cv2.destroyAllWindows()
    return result

