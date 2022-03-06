# and then the forms.py adjusted to the following:
#
# class ClientDetailsForm(ModelForm):
#     date_of_birth = DateField(input_formats=settings.DATE_INPUT_FORMATS)
#     class Meta:
#         model = ClientDetails


from django.forms import ModelForm

from products.models import Products


class ProductForm(ModelForm):
     class Meta:
        model=Products
        fields='__all__'