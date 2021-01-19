from django.shortcuts import render, HttpResponse, redirect
from FormApp1.form import LoginForm
from django.contrib.auth import login, logout, authenticate

def login_handler(request):

    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            print("Login cleaned data = ", lform.cleaned_data)
            username = lform.cleaned_data["login_email"]
            password = lform.cleaned_data["login_password"]
            login_user_obj = authenticate(username=username, password=password)
            if login_user_obj is not None:
                login(request, login_user_obj)
                request.session['user'] = username
                # return render(request, 'Dashboard.html')
                print("Session = ",request.session['user'])
                return redirect('/form/dash')
            else:
                print("User not found in database")    

    login_obj = LoginForm()
    return render(request, 'Login.html', {'login':login_obj})

def dash_handler(request):
    try:
        x = request.session['user']
        if x != None:
            print("Your Session: ", request.session.get('user'))
            return render(request, 'Dashboard.html') 
    except:
        return render(request, 'Error.html')  

def logout_handler(request):
    del request.session['user']
    logout(request)
    return redirect("/form/login")
