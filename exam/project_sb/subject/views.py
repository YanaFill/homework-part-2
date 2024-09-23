from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Subject, LessonType
from .forms import SubjectForm
from django.urls import reverse_lazy
from django.db.models import Q

# Список предметів + пошук
def subject_list(request):
    query = request.GET.get('q')
    if query:
        subjects = Subject.objects.filter(Q(name__icontains=query) | Q(teacher__icontains=query))
    else:
        subjects = Subject.objects.all()
    return render(request, 'subject/subject_list.html', {'subjects': subjects})

# Деталі предмета
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subject/subject_detail.html', {'subject': subject})

# Створення нового предмета
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject/subject_form.html', {'form': form})

# Оновлення існуючого предмета
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_detail', pk=subject.pk)
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subject/subject_form.html', {'form': form})

# Видалення предмета з підтвердженням
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subject/subject_confirm_delete.html', {'subject': subject})
