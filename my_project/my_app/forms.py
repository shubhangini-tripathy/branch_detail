from django import forms

from .models import BankDetail


class BankDetailForm(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = [
            "ifsc", "bank_id", "branch", "address", "city", "district",
            "state", "bank_name"
        ]
