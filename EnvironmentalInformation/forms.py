from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Guidances

class GuidancesAdminForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Guidances
        fields = '__all__'
