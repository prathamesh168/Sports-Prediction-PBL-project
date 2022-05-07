import pickle
import tensorflow as tf
from numpy import array

def get_prediction1(venue,team1,team2,toss_winner,toss_decision):
    tf.keras.backend.set_learning_phase(0)  # Ignore dropout at inference
    model = tf.keras.models.load_model('deep_model.h5')
    label = pickle.load('Label_Encoder.pki','rb')
    venue = label.transform(venue)
    teams = {0: 'Chennai Super Kings',
    1 :'Delhi Capitals',
    2: 'Kings XI Punjab',
    3: 'Kolkata Knight Riders',
    4:'Mumbai Indians',
    5: 'Rajasthan Royals',
    6: 'Royal Challengers Bangalore',
    7: 'Sunrisers Hyderabad'}
    team1 = teams[team1]
    team2 = teams[team2]
    toss_winner = teams[toss_winner]
    toss_decisions = {0: 'bat', 1: 'field'}
    toss_decision = toss_decisions[toss_decision]
    Xnew = array([[venue,team1,team2,toss_winner,toss_decision]])
    predict = model.predict(Xnew)
