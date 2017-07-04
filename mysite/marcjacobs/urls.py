
from django.conf.urls import url
from . import views

app_name = "marcjacobs"
urlpatterns = [
    url(r'^$', views.display_data, name="home"),
    url(r'^home/$', views.ListProductView.as_view(), name="products-list"),
    url(r'^home/product/(?P<pk>[0-9]+)', views.ProductDetailView.as_view(),
        name="product-detail")
]
