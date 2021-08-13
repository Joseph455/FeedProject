from django.urls import path
from FeedApp.views import  index, reports, post

app_name = 'FeedApp'

urlpatterns = [
    path('', index, name='index'),
    path('reports/', reports, name='reports'),
]
