from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import xgboost as xgb
import pickle
from numpy import array
import pickle
import tensorflow as tf
from numpy import array

def get_prediction(venue,team1,team2,toss_winner,toss_decision):
    tf.keras.backend.set_learning_phase(0)  # Ignore dropout at inference
    model = tf.keras.models.load_model('user\deep_model.h5')
    
    venues = {'Barabati Stadium': 0,
 'Brabourne Stadium': 1,
 'Buffalo Park': 2,
 'De Beers Diamond Oval': 3,
 'Dr DY Patil Sports Academy': 4,
 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium': 5,
 'Dubai International Cricket Stadium': 6,
 'Eden Gardens': 7,
 'Feroz Shah Kotla': 8,
 'Himachal Pradesh Cricket Association Stadium': 9,
 'Holkar Cricket Stadium': 10,
 'JSCA International Stadium Complex': 11,
 'Kingsmead': 12,
 'M.Chinnaswamy Stadium': 13,
 'MA Chidambaram Stadium, Chepauk': 14,
 'Maharashtra Cricket Association Stadium': 15,
 'New Wanderers Stadium': 16,
 'Newlands': 17,
 'Punjab Cricket Association IS Bindra Stadium, Mohali': 18,
 'Punjab Cricket Association Stadium, Mohali': 19,
 'Rajiv Gandhi International Stadium, Uppal': 20,
 'Sardar Patel Stadium, Motera': 21,
 'Sawai Mansingh Stadium': 22,
 'Sharjah Cricket Stadium': 23,
 'Sheikh Zayed Stadium': 24,
 "St George's Park": 25,
 'SuperSport Park': 26,
 'Wankhede Stadium': 27}
    venue = int(venue) - 1 
    teams = {'Chennai Super Kings': 0,
 'Delhi Capitals': 1,
 'Kings XI Punjab': 2,
 'Kolkata Knight Riders': 3,
 'Mumbai Indians': 4,
 'Rajasthan Royals': 5,
 'Royal Challengers Bangalore': 6,
 'Sunrisers Hyderabad': 7}
    team1 = int(team1) - 1
    team2 = int(team2) - 1
    toss_winner = int(toss_winner) -1
    toss_decisions = { 'bat':0, 'field':1}
    toss_decision = int(toss_decision) - 1 
    
    Xnew = array([[venue,team1,team2,toss_winner,toss_decision]])
    print(Xnew)
    predict = model.predict(Xnew)
    var =0
    for i in range(8):
        if(var<predict[0][i]):
            var = predict[0][i]
            index = i
    gamma = index     
    # max_v = np.where(predict == np.amax(predict))
    return gamma
def result1(venue,team1,team2,toss_winner,toss_decision):
    result_en =get_prediction(venue,team1,team2,toss_winner,toss_decision)
    teams = {0: 'Chennai Super Kings',
    1 :'Delhi Capitals',
    2: 'Kings XI Punjab',
    3: 'Kolkata Knight Riders',
    4:'Mumbai Indians',
    5: 'Rajasthan Royals',
    6: 'Royal Challengers Bangalore',
    7: 'Sunrisers Hyderabad'}
    result = teams[result_en]

    return result
def get_prediction1(venue,team1,team2,runs,wickets,over,runs_last_5,wickets_last_5):
    with open('user\\randomforest_runpredictor.pickle','rb') as f:
        model = pickle.load(f)
    # model = xgb.Booster()
    # model.load_model("xgboost.json")
    venues = {'Barabati Stadium': 0,
 'Brabourne Stadium': 1,
 'Buffalo Park': 2,
 'De Beers Diamond Oval': 3,
 'Dr DY Patil Sports Academy': 4,
 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium': 5,
 'Dubai International Cricket Stadium': 6,
 'Eden Gardens': 7,
 'Feroz Shah Kotla': 8,
 'Himachal Pradesh Cricket Association Stadium': 9,
 'Holkar Cricket Stadium': 10,
 'JSCA International Stadium Complex': 11,
 'Kingsmead': 12,
 'M Chinnaswamy Stadium': 13,
 'MA Chidambaram Stadium, Chepauk': 14,
 'Maharashtra Cricket Association Stadium': 15,
 'New Wanderers Stadium': 16,
 'Newlands': 17,
 'OUTsurance Oval': 18,
 'Punjab Cricket Association IS Bindra Stadium, Mohali': 19,
 'Punjab Cricket Association Stadium, Mohali': 20,
 'Rajiv Gandhi International Stadium, Uppal': 21,
 'Sardar Patel Stadium, Motera': 22,
 'Sawai Mansingh Stadium': 23,
 'Shaheed Veer Narayan Singh International Stadium': 24,
 'Sharjah Cricket Stadium': 25,
 'Sheikh Zayed Stadium': 26,
 "St George's Park": 27,
 'Subrata Roy Sahara Stadium': 28,
 'SuperSport Park': 29,
 'Wankhede Stadium': 30}
    venue = int(venue)-1
    teams = {'Chennai Super Kings': 0,
 'Delhi Daredevils': 1,
 'Kings XI Punjab': 2,
 'Kolkata Knight Riders': 3,
 'Mumbai Indians': 4,
 'Rajasthan Royals': 5,
 'Royal Challengers Bangalore': 6,
 'Sunrisers Hyderabad': 7}
    bat_team = int(team1)-1
    bowl_team = int(team2 )-1   
    Xnew = array([[venue,bat_team,bowl_team,runs,wickets,runs_last_5,wickets_last_5]])
    print(Xnew)
    predict = int(model.predict([[venue,bat_team,bowl_team,runs,wickets,over,runs_last_5,wickets_last_5]]))
       
    # max_v = np.where(predict == np.amax(predict))
    return predict
    
def result():
    venue = str(request.POST['venue'])
    team1 = str(request.POST['team1'])
    team2 = str(request.POST['team2'])
    runs = int(request.POST['runs'])
    wickets = int(request.POST['wickets'])
    overs = float(request.POST['overs'])
    runs_last_5 = int(request.POST['runs_last_5'])
    wickets_last_5 = int(request.POST['wickets_last_5'])
    # toss_win = str(request.POST['toss_win'])
    # toss_decision = str(request.POST['toss_decision'])
    result_en = int(get_prediction1(venue, team1, team2, runs, wickets, overs, runs_last_5, wickets_last_5))
    result2 = result(venue, team1, team2,toss_winner,toss_decision)
    return render(request, 'result.html', {'result':result_en,'result2':result2})


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    f_name = forms.CharField(label='First Name')
    l_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'username', 'email', 'password1', 'password2']


class PredictionInputForm(forms.Form):
    bat_team = forms.ChoiceField(
        label = "Which team is batting?",
        choices = ((1, 'Chennai Super Kings'), (2, 'Delhi Capitals'), (3, 'Kings XI Punjab'), (4, 'Kolkata Knight Riders'), (5, 'Mumbai Indians'), (6, 'Rajasthan Royals'), (7, 'Royal Challengers Bangalore'), (8, 'Sunrisers Hyderabad'), (9, 'Lucknow Super Giants'), (10, 'Gujarat Titans')),
    )
     
    ball_team = forms.ChoiceField(
        label = "Which team is bowling?",
        choices = ((1, 'Chennai Super Kings'), (2, 'Delhi Capitals'), (3, 'Kings XI Punjab'), (4, 'Kolkata Knight Riders'), (5, 'Mumbai Indians'), (6, 'Rajasthan Royals'), (7, 'Royal Challengers Bangalore'), (8, 'Sunrisers Hyderabad'), (9, 'Lucknow Super Giants'), (10, 'Gujarat Titans')),
    )
    venue = forms.ChoiceField(
        label='Venue',
        choices = ((1, 'Barabati Stadium'),
            (2, 'Brabourne Stadium'),
            (3, 'Buffalo Park'),
            (4, 'De Beers Diamond Oval'),
            (5, 'Dr DY Patil Sports Academy'),
            (6, 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium'),
            (7, 'Dubai International Cricket Stadium'),
            (8, 'Eden Gardens'),
            (9, 'Feroz Shah Kotla'),
            (10, 'Himachal Pradesh Cricket Association Stadium'),
            (11, 'Holkar Cricket Stadium'),
            (12, 'JSCA International Stadium Complex'),
            (13, 'Kingsmead'),
            (14, 'M Chinnaswamy Stadium'),
            (15, 'MA Chidambaram Stadium, Chepauk'),
            (16, 'Maharashtra Cricket Association Stadium'),
            (17, 'New Wanderers Stadium'),
            (18, 'Newlands'),
            (19, 'OUTsurance Oval'),
            (20, 'Punjab Cricket Association IS Bindra Stadium, Mohali'),
            (21, 'Punjab Cricket Association Stadium, Mohali'),
            (22, 'Rajiv Gandhi International Stadium, Uppal'),
            (23, 'Sardar Patel Stadium, Motera'),
            (24, 'Sawai Mansingh Stadium'),
            (25, 'Shaheed Veer Narayan Singh International Stadium'),
            (26, 'Sharjah Cricket Stadium'),
            (27, 'Sheikh Zayed Stadium'),
            (28, "St George's Park"),
            (29, 'Subrata Roy Sahara Stadium'),
            (30, 'SuperSport Park'),
            (31, 'Wankhede Stadium')
        )
    )
    toss_winner = forms.ChoiceField(
        label = "toss_winner",
        choices = ((1, 'Chennai Super Kings'), (2, 'Delhi Capitals'), (3, 'Kings XI Punjab'), (4, 'Kolkata Knight Riders'), (5, 'Mumbai Indians'), (6, 'Rajasthan Royals'), (7, 'Royal Challengers Bangalore'), (8, 'Sunrisers Hyderabad'), (9, 'Lucknow Super Giants'), (10, 'Gujarat Titans')),
    )
    toss_decision = forms.ChoiceField(
        label = "toss_winner",
        choices = ((1 , 'bat'),(2,'field')))
    runs = forms.IntegerField(label='Runs')
    wickets = forms.IntegerField(label='Wickets')
    overs = forms.FloatField(label='Overs')
    runs5 = forms.IntegerField(label='Runs in last 5 overs')
    wickets5 = forms.IntegerField(label='Wickets in last 5 overs')

    class Meta:
        model = User
        fields = ['venue','bat_team', 'ball_team', 'runs', 'wickets', 'overs', 'runs5', 'wickets5']

