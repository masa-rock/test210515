from django.contrib import admin
from .models import Category,Tag,Post

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
