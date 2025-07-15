from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin
from .models import Floor, Hall, BedSpace, Program, Applicants
from .resources import FloorResource, HallResource, BedSpaceResource, ProgramResource, ApplicantsResource

@admin.register(Floor)
class FloorAdmin(ImportExportModelAdmin):
    resource_class = FloorResource
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Hall)
class HallAdmin(ImportExportModelAdmin):
    resource_class = HallResource
    list_display = ['name', 'floor', 'created_at']
    search_fields = ['name', 'floor__name']
    list_filter = ['floor']


@admin.register(BedSpace)
class BedSpaceAdmin(ImportExportModelAdmin):
    resource_class = BedSpaceResource
    list_display = ['name', 'hall', 'number_of_beds']
    search_fields = ['name', 'hall__name']
    list_filter = ['hall']


@admin.register(Program)
class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource
    list_display = ['year']
    search_fields = ['year']


@admin.register(Applicants)
class ApplicantsAdmin(ImportExportModelAdmin):
    resource_class = ApplicantsResource
    list_display = ['fullname', 'phone_number', 'gender', 'age', 'marital_status', 'state', 'country', 'code']
    search_fields = ['fullname', 'phone_number', 'country', 'state', 'local_assembly', 'code']
    list_filter = ['gender', 'marital_status', 'state', 'country', 'year']
