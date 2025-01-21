from django.shortcuts import render
from Details_all.models import state_about
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def data_sending(request):
    if request.method == "POST":
        state_name = request.POST.get("state_name")
        state_images = request.FILES.get("state_images")
        print(f"{  state_name } { state_images }")

        state_about.objects.create(
            state_pics=state_images,
            state_name=state_name,
        )
        return HttpResponse("added successfully")
    return render (request, 'datasend.html')



def data_getting(request):
    if request.method == "GET":
        all_data = state_about.objects.all()
        context={
            'all_data':all_data
        }
    return render(request, 'index.html' ,context)