#app-level url code:
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^deletecheck/(?P<course_id>\d+)$', views.deletecheck),
    url(r'^remove/(?P<course_id>\d+)$', views.remove),

]
