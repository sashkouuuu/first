from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from blog.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^moda/$',moda, name='moda'),
    url(r'^culture/$',culture, name='culture')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)