from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild_value in self.fields.items():
            if isinstance(fild_value, BooleanField):
                fild_value.widget.attrs['class'] = 'form-check-input'
            else:
                fild_value.widget.attrs['class'] = 'form-control'

class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'country', 'password1', 'password2',)