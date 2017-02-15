from django.contrib import admin

# Register your models here.
from .models import Blog,Tag,Catagory,Comment


admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Catagory)