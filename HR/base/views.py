from django.shortcuts import redirect, render
from django.contrib import messages
import joblib
from .forms import RecruitmentData
from joblib import load
import pickle
import os

model_path = os.path.join('savedModels', 'best_stacking_model.pkl')
try:
    with open(model_path, 'rb') as file:
        model = joblib.load(model_path)    
        print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file {model_path} was not found.")
except pickle.UnpicklingError:
    print(f"Error: The file {model_path} could not be unpickled.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")



def Home (request):
    y_pred=None
    form = RecruitmentData(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            object1= form.save(commit=False)
            prediction_input = [
                        [
                            object1.age,
                            object1.gender,
                            object1.education_level,
                            object1.experience_years,
                            object1.previous_companies,
                            object1.distance_from_company,
                            object1.interview_score,
                            object1.skill_score,
                            object1.personality_score,
                            object1.recruitment_strategy
                        ]
                    ]        
            y_pred = model.predict([[object1.age, object1.gender, object1.education_level, object1.experience_years,
                                         object1.previous_companies, object1.distance_from_company, object1.interview_score,
                                         object1.skill_score, object1.personality_score, object1.recruitment_strategy]])
            y_pred = y_pred[0]
        else:
            messages.error(request, 'An error occurred during registration')
    if y_pred == 0:
        y_pred="NOT HIRED"
    if y_pred == 1:
        y_pred="HIRED"
        
    
        
    


    comtex={"form":form,"y_pred":y_pred}

    return render(request,'home.html',comtex)