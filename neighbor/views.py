from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from . forms import *
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    hoods = Hood.objects.all()

    return render(request,'home.html',locals())
    
@login_required(login_url='/accounts/login/')
def hood(request,hood_id):
    current_user = request.user
    hood_name = current_user.hood
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    businesses = Business.get_business(hood_id)
    posts = Post.get_post(hood_id)

    return render(request,'hood.html',locals())
@login_required(login_url='/accounts/login/')
def profile(request, username):

    profile = User.objects.get(username=username)
    print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        pass
    user = request.user
    profile = User.objects.get(username=username)
    title = f'@{profile.username} '

    return render(request, 'profile.html', locals()) 


   
@login_required(login_url='/accounts/login/')
def upload_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            hood.owner= current_user
            upload.save()
            return redirect('home')
    else:
        form = HoodForm()
    return render(request, 'upload_hood.html', locals())

@login_required(login_url='/accounts/login/')
def edit(request):
    current_user = request.user
    # print(f'profile {current_user.profile}')
    # user = Profile.objects.get(user=current_user)
   

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile.html')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', locals()) 
@login_required(login_url='/accounts/login')
def join(request,hood_id):
    hood = Hood.objects.get(id=hood_id)
    current_user = request.user
    current_user.hood = hood
    current_user.save()
    return redirect('hood',hood_id)


@login_required(login_url='/accounts/login')
def leave(request,hood_id):
    current_user = request.user
    current_user.profile.hood = None
    current_user.profile.save()
    return redirect('home')

