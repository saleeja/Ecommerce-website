from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, StoreConfiguration


@admin.register(StoreConfiguration)
class StoreConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_tagline', 'whatsapp_number')
    fields = ('site_name', 'site_tagline', 'whatsapp_number', 'logo', 'hero_title', 'hero_subtitle', 'hero_banner')

    def has_add_permission(self, request):
        # Only allow one config record
        return not StoreConfiguration.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_featured', 'whatsapp_link', 'created_at')
    list_editable = ('is_featured',)
    list_filter = ('category', 'is_featured', 'stock')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('whatsapp_link', 'created_at', 'updated_at')

    def whatsapp_link(self, obj):
        url = obj.whatsapp_url()
        return format_html('<a href="{}" target="_blank">📱 WhatsApp Order</a>', url)
    whatsapp_link.short_description = 'WhatsApp'
