from django.contrib.postgres.aggregates import ArrayAgg, StringAgg
from django.db.models import Avg, Min, Max, F, Value as V, CharField, Prefetch
# Create your views here.
from django.db.models.functions import Concat, Cast
from django.views.generic import ListView

from courses.models import Course
from exams.models import Exam, Note
from persons.models import Student


class ExamsList(ListView):
    model = Exam

    def get_queryset(self):
        qs = (
            super().get_queryset()
                .select_related('course')
                .prefetch_related('notes')
                .annotate(avg_note=Avg('notes__note'))
        )
        return qs


class ExamNotesView(ListView):
    model = Note
    template_name = 'exams/note_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        qs = (super().get_queryset().filter(exam_id=self.kwargs['pk'])
            .aggregate(
            avg=Avg('note'),
            min=Min('note'),
            max=Max('note'),
            title=StringAgg('exam__course__title', ',', distinct=True),
            student_notes=ArrayAgg(Concat(F('student__first_name'), V(' '), F('student__last_name'), V(' : '),
                                          Cast(F('note'), CharField())))
        )
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data

