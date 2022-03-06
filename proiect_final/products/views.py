# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from products.models import Products


class CreateProductView(CreateView):
    model = Products
    fields = ['tip_produs', 'cantitate', 'um', 'expiration_date', 'minqty', 'recur']
    template_name = 'products_form.html'

    def get_success_url(self):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER','/'))


class ProductsView(ListView):
    model = Products
    template_name = 'products_index.html'
    paginate_by = 10

    def get_queryset(self):
        return Products.objects.filter(active=True,cantitate__gt=0)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProductsView, self).get_context_data()
        return data


class UpdateProductView(UpdateView):
    model = Products
    fields = '__all__'
    # fields = ['city', 'country']
    template_name = 'products_form.html'

    # def get_queryset(self):
    #     if self.request.user.customer_id:
    #         location_of_company = Companies.objects.filter(id=self.request.user.customer.id).last().location.id
    #         return Location.objects.filter(active=True, id=location_of_company)
    #     return Location.objects.filter(active=True)

    def get_success_url(self):
        return reverse('products:lista_produse')

def deactivate_products(request, pk):
    if Products.objects.filter(id=pk).exists():
        Products.objects.filter(id=pk).update(active=False)
    return redirect('products:lista_produse')

def cumpara(request,pk):
    if(request.method == 'POST'):
        product = Products.objects.get(pk=pk)
        product.cantitate = int(request.POST.get('cantitate')) + product.cantitate 
        product.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def modifica_necesar(request,pk):
    if request.method == 'GET':
        return JsonResponse({'success':True})
    if(request.method == 'POST'):
        product = Products.objects.get(pk=pk)
        product.necesar = int(request.POST.get('necesar'))
        product.save()
        return JsonResponse({'success':True})
        
