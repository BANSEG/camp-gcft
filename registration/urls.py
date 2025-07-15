from django.urls import path
from .views import (
    FloorListCreateView, FloorRetrieveUpdateDestroyView,
    HallListCreateView, HallRetrieveUpdateDestroyView,
    BedSpaceListCreateView, BedSpaceRetrieveUpdateDestroyView,
    ProgramListCreateView, ProgramRetrieveUpdateDestroyView,
    ApplicantsListCreateView, ApplicantsRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Floor
    path('floors/', FloorListCreateView.as_view(), name='floor-list-create'),
    path('floors/<int:pk>/', FloorRetrieveUpdateDestroyView.as_view(), name='floor-detail'),

    # Hall
    path('halls/', HallListCreateView.as_view(), name='hall-list-create'),
    path('halls/<int:pk>/', HallRetrieveUpdateDestroyView.as_view(), name='hall-detail'),

    # BedSpace
    path('bedspaces/', BedSpaceListCreateView.as_view(), name='bedspace-list-create'),
    path('bedspaces/<int:pk>/', BedSpaceRetrieveUpdateDestroyView.as_view(), name='bedspace-detail'),

    # Program
    path('programs/', ProgramListCreateView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', ProgramRetrieveUpdateDestroyView.as_view(), name='program-detail'),

    # Applicants
    path('applicants/', ApplicantsListCreateView.as_view(), name='applicants-list-create'),
    path('applicants/<int:pk>/', ApplicantsRetrieveUpdateDestroyView.as_view(), name='applicants-detail'),
]
