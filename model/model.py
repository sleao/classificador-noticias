from joblib import load
import warnings
warnings.filterwarnings('ignore')

clf = load('model/modelo.joblib')
count_vect = load('model/count_vect.joblib')

def get_prediction(text):
    return (clf.predict(count_vect.transform([text]))[0])
