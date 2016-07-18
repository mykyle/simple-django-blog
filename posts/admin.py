from django.contrib import admin

from posts.models import *

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","content","timestamp","updated"]
    search_fields=["title","content"]
    list_editable=["title"]
    list_display_link=["updated"]
    class meta:
        model=Post

admin.site.register(Post,PostModelAdmin)
