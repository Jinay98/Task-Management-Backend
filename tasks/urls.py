from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^tasks/$', views.task_list),
    url(r'^task-details/(?P<pk>[0-9]+)$', views.task_detail),

]