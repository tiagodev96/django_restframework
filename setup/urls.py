
from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, EnrollmentsStudentList, StudentsEnrollmentList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments/', EnrollmentsStudentList.as_view()),
    path('enrollments/<int:pk>/students/', StudentsEnrollmentList.as_view())
]
