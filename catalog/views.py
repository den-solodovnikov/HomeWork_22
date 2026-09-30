from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:home')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    # success_url = reverse_lazy('catalog:home')
    login_url = reverse_lazy('users:login')
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if not user == self.object.owner or not user.has_perm('catalog.change_product'):
            return HttpResponseForbidden('У вас нет прав для удаления продукта.')
        return ProductForm

class ProductsListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    login_url = reverse_lazy('users:login')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    login_url = reverse_lazy('users:login')

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user = self.request.user

        if not user == self.object.owner or not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden('У вас нет прав для удаления продукта.')
        product.delete()
        return redirect('catalog:home')


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ("name", "phone", "message")
    template_name = "catalog/contact_form.html"
    context_object_name = "contacts"
    success_url = reverse_lazy('catalog:contact_form')
    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)
        # Добавляем последнюю запись в контекст по ключу last_record
        context['last_record'] = Contact.objects.latest('id')
        return context

def unpublished_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет прав для снятия с публикации продукта.')
    product.is_publicated = False
    product.save()
    return redirect(reverse('catalog:home'))
