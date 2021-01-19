# Django_Form

<h1>Login and logout form using django</h1>

<div>
  <h2>Check the installed list of apps</h2>
  In order to create form in django we need to check if "django.contrib.session" is installed in the list of installed apps of django or not.
</div>

<div>
  <h2>What is Session?</h2>
  <p>
    Without session, any usercan easily access the dashboard without logging in. Session is storage place of user information in server side. 
    It helps the server to identify the user and show the user's respective content. Otherwise, server would not be able to identify the user and 
    user would have to provide email and password or varify him/her every time s/he needd to interact with the server. 
  </p>
  <p>
    In order to solve the problem, when the user first time logs in then the server will crete a session and sends a cookie to the client.
    Such cookie will contain the session ID of the user so that user wouldn't have to verify himself/herself each and every time s/he interacts 
    with the server. i.e. When session is created and cookie is stored in the client side then the cookie having session ID will work as the 
    identity card of the user to interact with the server.The server will receive the session ID and checks if the session of the given user exist or not.
    If it exist, then the user can access the dashboard after logging in otherwise not.
  </p>
  
  <b>How session is used?</b>
  <p>
    When the user loggs in then, the session of the user is created and the user can access the dashboard if s/he is a valid user or if s/he has been registered.
    E.g: Setting the session: request.session['user'] = 'value'.
    Now before user can access the dashboard, the system will check if the session of the user is created or not.
    E.g: def dash_handler(request):
   </p> 
   
    try:
        x = request.session['user']
        if x != None:
            print("Your Session: ", request.session.get('user'))
            return render(request, 'Dashboard.html') 
    except:
        return render(request, 'Error.html') 
        
     When user loggs out then the session of the user is deleted.
     E.g: del request.session['user']
</div>
