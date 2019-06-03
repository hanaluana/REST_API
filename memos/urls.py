from django.urls import path
from . import views

urlpatterns = [
    path('memos/', views.memo_list, name="list")
]