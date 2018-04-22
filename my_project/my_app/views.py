from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BankDetailForm
from .models import BankDetail

# Create your views here.


def bank_detail(request, ifsc=None):
    instance = get_object_or_404(BankDetail, ifsc=ifsc)
    context = {
        "ifsc": instance.ifsc,
        "bank_id": instance.bank_id,
        "branch": instance.branch,
        "address": instance.address,
        "city": instance.city,
        "district": instance.district,
        "state": instance.state,
        "bank_name": instance.bank_name,
        "instance": instance,
    }
    return render(request, "bank_detail.html", context)
