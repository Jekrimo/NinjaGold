from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    return render(request, 'ninjaGold/index.html')

def create(request):
    time = datetime.now()

    #   for use in resets.
    # request.session['userGold'] = 0
    # request.session['activity'] = []

    if request.POST['place'] == "Cave":
        request.session['cave'] = random.randrange(5, 10)
        request.session['userGold'] += request.session['cave']
        activity = {'activity' : "Earned {} golds from the cave! {}".format(request.session['cave'], time), 'class' : 'win'}
        request.session['activity'].append(activity)
        print (request.session['cave'])
    elif request.POST['place'] == "Farm":
        request.session['farm'] = random.randrange(10, 20)
        request.session['userGold'] += request.session['farm']
        activity = {'activity' : "Earned {} golds from the farm! {}".format(request.session['farm'], time), 'class' : 'win'}
        request.session['activity'].append(activity)
        print (request.session['farm'])
    elif request.POST['place'] == "House":
        request.session['house'] = random.randrange(2, 5)
        request.session['userGold'] += request.session['house']
        activity = {'activity' : "Earned {} golds from the house! {}".format(request.session['house'], time), 'class' : 'win'}
        request.session['activity'].append(activity)
        print (request.session['house'])
    elif request.POST['place'] == "Casino":
        request.session['casino'] = random.randrange(-50, 50)
        if request.session['casino'] < 0:
            request.session['userGold'] += request.session['casino']
            activity = {'activity' : "Lost {} golds from the casino! {}".format(request.session['casino'], time), 'class' : 'lost'}
            request.session['activity'].append(activity)
        else:
            request.session['userGold'] += request.session['casino']
            activity = {'activity' : "Earned {} golds from the casino! {}".format(request.session['casino'], time), 'class' : 'win'}
            request.session['activity'].append(activity)
        print (request.session['casino'])
    return redirect('/')

def reset(request):
    if request.POST['reset'] == 'reset':
        request.session.clear()
        return redirect('/')
