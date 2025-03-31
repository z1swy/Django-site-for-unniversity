from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import Course, Institute, Department, Lecture, Enrollment, Unit
from .permissions import IsTeacherOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        student_id = self.request.query_params.get('studentId', None)
        teacher_id = self.request.query_params.get('teacherId', None)

        if student_id is not None:
            queryset = queryset.filter(students__id=student_id)

        if teacher_id is not None:
            queryset = queryset.filter(teacher__id=teacher_id)

        return queryset

    def list(self, request, *args, **kwargs):
        catalog = self.request.query_params.get('catalog', None)
        if catalog is not None:
            catalog_courses = []
            institutes = Institute.objects.prefetch_related('departments__courses__teacher',
                                                            'departments__courses__students')
            for institute in institutes:
                institute_data = {
                    'institute': institute.name,
                    'departments': []
                }
                for department in institute.departments.all():
                    department_data = {
                        'name': department.name,
                        'courses': []
                    }
                    for course in department.courses.all():
                        course_data = {
                            'name': course.title,
                            'year': course.year,
                            'teacher': course.teacher.get_full_name(),
                            'students': [student.get_full_name() for student in course.students.all()]
                        }
                        department_data['courses'].append(course_data)
                    institute_data['departments'].append(department_data)
                catalog_courses.append(institute_data)
            return Response(catalog_courses)

        return super().list(request, *args, **kwargs)


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsTeacherOrReadOnly]

    def get_queryset(self):
        unit_id = self.kwargs.get('unit_id')
        if unit_id is not None:
            return Lecture.objects.filter(unit=unit_id)
        return Lecture.objects.all()

    def perform_create(self, serializer):
        unit_id = self.kwargs['unit_id']
        unit = Unit.objects.get(id=unit_id)
        serializer.save(unit=unit)


class StudentListView(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        if course_id:
            course = Course.objects.get(id=course_id)
            return course.students.all()
        return CustomUser.objects.none()


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
