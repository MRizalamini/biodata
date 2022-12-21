from django.forms import ModelForm
from pribadiapp.models import Biodata
class FormBiodata(ModelForm):
    class Meta:
      model = Biodata
      fields =  "__all__"