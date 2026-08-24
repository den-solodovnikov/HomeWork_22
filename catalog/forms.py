from PIL import Image
from django.core.exceptions import ValidationError
from django import forms
from .models import Product


FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите подробное описание'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену товара'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        allowed_ext = ['PNG', 'JPEG']
        if image:
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError('Размер изображение не должен превышать 5 МБ')

            try:
                img = Image.open(image)
                if img.format not in allowed_ext:
                    raise ValidationError(f'Недопустимый формат изображения (допустимые: {allowed_ext})')
            except Exception:
                raise ValidationError('Загруженный файл не является корректным изображением.')
        return image

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in FORBIDDEN_WORDS:
            if name and description and word.lower() in name.lower() or word.lower() in description.lower():
                self.add_error('name', 'Name не может содержать слово {word}')
