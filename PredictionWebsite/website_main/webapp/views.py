from calendar import month
from django.shortcuts import render
from django.http import HttpResponse
import pandas
from datetime import datetime 



def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'webapp/home2/index.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'webapp/info/info.html', context)

def webteam(request):
    context = {
        'title': 'Web Team'
    }
    return render(request, 'webapp/webteam/webteam.html', context)

def sports(request):
    df1 = pandas.read_csv('webapp/data/cricket/cricket_schedule.csv')
    cric_schedule = []
    
    # # df1['date'] = df1['date'].apply(lambda x: datetime.strptime(x, '%d, %Y'))
    dt1 = datetime.now()
    for i in range(70):
        strif = str(df1.date[i])
        date = strif.split(',')
        date = date[0].split(' ')
        # print(date)
        month = {
            'March' : 3,
            'April' : 4,
            'May' : 5,
        }
        

        month1 = month[date[0]]
    #     # print(month1)   
         
        # print(type(date[1])  )
        if( dt1.day == int(date[1]) and dt1.month == month1):
            cric_schedule.append(
                {
                    'match_number': i+1,
                    'team1': df1.team1[i],
                    'team2': df1.team2[i],
                    'venue': df1.venue[i],
                    'date': df1.date[i],
                    'time': df1.time[i],
                }
            )

    df2 = pandas.read_csv('webapp/data/football/epl-2021-GMTStandardTime.csv')
    football_schedule = []
    date = []
    time = []
    for i in range(len(df2)):
        date.append(str(df2['Date'][i]).split()[0])
        time.append(str(df2['Date'][i]).split()[1])
        football_schedule.append(
            {
                'match_number': df2['Match Number'][i],
                'round': df2['Round Number'][i],
                'team1': df2['Home Team'][i],
                'team2': df2['Away Team'][i],
                'venue': df2['Location'][i],
                'date': date[i],
                'time': time[i],
                'view': 'View',
            }
        )
    context = {
        'title': 'Sports',
        'cric_schedule': cric_schedule,
        'football_schedule': football_schedule,
    }
    return render(request, 'webapp/sports/index.html', context)
