from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','msg_length','message','is_public','created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    # admin 단에 작성할 경우
    # def msg_length(self, post):
    #     return f"len(post.message) 글자"
