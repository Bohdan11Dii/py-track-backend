from django import forms
from quizzes.models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
