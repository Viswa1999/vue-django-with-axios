from django.urls import path
from . import views
from . views import PostsView

urlpatterns = [
    path('',views.index,name='index')
]