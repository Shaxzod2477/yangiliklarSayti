from django.contrib import admin
from .models import Article,Comment


# Register your models here.
class CommentInline(admin.TabularInline):    #StackedInline
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


admin.site.register(Article)
admin.site.register(Comment)