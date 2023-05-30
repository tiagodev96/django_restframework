from rest_framework import generics
from school.models import Enrollment
from school.serializer import EnrollmentsStudentListSerializer, StuentsEnrollmentsListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class EnrollmentsStudentList(generics.ListAPIView):
    """List all Student's Enrollments"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentsStudentListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentsEnrollmentList(generics.ListAPIView):
    """List all Enrollment's students"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = StuentsEnrollmentsListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]