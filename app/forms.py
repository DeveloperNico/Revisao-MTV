from .models import *
from django import forms


class PersonagemForm(forms.ModelForm):
    class Meta:
        model = PersonagemHarryPotter
        fields = '__all__'

    def __init(self, *args, **kwargs):
        super(PersonagemForm, self).__init__(*args, **kwargs)

        if self.isinstance and self.instance.pk:
            self.fields['cpf'].disabled = True
