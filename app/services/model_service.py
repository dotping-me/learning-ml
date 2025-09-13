from os import path, getcwd
from utils.preprocessing import clean_text

import joblib

DIR_PATH = path.dirname(path.abspath(__file__))
MODEL_PATH = path.join(DIR_PATH, "../../models/sentiment_model.pkl")
VECTORIZER_PATH = path.join(DIR_PATH, "../../models/vectorizer.pkl")

class SentimentModel:
    def __init__(self):
        """ Loads trained ML model """

        self.model = joblib.load(MODEL_PATH)
        self.vectorizer = joblib.load(VECTORIZER_PATH)

    def predict(self, text: str) -> str:
        """ Predicts the sentiment ('positive', 'negative' or 'neutral') from a string """

        cleaned_text = clean_text(text)
        vectorized_text = self.vectorizer.transform([ cleaned_text ]) # Converts to numerical value
        prediction = self.model.predict(vectorized_text)

        return prediction[0]
    
sentiment_model = SentimentModel() # Instantiate model on import