from django.contrib import admin
from pribadiapp.models import Biodata
# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = ['npm','nama','alamat','tetala', 'kelas']
    search_fields = ['npm','nama','alamat','tetala', 'kelas']
    list_display = ['npm','nama','alamat','tetala', 'kelas']
    list_per_page =6
    
admin.site.register(Biodata)