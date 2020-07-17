from joblib import load

clf = load('modelo.joblib')
count_vect = load('count_vect.joblib')

def get_prediction(text):
    return (clf.predict(count_vect.transform([text]))[0])
