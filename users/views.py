from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.


def signupView(request):
    form = UserCreationForm
    context = {
        'form': form
    }
    
    if request.method == 'GET':
        return render(request, 'users/signup.html', context)
    
    else: 
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1']
                )
                user.save()

                login(request, user)
            
                return redirect('tasks:all_tasks')
            
            except IntegrityError:
                context['error'] = str('user already exists')
                return render(request, 'users/signup.html', context)
            
            except Exception as e:
                context['error'] = str(e)
                return render(request, 'users/signup.html', context)
        
        else:
            context['error'] = str('Passwords do not match')
            return render(request, 'users/signup.html', context)
        
        
        
def signinView(request):
    form = AuthenticationForm
    context = {
        'form': form
    }
    
    if request.method == 'GET':
        return render(request, 'users/signin.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is not None:
            login(request, user)
            return redirect('tasks:all_tasks')
        else:
            context['error'] = str('Invalid credentials')
            return render(request, 'users/signin.html', context)


@login_required
def signoutView(request):
    logout(request)
    return redirect('home')