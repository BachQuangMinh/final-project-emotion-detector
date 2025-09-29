from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    result = emotion_detector(text_to_analyze)

    if not result:
        return 'Invalid input! Try again'

    message = f'''
        For the given statement, the system response is 'anger': {result['anger']}, \
        'disgust': {result['disgust']}, 'fear': {result['fear']}, \
        'joy': {result['joy']} and 'sadness': {result['sadness']}. \
        The dominant emotion is {result['dominant_emotion']}
    '''

    return message

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="0.0.0.0", port=5000)
