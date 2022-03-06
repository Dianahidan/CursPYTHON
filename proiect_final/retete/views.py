from django.shortcuts import render

def retete_view(request):
    return render(request, 'retete.html', {'title': 'Retete'})




# # from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
# from django.urls import reverse
# from django.views.generic import ListView, UpdateView
# from products.models import Products

# class ProductsView(ListView):
#     model = Products
#     template_name = 'products_index.html'
#     paginate_by = 10

#     def get_queryset(self):
#         return Products.objects.filter(active=True)

#     def get_context_data(self, *, object_list=None, **kwargs):
#         data = super(ProductsView, self).get_context_data()
#         return data


# class UpdateProductView(UpdateView):
#     model = Products
#     fields = '__all__'
#     # fields = ['city', 'country']
#     template_name = 'products_form.html'

#     # def get_queryset(self):
#     #     if self.request.user.customer_id:
#     #         location_of_company = Companies.objects.filter(id=self.request.user.customer.id).last().location.id
#     #         return Location.objects.filter(active=True, id=location_of_company)
#     #     return Location.objects.filter(active=True)

#     def get_success_url(self):
#         return reverse('products:lista_produse')




# # from django.shortcuts import redirect
# # from django.urls import reverse
# # from django.views.generic import CreateView, ListView, UpdateView
# # from retete.models import Reteta
# # from products.models import Products
# # from django.contrib.auth.decorators import login_required
# # from django.contrib.auth.mixins import LoginRequiredMixin


# # class CreateRetetaView(LoginRequiredMixin, CreateView):
# #     model = Reteta
# #     # fields = '__all__' # le afisam pe toate din models
# #     fields = ['tip_ingredient', 'cantitate', 'um']
# #     template_name = 'retete_form.html'

# #     def get_success_url(self):
# #         return reverse('retete:adauga')


# # class ReteteView(ListView):
# #     model = Reteta
# #     template_name = 'retete_index.html'
# #     # paginate_by = 5

# #     def get_queryset(self):
# #         return Reteta.objects.filter()


# # class UpdateRetetaView(UpdateView):
# #     model = Reteta
# #     # fields = '__all__'
# #     fields = ['tip_ingredient', 'cantitate', 'um']
# #     template_name = 'reteta_form.html'

# #     def get_queryset(self):
# #         return Reteta.objects.filter()

# #     def get_success_url(self):
# #         return reverse('retete:lista_retete')


# # @login_required
# # def updateQuantityView(request, pk):
# #     if Reteta.objects.filter(id=pk).exists():
# #         reteta_instance = Reteta.objects.get(id=pk)
# #         produs = reteta_instance.cantitate
# #         quantity_diff = reteta_instance.cantitate.cantitate - 1
# #         Products.objects.filter(id=produs.id).update(cantitate=quantity_diff)
# #     return redirect('retete:lista_retete')


# # @login_required
# # def deactivate_recipe(request, pk):
# #     if Reteta.objects.filter(id=pk, name=Reteta.tip_produs).exists:
# #         Reteta.objects.filter(id=pk, name=Reteta.tip_produs).update(active=False)
# #     return redirect('recipes:lista_retete')