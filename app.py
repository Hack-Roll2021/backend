from flask import Flask, jsonify, request
from flask_cors import CORS
from analyzer import analyze_video
app = Flask(__name__)
cors = CORS(app)
import json
import cv2

@app.route('/')
def welcome():
    msg = "Welcome to Emotional Intelligenze server!"
    return msg;

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # test_url = "https://media.istockphoto.com/videos/group-of-six-friends-saying-cheers-over-video-chat-video-id1221689160"
    data = request.get_json()
    result = analyze_video(data['url'])

@app.route('/api/image', methods=['GET'])
def send_file(): 
    data = request.get_json()
    result = analyze_video(data["url"])
    # return send_file('data\pic.jpg')
    img = cv2.imread('data\pic.jpg')
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', img)
    return img_encoded.tostring()
    

