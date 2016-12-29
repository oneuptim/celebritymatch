from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index), # Stop forgetting to add the $ at the end of this URL.
    url(r'^process$', views.process),
    url(r'^results$', views.results),
]
