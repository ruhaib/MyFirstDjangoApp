
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^store/', include('super_store.urls')),
    url(r'^user/', include('authentication.urls'))
]
