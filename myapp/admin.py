from django.contrib import admin

# Register your models here.
from myapp.models import Item

admin.site.register(Item)