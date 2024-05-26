from django.contrib import admin
from .models import Post


#  admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = '__all__'
    search_fields = ('title', 'text')
    list_filter = ('author',)
    readonly_fields = ('created_at', 'updated_at')
