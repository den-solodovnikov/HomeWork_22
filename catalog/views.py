from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    # success_url = reverse_lazy('catalog:home')
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

class ContactCreateView(CreateView):
    model = Contact
    fields = ("name", "phone", "message")
    template_name = "catalog/contact_form.html"
    context_object_name = "contacts"
    success_url = reverse_lazy('catalog:contact_form')

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)
        # Добавляем последнюю запись в контекст по ключу last_record
        context['last_record'] = Contact.objects.latest('id')
        return context



