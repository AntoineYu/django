from django.urls import path
from .views import RegistrerView,LoginView
from . import views

urlpatterns = [
    path(r'registrer/',RegistrerView.as_view(), name='registrer'),
    path(r'',LoginView.as_view(),name='login'),
    path(r'user/',views.get),
    path(r'ajax/',views.ajax,name="ajax"),
    path(r'logout/',views.logout,name="logout")
]