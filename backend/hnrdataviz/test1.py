import json

with open('faces.json', 'r') as fo:
    times =json.load(fo)

times
print(len(times))

new_dict = {}
for faces_dict in times:
    for face_dict in faces_dict:
        # print(face_dict)
        # emotions_dict = face_dict['faceAttributes']

        emotions_vals = list(face_dict['faceAttributes']['emotion'].values())
        print(emotions_vals)
        # print(type(emotions_vals))


        face_id = face_dict['faceId']
        # new_dict[face_id] = emotions_dict
        new_dict[face_id] = emotions_vals


emotions = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']

columns_id = ['face_id', 'anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']


new_dict

import pprint
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame.from_dict(new_dict, orient = 'index')
df.reset_index(inplace=True)
df.columns = columns_id
df.head()

import plotly.express as px

barchart = px.bar(
    df,
    x='face_id',
    y='happiness'
)