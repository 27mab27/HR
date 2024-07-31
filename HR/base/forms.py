from django import forms
from django.forms import ModelForm, ChoiceField
from .models import RecruitmentData   


class RecruitmentData(ModelForm):
    GENDER_CHOICES = [('', ''), (0, 'Male'), (1, 'Female')]
    EDUCATION_LEVEL_CHOICES = [('', ''), (1, 'diploma'), (2, "Bachelor's"), (3, "Master's"), (4, "PhD")]
    RECRUITMENT_STRATEGY_CHOICES = [('', ''), (1, 'Aggressive'), (2, 'Moderate'), (3, 'Conservative')]

    gender = ChoiceField(choices=GENDER_CHOICES, required=True)
    education_level = ChoiceField(choices=EDUCATION_LEVEL_CHOICES, required=True)
    recruitment_strategy = ChoiceField(choices=RECRUITMENT_STRATEGY_CHOICES, required=True)



    class Meta:
        model = RecruitmentData
        exclude = ['hire']
        fields = '__all__'


    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and not (18 <= age <= 70):
            raise forms.ValidationError('Age must be between 18 and 70.')
        return age

    def clean_experience_years(self):
        experience_years = self.cleaned_data.get('experience_years')
        if experience_years is not None and not (0 <= experience_years <= 20):
            raise forms.ValidationError('Experience years must be between 0 and 20.')
        return experience_years

    def clean_previous_companies(self):
        previous_companies = self.cleaned_data.get('previous_companies')
        if previous_companies is not None and not (0 <= previous_companies <= 100):
            raise forms.ValidationError('Previous companies must be between 0 and 100.')
        return previous_companies

    def clean_distance_from_company(self):
        distance_from_company = self.cleaned_data.get('distance_from_company')
        if distance_from_company is not None and not (1 <= distance_from_company <= 60):
            raise forms.ValidationError('Distance from company must be between 1 and 60 kilometers.')
        return distance_from_company

    def clean_interview_score(self):
        interview_score = self.cleaned_data.get('interview_score')
        if interview_score is not None and not (0 <= interview_score <= 100):
            raise forms.ValidationError('Interview score must be between 0 and 100.')
        return interview_score

    def clean_skill_score(self):
        skill_score = self.cleaned_data.get('skill_score')
        if skill_score is not None and not (0 <= skill_score <= 100):
            raise forms.ValidationError('Skill score must be between 0 and 100.')
        return skill_score

    def clean_personality_score(self):
        personality_score = self.cleaned_data.get('personality_score')
        if personality_score is not None and not (0 <= personality_score <= 100):
            raise forms.ValidationError('Personality score must be between 0 and 100.')
        return personality_score

