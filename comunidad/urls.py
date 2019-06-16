from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from comunidad import views

urlpatterns = [
	url(r'^comunidad/$', views.ComunidadList.as_view()),
	url(r'^comunidad/(?P<pk>[0-9])+/$', views.ComunidadDetail.as_view()),
	url(r'^miembro/$', views.ComunidadList.as_view()),
	url(r'^miembro/(?P<pk>[0-9])+/$', views.ComunidadDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)