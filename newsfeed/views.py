import mailbox
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Newsfeed
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Users
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def signup(request):

    if request.method == 'POST':
        names = request.POST['names']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            myuser = User.objects.create_user(names,email,password1)
            myuser.name = names
            myuser.email = email

            myuser.save()

            messages.success(request, "Account created successfully!.")

            return redirect('/login')
        else:
            return HttpResponse("<p>passwords do not match </p>")

    return render(request, 'newsfeed/signup.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects(email,password)
        myuser.email = email



        if email == myuser.object(email) and password == myuser.object(password):
            return render(request, '/newsfeed')

        


    return render(request, 'newsfeed/login.html')



def index(request):
    newsfeed = Newsfeed.objects.all()
    return render(request, 'newsfeed/index.html',{
        'newsfeed' : newsfeed
    })


def detail(request, feed_slug):
    try:
        selected_news = Newsfeed.objects.get(slug=feed_slug)
        return render(request, 'newsfeed/news-detail.html', {
            'meetup_found' : True,
            'news_title' : selected_news.title,
            'news_detail' : selected_news.details,
            'news_image' : selected_news.image
        })
    except Exception as axc:
        return render(request, 'newsfeed/news-detail.html',{
            'meetup_found' : False
        })





