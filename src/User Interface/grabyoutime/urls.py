from django.urls import path
from . import views
import grabyoutime.views
urlpatterns = [
    path('/home.html',grabyoutime.views.home,name = 'home'),
]