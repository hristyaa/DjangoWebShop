from django.forms import ModelForm

from catalog.models import Product


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

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if name:
            for word in words:
                if f' {word} ' in f' {name.lower()} ':
                    self.add_error('name',
                           '''Наименование содержит запрещенные слова: 
казино, криптовалюта, крипта, биржа,дешево,бесплатно,обман,полиция,радар.''')
                    break

        if description:
            for word in words:
                if f' {word} ' in f' {description.lower()} ':
                    self.add_error('description',
                                       '''Наименование содержит запрещенные слова: 
            казино, криптовалюта, крипта, биржа,дешево,бесплатно,обман,полиция,радар.''')
                    break

        return cleaned_data


