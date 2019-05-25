from django.urls import path
from .views import RegistrerView,LoginView,UserView,TryView

urlpatterns = [
    path(r'registrer/',RegistrerView.as_view(), name='registrer'),
    path(r'',LoginView.as_view(),name='login'),
    path(r'user/',UserView.as_view()),
    path(r'ajax/',UserView.ajax),
    path(r'comments_upload/', TryView.as_view(), name='comments_upload'),
]