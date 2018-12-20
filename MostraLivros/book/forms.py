from django.forms import *
from book.models import *
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'birth_date':forms.DateInput(
                attrs = {
                    'type':'date'
                }
            )
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'