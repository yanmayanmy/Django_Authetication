from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')
    user = None
    if request.method == "POST":
        member_id = request.POST['member_id']
        password = request.POST['password']
        user = authenticate(request, username=member_id, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'accounts/login_success.html')
    else:
        return render(request, 'accounts/login.html', {'error_message': 'login failed'})