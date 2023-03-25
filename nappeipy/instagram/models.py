from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')

    # JAVA toString
    def __str__(self):
        #return f"Custom Post object ({self.id})"
        return self.message

    def msg_length(self):
        return len(self.message)

    msg_length.short_description = "메세지 글자수"
