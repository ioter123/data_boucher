from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Data


class DataAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Data, DataAdmin)