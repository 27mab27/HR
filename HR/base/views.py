from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RecruitmentData
from joblib import load
import pickle
import os

model_path = os.path.join('savedModels', 'LR_model_imb.pkl')
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file {model_path} was not found.")
except pickle.UnpicklingError:
    print(f"Error: The file {model_path} could not be unpickled.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")



def Home (request):
    form = RecruitmentData()
    if request.method == 'POST':
        if form.is_valid():
            object1 = form.save(commit=False)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')



    comtex={"form":form}

    return render(request,'home.html',comtex)