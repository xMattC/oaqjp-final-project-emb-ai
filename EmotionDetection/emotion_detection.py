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


if __name__ == "__main__":
    emotion_detector("“I hate working long hours.”")