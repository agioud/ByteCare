from django import forms

class PredictionForm(forms.Form):
    age = forms.FloatField(label="Âge", min_value=0)
    
    genre = forms.ChoiceField(
        label="Genre", 
        choices=[(0, "Homme"), (1, "Femme")])
    
    niveau_etudes = forms.ChoiceField(
        label="Niveau d'études",
        choices=[
            (0, "Aucun"),
            (1, "Lycée"),
            (2, "Licence"),
            (3, "Supérieur")
        ]
    )
    smoking = forms.ChoiceField(
        label="Fumeur", 
        choices=[(0, "Non"), (1, "Oui")])
    
    alcool = forms.FloatField(
        label="Consommation d'alcool par semaine", 
        min_value=0, max_value=20)
    
    activites_phy = forms.FloatField(
        label="Heures de sport par semaine", 
        min_value=0, max_value=10)
    
    diet = forms.FloatField(
        label="Qualité du régime alimentaire (0-10)", 
        min_value=0, max_value=10)
    
    sleep = forms.FloatField(
        label="Qualité du sommeil (4-10)", 
        min_value=4, max_value=10)
    
    family_hist = forms.ChoiceField(
        label="Antécédents familiaux", 
        choices=[(0, "Non"), (1, "Oui")])
    
    cardio_dis = forms.ChoiceField(
        label="Problèmes cardio-vasculaires", 
        choices=[(0, "Non"), (1, "Oui")])
    
    head_inju = forms.ChoiceField(
        label="Blessures à la tête", 
        choices=[(0, "Non"), (1, "Oui")])
    
    cholesterol = forms.FloatField(
        label="Taux de cholestérol (mg/dL)", 
        required=False)
    
    mmse = forms.FloatField(
        label="Résultat MMSE (0-30)", 
        required=False)
    
    memo_complain = forms.ChoiceField(
        label="Plaintes de mémoire", 
        choices=[(0, "Non"), (1, "Oui")])
    
    confu = forms.ChoiceField(
        label="Confusion", 
        choices=[(0, "Non"), (1, "Oui")])
    
    disorient = forms.ChoiceField(
        label="Désorientation", 
        choices=[(0, "Non"), (1, "Oui")])
    
    perso_change = forms.ChoiceField(
        label="Trouble de personnalité", 
        choices=[(0, "Non"), (1, "Oui")])
    
    diff_tasks = forms.ChoiceField(
        label="Difficultés dans les tâches", 
        choices=[(0, "Non"), (1, "Oui")])
    
    forget_ful = forms.ChoiceField(
        label="Pertes de mémoire", 
        choices=[(0, "Non"), (1, "Oui")])
