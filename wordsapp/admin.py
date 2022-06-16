from csv import list_dialects
from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

    list_display_links = ('id','title')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','question')

    list_display_links = ('id','question')


admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)
