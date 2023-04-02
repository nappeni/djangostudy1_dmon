from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post,Comment,Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag','msg_length','message','is_public','created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" alt="" style="width: 75px;" />')
        return None

    # admin 단에 작성할 경우
    # def msg_length(self, post):
    #     return f"len(post.message) 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass