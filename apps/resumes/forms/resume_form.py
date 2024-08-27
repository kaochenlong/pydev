from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, EmailInput, Textarea, TextInput

from apps.resumes.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ["name", "email", "introduce", "profile", "online"]
        widgets = {
            "name": TextInput(attrs={"class": "input input-bordered"}),
            "email": EmailInput(attrs={"class": "input input-bordered"}),
            "introduce": TextInput(attrs={"class": "input input-bordered"}),
            "profile": Textarea(
                attrs={"rows": 5, "class": "textarea textarea-bordered"}
            ),
            "online": CheckboxInput(attrs={"class": "toggle"}),
        }
        labels = {
            "name": "姓名",
            "email": "Email",
            "introduce": "簡介",
            "profile": "個人檔案",
            "online": "是否上線",
        }
