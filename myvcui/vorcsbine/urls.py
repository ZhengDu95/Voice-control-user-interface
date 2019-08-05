from django.urls import path

from .views import *

urlpatterns = [
    # Index
    path('index', index),
    path('back_index', back_index),

    # Sign In
    path('signIn', signIn),
    path('signIn_process', signIn_process),

    # Sign Up
    path('signUp', signUp),
    path('signUp_process', signUp_process),

    # Text chat page
    path('textChat', textChat),

    # Text chat page component
    path('textChat_component', textChat_component),

    # Voice chat page
    path('voiceChat', voiceChat),

    # Voice chat page component
    path('voiceChat_component', voiceChat_component),

]
