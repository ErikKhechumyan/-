from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import product,menu,serv,about,cont,projectss,Us,flag
# Register your models here.

admin.site.register(product)
admin.site.register(menu)
admin.site.register(serv)
admin.site.register(about)
admin.site.register(cont)
admin.site.register(projectss)
admin.site.register(Us)
admin.site.register(flag)