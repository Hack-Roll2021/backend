# Project
App that analyzes emotions of video conference participants using Azure Face API. 

## Python Libraries used
Python 3 is required for this app.
- Flask
- Opencv
- Pandas
- Numpy

## APIs used
- [Azure Face API](https://azure.microsoft.com/en-us/services/cognitive-services/face/). Note that an API key needs to be generated to use this app.
    - Face detection
    - Face similarity

## Setup
1. Clone repo and `cd backend`
2. Set up a [python virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
2. At project root run: `pip install -r requirements.txt`
3. Set up environment variables (refer to `analyzer.py`)
   - `AZURE_KEY_1` refers to the azure secret key
   - Windows [example](https://www.youtube.com/watch?v=IolxqkL7cD8)
4. `flask run`

Call APIs exposed easily through the frontend website.