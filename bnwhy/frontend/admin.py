from django.contrib import admin
from bnwhy.api.models import Post, Comment, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)