from django.shortcuts import render
from  django.http import HttpResponse
from django.contrib import messages

def home(request ):
    return render(request,"authentication/index.html")
def signup(request):
    # username = request.POST.get('username')
    if request.method == "POST":
        username =request.POST['username']
        fname=request.POST['first']
        lname = request.POST['last']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

    myuser =User.objects.create(username,email,pass1)
    myuser_first_name= fname
    myuser_last_name =lname
    
    myuser.save()
    
    messages.success(request,"Your Account has been succesfully created")

    return render(request,"authentication/signup.html")
def signin(request):
    return render(request,"authentication/signin.html")
def signout(request):
 pass