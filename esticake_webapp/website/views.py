from django.views import generic
from .models import Cake
from django.utils import timezone
from django.views.generic.detail import DetailView

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'cake_list'

    def get_queryset(self):
        return Cake.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        cakes = Cake.objects.all()
        context['cakes'] = cakes
        return context

class AboutView(generic.ListView):
    template_name = 'about.html'
    context_object_name = 'cake_list'
    def get_queryset(self):
        return Cake.objects.all()

class ContactsView(generic.ListView):
    template_name = 'contacts.html'
    context_object_name = 'cake_list'
    def get_queryset(self):
        return Cake.objects.all()

class ServicestsView(generic.ListView):
    template_name = 'services.html'
    context_object_name = 'cake_list'
    def get_queryset(self):
        return Cake.objects.all()

class BlogView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'cake_list'
    def get_queryset(self):
        return Cake.objects.all()

class CakeDetailView(DetailView):
    template_name = 'products-detail.html'
    model = Cake
    context_object_name = 'ccake'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['cakes'] = Cake.objects.all()[:4]
        return context

class ProductsView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'cake_list'
    def get_queryset(self):
        return Cake.objects.all()
