from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='IndexView'),
    #url(r'^board$', views.BoardView.as_view(), name='BoardView'),
    #url(r'^wait$', views.Waiting, name='Waiting'),
]
