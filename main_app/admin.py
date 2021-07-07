from django.contrib import admin
# import your models here
from .models import Champion, Comment, Favorite

# Register your models here.
admin.site.register(Champion)
admin.site.register(Comment)
admin.site.register(Favorite)