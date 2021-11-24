from django.contrib import admin
from . import models
#from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline,
            ]

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
