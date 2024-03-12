from flask import Flask, render_template, request, jsonify
from joblib import load

app = Flask(__name__)

# Carga el modelo y el vectorizador desde el archivo .pkl
model = load('./model/naive_bayes_classifier.pkl')
vectorizer = load('./model/tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtiene el tweet del cuerpo de la solicitud
    data = request.get_json(force=True)
    tweet = data['tweet']

    print(f"Received tweet: {tweet}")

    # Vectoriza el tweet y hace la predicción
    tweet_vector = vectorizer.transform([tweet])
    prediction = model.predict(tweet_vector)

    print(f"Prediction: {prediction[0]}")

    # Mapea la predicción numérica a una cadena
    label_map = {0: 'Sadness', 1: 'Joy', 2: 'Love', 3: 'Anger', 4: 'Fear', 5: 'Surprise'}
    prediction_label = label_map[int(prediction[0])]

    # Devuelve la predicción como respuesta
    return jsonify({'prediction': prediction_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)