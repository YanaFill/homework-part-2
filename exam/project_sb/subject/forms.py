from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'teacher', 'lesson_type', 'control', 'specialty', 'semester', 'image']

    # валідація семестру
    def clean_semester(self):
        semester = self.cleaned_data.get('semester')
        if semester < 1 or semester > 12:
            raise forms.ValidationError("Семестр повинен бути від 1 до 12.")
        return semester