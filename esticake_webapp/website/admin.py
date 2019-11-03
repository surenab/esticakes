from django.contrib import admin
from .models import Cake
# Register your models here.
class CakeModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cake._meta.get_fields()]
    search_fields = ('name','description')
admin.site.register(Cake,CakeModelAdmin)
