from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cybersecurity/', views.cybersecurity, name='cybersecurity'),
    path('cybersport/', views.cybersport, name='cybersport'),
    path('design/', views.design, name='design'),
    path('information-technology/', views.information_technology, name='information_technology'),
    path('movie-and-video/', views.movie_and_video, name='movie_and_video'),
    path('olimp/', views.olimp, name='olimp'),
    path('robots/', views.robots, name='robots'),
    path('solutions/', views.solutions, name='solutions'),
]
