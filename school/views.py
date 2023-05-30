from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentsStudentListSerializer, StuentsEnrollmentsListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    """Display All Students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    """Display All Courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """Display All Enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

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