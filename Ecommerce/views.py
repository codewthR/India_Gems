from django.shortcuts import render
from django.http import HttpResponse
from Details_all.models import state_about

def disp(request):
    if request.method == "GET":
        all_data = state_about.objects.all()
        # one = state_about.objects.get(id=32)
        # two = state_about.objects.get(id=5)
        context={
            'all_data':all_data,
            # 'one' : one,
            # 'two':two,
        }
    return render(request, 'index.html', context )