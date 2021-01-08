from flask import Flask, jsonify, request
from flask_cors import CORS
from analyzer import analyze_video
from hnrdataviz.visualizer import visualizer

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def welcome():
    msg = "Welcome to Emotional Intelligenze server!"
    return msg;

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # test_url = "https://media.istockphoto.com/videos/group-of-six-friends-saying-cheers-over-video-chat-video-id1221689160"
    data = request.get_json()
    result = analyze_video(data['url'])
    dict_jsons = visualizer(result)
    return dict_jsons

