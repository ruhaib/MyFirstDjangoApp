
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.display_data),
    url(r'^load-scrappy', views.load_scrappy_data),
]
