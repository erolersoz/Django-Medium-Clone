from django.contrib import admin
from .models import Category , Tag, BlogPost , UserPostFav
# Register your models here.
@admin.register(UserPostFav)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'user',
        'post',
        'is_deleted',]  
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'title',
        'is_active',]


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'title',
        'is_active',]


@admin.register(BlogPost)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'title',
        'is_active',
        'user',
        'view_count',
    ]
    