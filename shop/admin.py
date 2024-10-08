from django.contrib import admin
from .models import Catagory
from .models import Product

'''class CatrgoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
admin.site.register(Catagory,CatrgoryAdmin)
'''

admin.site.register(Catagory)
admin.site.register(Product)