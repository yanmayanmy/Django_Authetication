from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signin(request):
    if request.method == "GET":
        return render(request, 'employee/login.html')
    user = None
    if request.method == "POST":
        e_id = request.POST['e_id']
        password = request.POST['password']
        user = authenticate(request, username=e_id, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'employee/login_success.html')
    else:
        print(user.is_staff)
        print(user.is_active)
        return render(request, 'employee/login.html', {'error_message': 'login failed'})