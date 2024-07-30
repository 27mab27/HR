from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm 
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

def LoginPage(request):
    page = 'Login'
    if request.user.is_authenticated:
        return redirect('home')
    

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
    
    context = {'page':page}
    return render(request, 'login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        

    return render(request, 'login_register.html', {'form': form})


def Home (request):
    y_pred=None
    form = RecruitmentData()
    if request.method == 'POST':
        form = RecruitmentData(request.POST)
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
            
    if y_pred == 0:
        y_pred="NOT HIRED"
    if y_pred == 1:
        y_pred="HIRED"
        
    
        
    


    comtex={"form":form,"y_pred":y_pred}

    return render(request,'home.html',comtex)

def root (request):
    return render(request,'root.html')


