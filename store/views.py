from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Category, Product

class HomeView(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        q = self.request.GET.get('q', '').strip()
        view_all = self.request.GET.get('view_all', '')

        products = Product.objects.all()

        if q:
            # Search overrides featured filter — show all matching products
            products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
            context['search_query'] = q
            context['show_all'] = True
        elif view_all:
            # Explicit "View all" click — show every product
            context['show_all'] = True
        else:
            # Default homepage — only featured products
            products = products.filter(is_featured=True)
            context['show_all'] = False

        context['products'] = products
        return context

class CategoryView(ListView):
    model = Product
    template_name = 'store/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs['slug'])
