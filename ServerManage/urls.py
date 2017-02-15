from django.conf.urls import url
from . import views

app_name='ServerManage'

urlpatterns = [
    # ex: /script/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /script/5/
]
