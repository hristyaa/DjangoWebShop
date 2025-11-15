from django.forms import ModelForm

from catalog.models import Product
from django.core.exceptions import ValidationError

WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название', }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание', }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control'}
        )

        self.fields['category'].widget.attrs.update(
            {
                'class': 'form-control'}
        )

        self.fields['price'].widget.attrs.update(
            {
                'class': 'form-control'
            }
        )

        self.fields['is_available'].widget.attrs.update(
            {
                'class': 'form-check-input'
            }
        )

    def clean_name(self):
        """Валидация названия (отсутствие запрещенных слов)"""
        name = self.cleaned_data.get('name')
        if name:
            for word in WORDS:
                if f' {word} ' in f' {name.lower()} ':
                    raise ValidationError('''Наименование содержит запрещенные слова
(казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар).''')
        return name

    def clean_description(self):
        """Валидация описания (отсутствие запрещенных слов)"""
        description = self.cleaned_data.get('description')
        if description:
            for word in WORDS:
                if f' {word} ' in f' {description.lower()} ':
                    raise ValidationError('''Описание содержит запрещенные слова 
(казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар).''')
        return description

    def clean_price(self):
        """Валидация цены (цена продукта не может быть отрицательной)"""
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price


    # def clean_image(self):
    #     """Валидация цены (цена продукта не может быть отрицательной)"""
    #     price = self.cleaned_data.get('price')
    #     if price<0:
    #         raise ValidationError('Цена продукта не может быть отрицательной')
    #     return price








