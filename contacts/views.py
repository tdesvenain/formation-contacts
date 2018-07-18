from django.http import HttpResponse


def home(request):
    return HttpResponse('<a href="persons">Personnes</a><br/><a href="exams">Examens</a>')
