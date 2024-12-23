from django.urls import path
from .views import *

app_name='myapp'

urlpatterns = [
    path('insert/',insert,name='insert'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('viewdata/',viewdata,name='viewdata'),
    path('',home,name='home')
]
