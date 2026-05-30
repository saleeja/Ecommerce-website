from .models import StoreConfiguration


def store_config(request):
    """Inject StoreConfiguration into every template context."""
    config = StoreConfiguration.objects.first()
    if not config:
        # Create a default config if none exists
        config = StoreConfiguration.objects.create()
    return {
        'site_config': config,
        'site_name': config.site_name,
        'site_tagline': config.site_tagline,
    }
