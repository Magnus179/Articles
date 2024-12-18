from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('one/<int:pk>',details,name='display_details')

]