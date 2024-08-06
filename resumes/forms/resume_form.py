from django.forms import ModelForm
from resumes.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            "name",
            "email",
            "introduce",
            "profile",
            "online",
        ]
