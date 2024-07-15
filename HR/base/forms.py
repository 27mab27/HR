from django.forms import ModelForm
from .models import RecruitmentData


class RecruitmentData(ModelForm):
    class Meta:
        model = RecruitmentData
        fields = '__all__'
