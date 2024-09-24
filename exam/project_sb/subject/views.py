from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, LessonType
from .forms import SubjectForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseForbidden

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
            subject = form.save(commit=False)
            subject.author = request.user
            subject.save()
            messages.success(request, "Предмет було успішно додано.")
            return redirect('subject_list') # POST-REDIRECT-GET
        else:
            messages.error(request, "Будь ласка, перевірте коректність даних")
    else:
        form = SubjectForm()
    return render(request, 'subject/subject_form.html', {'form': form})

# Оновлення існуючого предмета
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if subject.author != request.user:
        return HttpResponseForbidden("Ви не можете редагувати цей запис.")
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, "Предмет було успішно відредаговано.")
            return redirect('subject_detail', pk=subject.pk) # POST-REDIRECT-GET
        else:
            messages.error(request, "Будь ласка, перевірте коректність даних")
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subject/subject_form.html', {'form': form})

# Видалення предмета з підтвердженням
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if subject.author != request.user:
        return HttpResponseForbidden("Ви не можете видалити цей запис.")
    if request.method == 'POST':
        subject.delete()
        messages.success(request, "Предмет було успішно видалено.")
        return redirect('subject_list') # POST-REDIRECT-GET
    return render(request, 'subject/subject_confirm_delete.html', {'subject': subject})
