from django.urls import path
from . import views 

app_name='posts'

urlpatterns = [
    path('destacados/',views.Posts_Destacados ,name='Posts_Destacados'),
    path('Alta/',views.AltaPost.as_view() ,name='alta_post'),
]
