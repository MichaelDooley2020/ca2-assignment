from django.urls import path
from shopapp import views 
from .views import SignUpView

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
]
