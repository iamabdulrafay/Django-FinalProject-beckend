# urls.py

from django.urls import path
from .views import SignupSerializerViewSets, LoginSerializerViewSets

urlpatterns = [
    path('signup/', SignupSerializerViewSets.as_view(), name='signup'),
    path('login/', LoginSerializerViewSets.as_view(), name='login'),
]
