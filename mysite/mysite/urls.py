
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^store/', include('super_store.urls')),
    url(r'^user/', include('authentication.urls')),
    url(r'^$', RedirectView.as_view(url='/store/brands/', permanent=False)),
]
