from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('musics/', views.music_list, name="list"), 
    path('musics/<int:music_id>/', views.music_detail, name="detail"),
    
    path('docs/', get_swagger_view(title="API 문서")),
    
]

