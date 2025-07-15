from import_export import resources
from .models import Floor, Hall, BedSpace, Program, Applicants

class FloorResource(resources.ModelResource):
    class Meta:
        model = Floor
        fields = '__all__'

class HallResource(resources.ModelResource):
    class Meta:
        model = Hall
        fields = '__all__'

class BedSpaceResource(resources.ModelResource):
    class Meta:
        model = BedSpace
        fields = '__all__'

class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        fields = '__all__'

class ApplicantsResource(resources.ModelResource):
    class Meta:
        model = Applicants
        fields = '__all__'
