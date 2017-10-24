from django.conf.urls import url

from blog.views import home, moda

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^act/moda/$',moda, name='moda')
]