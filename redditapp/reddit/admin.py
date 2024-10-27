from django.contrib import admin
from .models import Topic, Question, Answer

# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Topic, TopicAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'created_at')
    # list_filter = ('topic',)

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at')

admin.site.register(Answer, AnswerAdmin)