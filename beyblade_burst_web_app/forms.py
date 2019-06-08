from django import forms

from .models import BeybladePart, Combination


class BeybladePartCreateForm(forms.ModelForm):
    
    class Meta:
        model = BeybladePart
        exclude = ['aliases']

class CombinationCreateForm(forms.ModelForm):
    
    class Meta:
        model = Combination
        exclude = ['name']

    def __init__(self, *args, **kwargs):
        super(CombinationCreateForm, self).__init__(*args, **kwargs)
        self.fields['layer'] = forms.ModelChoiceField(queryset=BeybladePart.objects.filter(part_type="LAYER"))
        self.fields['disk'] = forms.ModelChoiceField(queryset=BeybladePart.objects.filter(part_type="DISK"))
        self.fields['tip'] = forms.ModelChoiceField(queryset=BeybladePart.objects.filter(part_type="TIP"))
