from django.contrib import admin

# Register your models here.
from .models import Ods,Posts

admin.site.register(Ods)
admin.site.register(Posts)