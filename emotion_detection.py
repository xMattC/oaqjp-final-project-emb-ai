import requests
import json


def emotion_detector(text_to_analyse):
    """ Emotion predict function using the Watson NLP Library
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_text = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=input_text, headers=header)

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions

    print(type(response.text))
    formatted_response = json.loads(response.text)
    print(type(formatted_response))

    # # Parse the response from the API
    # formatted_response = json.loads(response.text)

    # # If the response status code is 200, extract the label and score from the response
    # if response.status_code == 200:
    #     label = formatted_response['documentSentiment']['label']
    #     score = formatted_response['documentSentiment']['score']

    # # If the response status code is 500, set label and score to None
    # elif response.status_code == 500:
    #     label = None
    #     score = None

    # Return the label and score in a dictionary
    return
    # return {'label': label, 'score': score}


emotion_detector("“I love this new technology.”")