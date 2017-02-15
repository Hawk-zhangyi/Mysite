from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from django.contrib.admin.utils import flatten_fieldsets


#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data Name',         {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],})

    ]
#    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.register(Question)
#admin.site.register(Choice)
