# Project
App that analyzes videos using Azure Face API to give info about emotions of video participants during the meeting.

## Stack & Libraries
- Flask
- Opencv 4

## APIs
- Azure Face API

## Setup
Python 3 is required to run this app.
1. Clone repo
2. At project root run: `pip install -r requirements.txt`
3. Set up environment variables (refer to `analyzer.py`)
   - `AZURE_KEY_1` refers to the azure secret key
   - Windows [example](https://www.youtube.com/watch?v=IolxqkL7cD8)
4. Use Postman or equivalent to call the api.