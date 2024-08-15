from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, EmailInput, Textarea, TextInput

from resumes.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ["name", "email", "introduce", "profile", "online"]
        widgets = {
            "profile": Textarea(attrs={"rows": 5}),
        }
        labels = {
            "name": "姓名",
            "email": "Email",
            "introduce": "簡介",
            "profile": "個人檔案",
            "online": "是否上線",
        }
