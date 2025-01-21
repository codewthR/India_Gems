# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
# # Create your views here.





# def logging(request):
#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = User.objects.get(username = username)
#         short = user.get_full_name()
#         uname = user.get_username()
#         print(f"{short},{uname}")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             context={
#                     'short':short,
#                     'uname':uname,
#             }
#             return redirect('home')
#         else:
#             messages.error(request, "Invalid Credentials 🚫!")
#     return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth import password_validation

# Create your views here.

# def logging(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")
        
#         # First, authenticate the user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             # Successful login, proceed to login and redirect
#             login(request, user)
#             messages.success(request, f"Welcome {user.get_full_name()}!")
#             return redirect('home')
#         else:
#             # Invalid credentials
#             messages.error(request, "Invalid Credentials 🚫!")
    
#     return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get ('first_name')
        last_name = request.POST.get ('last_name')
        user = request.POST.get ('username')
        password = request.POST.get ('password')

        print(f"{first_name} {last_name}  {user}  {password}")

        user = User.objects.create(
            first_name = first_name ,
            last_name = last_name ,
            username = user ,
        )
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.INFO, "Account Created Successfully 😊")
        # return redirect()
    return render(request, 'signup.html')


# def forgot_password(request):
#     if request.method == 'POST':
#         pass



def logging(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password= password)

        if user is not None:
            person = User.objects.get(username = username)
            short = person.get_full_name()
            uname = person.get_username()
            context ={
                'short' :short,
                'uname' :uname,
            }

        if user is None:
            messages.error(request, "Invalid Credentials 🚫!")
        else :
            login(request, user)
            return render(request, 'index.html', context)
        
    return render(request, 'loginn.html')


def logout_page(request):
    logout(request)
    return redirect('home')


# def forgotpass(request):
#     if request.method == 'POST':
#         username = request.POST.get ('username')
#         new_password = request.POST.get ('new-password')
#         new_pas = request.POST.get ('new-pass')


#         print(f"{username} {new_password} {new_pas}")


#         user = authenticate(username=username)

#         if user is not None :
#             User.set_password(new_password)

#             messages.INFO("Your password updated sucessfully ...")

#             return redirect('login')

#         else :
#             messages.INFO("Incorrect Username ")
#     return render(request, 'forgot-password.html')


