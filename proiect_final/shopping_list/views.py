from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from products.forms import ProductForm
from products.models import Products
# from shopping_list.forms import ProductForm
from shopping_list.models import ShoppingList
from django.db.models import F, Q


# from my_web_app.products.models import Products


class CreateShoppingListView(CreateView):
    model = Products
    fields = ['tip_produs', 'necesar', 'um']
    template_name = 'products_form.html'

    print('save')

    def get_success_url(self):
        return reverse('shopping_list:lista_cumparaturi')


class ShoppingListView(ListView):
    model = Products
    template_name = 'shopping_list_index.html'
    # paginate_by = 5


    def get_queryset(self):        
        return Products.objects.filter(Q(active = True) & ((Q(recur=True) & Q(cantitate__lte=F('minqty'))) | Q(necesar__gt=0)))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShoppingListView, self).get_context_data()
        context['form'] = ProductForm
        return context
    # return ShoppingList.objects.filter(active = True,recur=True,cantitate__lte=F('minqty'))
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super(ShoppingListView, self).get_context_data()
    #     # data['form'] = ProductForm
    #     recur = Products.objects
    #     data['recur'] = recur
    #     return data

    # if Products.objects.filter(cantitate=0):
    #     um = Products.objects.get(id=igredients(gabriel)).um
    #     ShoppingList.objects.create(tip_produs=ingredients(Gabriel), cantintate=0, um=um)

class UpdateShoppingListView(UpdateView):
    model = ShoppingList
    fields = '__all__'
    # fields = ['city', 'country']
    template_name = 'shopping_list_form.html'

    # def get_queryset(self):
    #     if self.request.user.customer_id:
    #         location_of_company = Companies.objects.filter(id=self.request.user.customer.id).last().location.id
    #         return Location.objects.filter(active=True, id=location_of_company)
    #     return Location.objects.filter(active=True)

    def get_success_url(self):
        return reverse('shopping_list:lista_cumparaturi')

def deactivate_products(request, pk):
    if ShoppingList.objects.filter(id=pk).exists():
        ShoppingList.objects.filter(id=pk).update(active=False)
    return redirect('shopping_list:lista_cumparaturi')



