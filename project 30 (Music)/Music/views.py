from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Music,MyPlaylist
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('userdashboard')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('userdashboard')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['Name']
        Email=request.POST['Email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'registration.html')
def user_dash(request):
    users=User.objects.all()
    musics=Music.objects.all()
    Mymusics=MyPlaylist.objects.filter(user=request.user)
    return render(request,'dashboard.html',{'users':users,'musics':musics,'Mymusics':Mymusics})
def add_music(request):
    if request.method=="POST" and request.FILES.get('file'):
        title=request.POST['music_artist']
        artist=request.POST['music_artist']
        genre=request.POST['music_genre']
        file=request.FILES['file']
        data=Music.objects.create(user=request.user,title=title,artist=artist,genre=genre,file=file)
        data.save()
        return redirect('userdashboard')
    return redirect('userdashboard')
def search_music(request):
    if request.method=="POST":
        data=request.POST['search']
        search = Music.objects.filter(title=data)
        return render(request,'search.html',{ 'search':search})
def add_playlist(request,pk):
    fav=Music.objects.get(id=pk)
    data=MyPlaylist.objects.filter(user=request.user,fav=fav)
    if data:
        return redirect('userdashboard')
    else:
        data=MyPlaylist.objects.create(user=request.user,fav=fav)
        data.save()
    return redirect('userdashboard')
@login_required(login_url='login')
def remove_play(request,pk):
    data=MyPlaylist.objects.get(user=request.user,id=pk)
    data.delete()
    return redirect('userdashboard')