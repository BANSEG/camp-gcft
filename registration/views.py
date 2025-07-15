from rest_framework import generics
from .models import Floor, Hall, BedSpace, Program, Applicants
from .serializers import (
    FloorSerializer,
    HallSerializer,
    BedSpaceSerializer,
    ProgramSerializer,
    ApplicantsSerializer,
)

# === FLOOR VIEWS ===
class FloorListCreateView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class FloorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


# === HALL VIEWS ===
class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class HallRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


# === BEDSPACE VIEWS ===
class BedSpaceListCreateView(generics.ListCreateAPIView):
    queryset = BedSpace.objects.all()
    serializer_class = BedSpaceSerializer

class BedSpaceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedSpace.objects.all()
    serializer_class = BedSpaceSerializer


# === PROGRAM VIEWS ===
class ProgramListCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


# === APPLICANT VIEWS ===
class ApplicantsListCreateView(generics.ListCreateAPIView):
    queryset = Applicants.objects.all()
    serializer_class = ApplicantsSerializer

class ApplicantsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicants.objects.all()
    serializer_class = ApplicantsSerializer
