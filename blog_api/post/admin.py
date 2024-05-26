from django.contrib import admin
from .models import Post


#  admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Post._meta.get_fields()]

    search_fields = ('title', 'text')
    list_filter = ('author',)
    readonly_fields = ('time_create', 'time_update')
