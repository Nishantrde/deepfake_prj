from django.urls import path
from .views import *

urlpatterns = [
    path('handel/', HandelFileUpload.as_view()),
    path('pp/', HandelFaceFileUpload.as_view()),
    path('', index)
]
