from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.post_view, name='post_list'),

]