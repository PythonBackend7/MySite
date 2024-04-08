from django.contrib import admin
from .models import Post, About, Contact, Category, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'author')
    filter_horizontal = ('tags',)
    list_filter = ('author', 'category',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_read')
    list_display_links = ('id', 'name', 'email', 'phone')
    search_fields = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(Tag)