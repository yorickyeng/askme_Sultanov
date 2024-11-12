from django.contrib import admin
from app import models

admin.site.register(models.Question)
admin.site.register(models.QuestionLike)
admin.site.register(models.Answer)
admin.site.register(models.AnswerLike)
admin.site.register(models.Tag)
