from django.shortcuts import render
from django.views import generic
from .models import ServerInfo
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'ServerManage/index.html'
    context_object_name = 'all_machine_list'
    def get_queryset(self):
        """Test! Last 5 items!"""
        return ServerInfo.objects.all()
