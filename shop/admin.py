from django.contrib import admin
from .models import *


from .forms import *
from django.contrib.auth.admin import UserAdmin


"""----------------------------------------------------------------------"""
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('id', 'email', 'username')
    list_display_links = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': ('city', 'phone')
            }
        ),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                'fields': ('first_name', 'last_name', 'email', 'city', 'phone')
            }
        ),
    )

    ordering = ('id', 'username')
"""----------------------------------------------------------------------"""



#продукт
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category', 'made')
    list_display_links = ('id', 'name')


#категория
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)


#цвет
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)


#разммер
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('id',)


