from django.urls import path, include
from school.views import EnrollmentsStudentList, StudentsEnrollmentList
from school.viewsets import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments/', EnrollmentsStudentList.as_view()),
    path('enrollments/<int:pk>/students/', StudentsEnrollmentList.as_view())
]