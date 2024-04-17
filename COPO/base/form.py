from django.forms import ModelForm
from .models import CalculateExcel

class ExcelForm(ModelForm):
    class Meta:
        model = CalculateExcel
        fields = ['subject','type','semester','attainment','courseOutCome','file']