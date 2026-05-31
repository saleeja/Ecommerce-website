from django.db import models
from django.utils.text import slugify
import urllib.parse


WHATSAPP_PHONE = '1234567890'   # ← Change to your business WhatsApp number


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class StoreConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default="Papparazzo")
    site_tagline = models.CharField(max_length=255, default="Shop Smarter, Order via WhatsApp")
    whatsapp_number = models.CharField(max_length=20, default="1234567890", help_text="Business WhatsApp phone number")
    logo = models.ImageField(upload_to='store/', blank=True, null=True, help_text="Upload custom store logo. For best styling, please upload a small image with a height around 32px to 40px, ideally a transparent PNG/SVG (fallback to default SVG logo if empty)")
    hero_title = models.CharField(max_length=255, default="Shop Smart.<br>Order Instantly via <span>WhatsApp</span>", help_text="HTML tags like <span> are allowed for styling")
    hero_subtitle = models.TextField(default="Quality products, best prices and fast delivery. Just choose and order on WhatsApp!")
    hero_banner = models.ImageField(upload_to='store/', blank=True, null=True, help_text="Upload custom hero banner image (fallback to default generated image if empty)")

    class Meta:
        verbose_name = "Store Configuration"
        verbose_name_plural = "Store Configuration"

    def __str__(self):
        return self.site_name


class Product(models.Model):
    category   = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name       = models.CharField(max_length=150)
    slug       = models.SlugField(max_length=160, unique=True, blank=True)
    description = models.TextField(blank=True)
    price      = models.DecimalField(max_digits=10, decimal_places=2)
    stock      = models.PositiveIntegerField(default=0)
    image      = models.ImageField(upload_to='products/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Show this product in the Featured Products section on the homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["slug"])]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def whatsapp_url(self):
        """Generate a WhatsApp deep-link with a pre-filled order message."""
        config = StoreConfiguration.objects.first()
        phone = config.whatsapp_number if config else WHATSAPP_PHONE
        msg = (
            f"Hello! I'd like to order:\n\n"
            f"*{self.name}*\n"
            f"Category: {self.category.name}\n"
            f"Price: ₹{self.price}\n\n"
            f"Please let me know availability. Thank you!"
        )
        encoded = urllib.parse.quote(msg)
        return f"https://wa.me/{phone}?text={encoded}"
