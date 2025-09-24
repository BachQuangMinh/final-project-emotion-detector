import requests

def emotion_detector(text_to_analyze):
    ''' This function takes the input text and applies sentiment analysis
        over it using the deployed model on IBM Cloud. The output returns
        the sentiment label and its confidence score.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        formatted_response = response.json()
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotion_dict.items(), key=lambda item: item[1])
        label = max_emotion[0]
        score = max_emotion[1]
        emotion_dict['dominant_emotion'] = label

    if response.status_code == 500:
        emotion_dict = None
    
    return emotion_dict