from django.shortcuts import render, redirect, Http404, reverse
from users.forms import LoginForm, UserForm, RegisterForm, UserImageForm, ProfileImageForm
from django.contrib.auth import authenticate, login, logout
from users.email import send_register_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            send_register_mail(user)

            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        form = LoginForm()
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            raise Http404('Username or password not provided!')
        print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request,'nume utilizator sau parola incorecta')
            print('###################')
        else:
            login(request, user)

            return redirect(reverse('users:profile'))

    return render(request, 'users/login.html', {'form': form, 'error':error})


def logout_user(request):
    logout(request)
    return redirect('/')


def upload_view(request):
    if request.method == 'GET':
        form = UserImageForm()
    else:
        form = UserImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'users/file_uploaded.html')

    return render(request, 'users/upload.html', {
        'form': form
    })


@login_required
def profile_view(request):
   
    # print(profile_form)
    if request.method == 'GET':
        profile_form = UserForm(initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'username':request.user.username,
            'email':request.user.email
        })
        # print(profile_form)
        form = ProfileImageForm()     
    else:
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form,
        'profile_form':profile_form
    })

def profile_update(request):
    profile_form = UserForm()
    if request.method == 'GET':
        form = ProfileImageForm()
    else:
        profile_update_form = UserForm(request.POST, instance=request.user)
        if profile_update_form.is_valid():
            profile_update_form.save()          
            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form,
        'profile_form':profile_form
    })


