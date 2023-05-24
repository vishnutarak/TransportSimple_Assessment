from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(DisplayQuestions)
admin.site.register(DisplayAnswers)
admin.site.register(Like)