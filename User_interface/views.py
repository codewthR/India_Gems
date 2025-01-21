from django.shortcuts import render
from Details_all.models import state_about, city_detail

# Create your views here.


def city_all(request,state_names):
    print(type(state_names))
    if request.method == 'GET':
        city = city_detail.objects.filter(state_name__state_name=state_names)
        context = {
            'city' : city
        }
    return render(request, 'explore.html', context)
