from django.db import models
from django.forms import ValidationError

class RecruitmentData(models.Model):
    age = models.IntegerField()
    gender = models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])
    education_level = models.IntegerField(choices=[(1, 'diploma'), (2, "Bachelor's"),(3,"Master's"),(4,"PhD")])
    experience_years = models.IntegerField()
    previous_companies = models.IntegerField()
    distance_from_company = models.FloatField()
    interview_score = models.IntegerField()
    skill_score = models.IntegerField()
    personality_score = models.IntegerField()
    recruitment_strategy = models.IntegerField(choices=[(1, 'Aggressive'), (2, 'Moderate'),(3,'Conservative')])


