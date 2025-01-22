import os
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

# Récupérer le chemin du fichier CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'predictor', 'static', 'alzheimers_disease_data.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'predictor', 'models', 'model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'predictor', 'models', 'scaler.pkl')

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(CSV_PATH)

# Charger le modèle et le scaler
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

# Fonction pour afficher le formulaire et calculer la probabilité
def calculate_probability(request):
    if request.method == 'POST':
        # Collecte des données depuis le formulaire
        age = float(request.POST['age'])
        genre = float(request.POST['genre'])
        niveau_etudes = float(request.POST['niveau_etudes'])
        smoking = float(request.POST['smoking'])
        alcool = float(request.POST['alcool'])
        activites_phy = float(request.POST['activites_phy'])
        diet = float(request.POST['diet'])
        sleep = float(request.POST['sleep'])
        family_hist = float(request.POST['family_hist'])
        cardio_dis = float(request.POST['cardio_dis'])
        head_inju = float(request.POST['head_inju'])
        cholesterol = float(request.POST['cholesterol'])
        
        if cholesterol == 0:
            cholesterol = round(df['CholesterolTotal'][(df['CholesterolTotal'] > 150) & (df['CholesterolTotal'] < 300)].mean(), 2)
        else:
            cholesterol = float(request.POST['cholesterol'])
        
        mmse = float(request.POST['mmse'])
        if mmse == 0:
            mmse = round(df['MMSE'].mean(), 2)
        else:
            mmse = float(request.POST['mmse'])

        memo_complain = float(request.POST['memo_complain'])
        confu = float(request.POST['confu'])
        disorient = float(request.POST['disorient'])
        perso_change = float(request.POST['perso_change'])
        diff_tasks = float(request.POST['diff_tasks'])
        forget_ful = float(request.POST['forget_ful'])

        # Préparer les données de l'utilisateur
        user_data = np.array([[age, genre, niveau_etudes, smoking, alcool, activites_phy, diet, sleep, family_hist,
                               cardio_dis, head_inju, cholesterol, mmse, memo_complain, confu, disorient, perso_change,
                               diff_tasks, forget_ful]])

        # Normaliser les données
        user_data_scaled = scaler.transform(user_data)

        # Prédire la probabilité
        probability = model.predict_proba(user_data_scaled)[0, 1]  # Probabilité d'être positif (classe 1)

        # Afficher le résultat
        return render(request, 'predictor/result.html', {'probability': probability * 100})

    # Si la méthode est GET, afficher le formulaire
    return render(request, 'predictor/form.html')
