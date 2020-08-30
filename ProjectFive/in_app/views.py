from django.shortcuts import render
from in_app.forms import UserForm,UserProfileForm
# Create your views here.

def index(request):
    return render(request,'in_app/base.html')

def other(request):
    total=0
    if request.method=='POST':
        value01=request.POST['value01']
        value02=request.POST['value02']
        total=int(value01)+int(value02)

    return render(request,'in_app/other.html',{'total':str(total)})

def register(request):

    registered=False

    if request.method=='POST':

        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pics' in request.FILES:
                profile.profile_pics=request.FILES['profile_pics']

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'in_app/register.html',{'user_form':user_form,
                                                    'profile_form':profile_form,
                                                    'registered':registered})


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


def log_in(request):

    if request.method=='POST':

        username=request.POST.get('Username')
        password=request.POST.get('Password')

        user=authenticate(username=username,password=password)

        if user:

            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('in_app:special'))

            else:
                return HttpResponse("Account isn't activated")
        else:
            print('Someone tried to login failed!')
            print(f"username:{username} and password:{password}")
            return HttpResponse('Invalid login details supplied')

    else:
        return render(request,'in_app/log_in.html')


def special(request):
    return render(request,'in_app/special.html')

def goodbye(request):
    return render(request,'in_app/goodbye.html')

@login_required
def log_out(request):

    logout(request)
    return HttpResponseRedirect(reverse('in_app:goodbye'))
