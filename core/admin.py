from django.contrib import admin
from django.forms import forms, Textarea
from django.db import models
from core.models import QuizQuestion, QuizCategory, MyResults, Progress, UserSubmittedAnswer





# Register your models here.
admin.site.register(QuizCategory)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question']


admin.site.register(QuizQuestion, QuizQuestionAdmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id','question','user','right_answer']
admin.site.register(UserSubmittedAnswer, UserSubmittedAnswerAdmin)



admin.site.register(MyResults)

admin.site.register(Progress)
