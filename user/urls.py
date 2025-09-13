from django.urls import path,include
from .views import RegisterView,SignInView,SignOutView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('sign_in/',SignInView.as_view(),name='signin'),
    path('sign_out/',SignOutView.as_view(),name='signout')
]