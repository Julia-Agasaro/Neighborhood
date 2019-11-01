from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
