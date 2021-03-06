from django.conf.urls import url
from . import views

app_name = "authentication"
urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(), name="signup"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout")
]
