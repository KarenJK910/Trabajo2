from django.contrib import admin
from . import models

# Register your models here.
from .models import Ods,Posts,Comentarios

admin.site.register(Ods)
admin.site.register(Posts)
admin.site.register(Comentarios)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("Posts", "name", "body", "date_added", "status")
    list_filter = ("status")
    search_fields = ("Posts", "name", "body", "date_added")