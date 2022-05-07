from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, PredictionInputForm
from .forms import get_prediction1,result1

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            f_name = form.cleaned_data.get('f_name')
            l_name = form.cleaned_data.get('l_name')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'user/register.html', context)

def prediction_input(request):
    if request.method == 'POST':
        form = PredictionInputForm(request.POST)
        if form.is_valid():
            bat_team = form.cleaned_data.get('bat_team')
            ball_team = form.cleaned_data.get('ball_team')
            venue = form.cleaned_data.get('venue')
            runs = form.cleaned_data.get('runs')
            wickets = form.cleaned_data.get('wickets')
            overs = form.cleaned_data.get('overs')
            runs5 = form.cleaned_data.get('runs5')
            wickets5 = form.cleaned_data.get('wickets5')
            toss_winner = form.cleaned_data.get('toss_winner')
            toss_decision = form.cleaned_data.get('toss_decision')
            result_en = int(get_prediction1(venue, bat_team, ball_team, runs, wickets, overs, runs5, wickets5))
            result2 = result1(venue, bat_team, ball_team,toss_winner,toss_decision)
            return render(request, 'user/match_prediction_form.html', {'result2':result2,'result': result_en,'venue':venue,'team1' :bat_team, 'team2':ball_team, 'runs':runs,'wickets': wickets,'overs' :overs, 'runs5':runs5, 'wickets5':wickets5})

    else:
        form = PredictionInputForm()

    context = {
        'form': form,
    }

    return render(request, 'user/match_prediction_form.html', context)
