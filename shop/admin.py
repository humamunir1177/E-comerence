from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    ProductImage,
    Customer_user,
    Profile
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'discount', 'image')

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'brand', 'image')
        }),
        ('Pricing', {
            'fields': ('price', 'discount')
        }),
        ('Product Details', {
            'fields': ('description', 'features', 'warranty')
        }),
        ('Status', {
            'fields': ('stock', 'popular')
        }),
    )

    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Customer_user)
admin.site.register(Profile)
