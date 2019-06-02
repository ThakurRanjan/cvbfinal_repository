from django.contrib import admin
from cbvfinalapp.models import Beer

class BeerAdmin(admin.ModelAdmin):
    list_display = ['name','teste','color','price']

admin.site.register(Beer,BeerAdmin)
