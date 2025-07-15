from rest_framework import serializers
from .models import Floor, Hall, BedSpace, Program, Applicants


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    floor = FloorSerializer(read_only=True)
    floor_id = serializers.PrimaryKeyRelatedField(queryset=Floor.objects.all(), source='floor', write_only=True)

    class Meta:
        model = Hall
        fields = ['id', 'name', 'floor', 'floor_id', 'created_at', 'updated_at']


class BedSpaceSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)
    hall_id = serializers.PrimaryKeyRelatedField(queryset=Hall.objects.all(), source='hall', write_only=True)

    class Meta:
        model = BedSpace
        fields = ['id', 'name', 'number_of_beds', 'hall', 'hall_id', 'created_at', 'updated_at']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class ApplicantsSerializer(serializers.ModelSerializer):
    year = ProgramSerializer(read_only=True)
    year_id = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all(), source='year', write_only=True)

    class Meta:
        model = Applicants
        fields = [
            'id', 'fullname', 'phone_number', 'gender', 'age', 'marital_status',
            'num_children_below_10', 'names_of_children', 'country', 'state',
            'arrival_date', 'disability_or_allergy', 'local_assembly',
            'local_assembly_address', 'code', 'year', 'year_id',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['code', 'created_at', 'updated_at']
