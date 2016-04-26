from django.conf.urls import url, include
from .views import GenerateRecommendations, ratings_list


urlpatterns = [
    url(r'^generate/$', GenerateRecommendations),
    url(r'^rating_list/$', ratings_list, name='ratings'),
]



