import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomsite.settings')
django.setup()

from store.models import Category, Product

def populate():
    print("Populating database...")
    
    # Create Categories
    electronics, _ = Category.objects.get_or_create(name="Electronics")
    home, _ = Category.objects.get_or_create(name="Home & Living")
    
    # Create Products
    products = [
        {
            "category": electronics,
            "name": "Wireless Noise-Cancelling Headphones",
            "description": "Experience premium sound quality with industry-leading active noise cancellation. Features up to 30 hours of battery life and quick charge technology.",
            "price": 14999.00,
            "stock": 15
        },
        {
            "category": electronics,
            "name": "Smart Fitness Watch v2",
            "description": "Track your daily activity, heart rate, sleep stages, and more. Waterproof with built-in GPS and a vibrant AMOLED display.",
            "price": 7499.00,
            "stock": 8
        },
        {
            "category": home,
            "name": "Ceramic Essential Oil Diffuser",
            "description": "Create a calming environment in any room with this ultrasonic diffuser. Crafted from high-quality ceramic, it runs silently for up to 8 hours.",
            "price": 2499.00,
            "stock": 25
        },
        {
            "category": home,
            "name": "Ergonomic Memory Foam Pillow",
            "description": "Designed to provide optimal neck support and alignment. Made with breathable cooling gel memory foam for a comfortable sleep.",
            "price": 1899.00,
            "stock": 0  # Out of stock
        }
    ]
    
    for p_data in products:
        p, created = Product.objects.get_or_create(
            category=p_data["category"],
            name=p_data["name"],
            defaults={
                "description": p_data["description"],
                "price": p_data["price"],
                "stock": p_data["stock"]
            }
        )
        if created:
            print(f"Created product: {p.name}")
        else:
            print(f"Product already exists: {p.name}")

    # Create admin user if not exists
    from django.contrib.auth.models import User
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        print("Created superuser 'admin' with password 'admin123'")
    else:
        print("Superuser 'admin' already exists")

if __name__ == "__main__":
    populate()
