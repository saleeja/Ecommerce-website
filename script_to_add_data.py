from store.models import Category, Product

categories = {
    "Electronics": [
        ("Smart Fitness Watch v2", 749, 25),
        ("Wireless Earbuds Pro", 1299, 30),
        ("Bluetooth Speaker Mini", 899, 15),
        ("Power Bank 20000mAh", 1499, 20),
        ("USB-C Fast Charger", 499, 40),
    ],
    "Mobile": [
        ("Android Smartphone X1", 12999, 10),
        ("Wireless Charger", 999, 15),
        ("Phone Case Premium", 299, 50),
        ("Screen Protector", 199, 100),
        ("Mobile Stand", 249, 40),
    ],
    "Home & Kitchen": [
        ("Electric Kettle", 899, 20),
        ("Air Fryer 4L", 3499, 8),
        ("Vegetable Chopper", 349, 30),
        ("Non-Stick Fry Pan", 699, 15),
        ("Rice Cooker", 1999, 12),
    ],
    "Home & Living": [
        ("LED Table Lamp", 599, 25),
        ("Wall Clock", 799, 10),
        ("Storage Organizer", 499, 35),
        ("Decorative Plant Pot", 399, 20),
        ("Study Desk", 3999, 5),
    ],
}

for category_name, products in categories.items():

    category, _ = Category.objects.get_or_create(
        name=category_name
    )

    for name, price, stock in products:

        Product.objects.get_or_create(
            name=name,
            defaults={
                "category": category,
                "description": f"Premium quality {name.lower()} for everyday use.",
                "price": price,
                "stock": stock,
                "is_featured": True,
            }
        )

print("Products added successfully!")