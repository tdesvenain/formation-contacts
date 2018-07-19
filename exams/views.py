from django.contrib.postgres.aggregates import ArrayAgg, StringAgg
from django.db.models import Avg, Min, Max, F, Value as V, CharField
# Create your views here.
from django.db.models.functions import Concat, Cast
from django.db.models.query_utils import Q
from django.views.generic import ListView

from courses.models import Course
from exams.models import Exam, Note


class ExamsList(ListView):
    model = Exam

    def get_queryset(self):
        qs = (
            super().get_queryset()
                .select_related('course')
                .annotate(
                avg_note=Avg('notes__note'),
                array_note=ArrayAgg('notes__note'))
        )
        return qs


class CoursesList(ListView):
    model = Course
    template_name = 'exams/course_list.html'

    def get_queryset(self):
        qs = super().get_queryset().annotate(avg_course_note=Avg('exams__notes__note'))
        return qs


class ExamNotesView(ListView):
    model = Note
    template_name = 'exams/note_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        qs = (super().get_queryset()
            .filter(exam_id=self.kwargs['pk'])
            .aggregate(
            avg=Avg('note'),
            min=Min('note'),
            max=Max('note'),
            # extreme !! :)
            title=StringAgg('exam__course__title', ',', distinct=True),
            # extreme !! :)
            student_notes=ArrayAgg(
                Concat(
                    F('student__first_name'),
                    V(' '),
                    F('student__last_name'),
                    V(' : '),
                    Cast(F('note'), CharField()))),
        )
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data


class StudentCourses(ListView):
    model = Course
    slug_field = 'student_id'
    template_name = 'exams/student_courses.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(
            avg_note=Avg(
                'exams__notes__note',
                filter=Q(exams__notes__student_id=self.kwargs['pk']),
            ),
        )
