from django.contrib import admin
from apps.article.models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'slug',
        'writer',
        'created_date',
        'content'
    ]

admin.site.register(Article, ArticleAdmin)
