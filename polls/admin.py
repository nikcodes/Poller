from django.contrib import admin
from .models import Question,Choice

class for_choice(admin.TabularInline):
    model=Choice
    extra=2

class first(admin.ModelAdmin):
    # fieldsets = [
    #     ('Major details',{'fields':['question_text'],'classes':['collapse']}),
    #     ('Time',{'fields':['pub_date']})
    # ]
    # inlines=[for_choice]
    list_display=('pub_date','question_text','recent')
    list_filter=['pub_date']
    search_fields=['question_text']


admin.site.register(Question,first)