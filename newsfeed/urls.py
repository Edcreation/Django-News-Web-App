from unicodedata import name
from django.urls import URLPattern, path
from . import views 

urlpatterns = [
    path('newsfeed/', views.index , name= 'all-newsfeeds'),
    path('newsfeed/<slug:feed_slug>', views.detail , name="news-detail"  ),
    path('signup', views.signup, name='signup'),
    path('login' , views.login, name='login')
]