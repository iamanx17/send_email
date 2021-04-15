from django.contrib import admin
from .models import emailids

# Register your models here.

class emailAdmin(admin.ModelAdmin):
    fields=('email','user')
    list_display=['id','email','date','user']
    list_filter=['date']
    search_fields=['email']

admin.site.register(emailids,emailAdmin)
