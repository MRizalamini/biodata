from django.shortcuts import render
from pribadiapp.models import Biodata
from pribadiapp.forms import FormBiodata

def pribadi(request):
    biodatas = Biodata.objects.all()
    context = {
        'biodatas': biodatas,
    }
    return render(request,'index.html',context)

def tambahkan(request):
    form = FormBiodata()
    
    context = {
        'form': form,
    }
    return render(request,'tambahkan.html',context)