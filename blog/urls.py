from django.conf.urls import url

from blog.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]