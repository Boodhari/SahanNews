from django.contrib import admin

# Register your models here.
from News.models import Category ,Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
 prepopulated_fields= {"slug":("title",)}
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
