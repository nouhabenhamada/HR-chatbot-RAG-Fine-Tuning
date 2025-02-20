import pandas as pd
from faker import Faker
import random

# Initialisation de Faker et des données spécifiques
fake = Faker()
Faker.seed(0)

# Listes spécifiques pour les choix
postes = ["Ingénieur", "Chef de projet", "Technicien", "Formateur", "Analyste", "Consultant", "Développeur"]
departements = ["R&D", "Production", "Qualité", "Service Clients", "Finance et Comptabilité", "IT", "Marketing"]
types_contrat = ["CDI", "CDD", "temps partiel"]

# Fonction pour générer un employé
# Fonction pour générer un employé
def generer_employe(poste=None, Type_contrat=None, Salaire=None):
    date_embauche = fake.date_this_decade()
    date_naissance = fake.date_of_birth(minimum_age=22, maximum_age=60)
    quit_date = random.choice([fake.date_between_dates(date_start=date_embauche, date_end=pd.Timestamp.now()), None])
    lastname = fake.last_name()
    firstname = fake.first_name()
    
    # Exclure les contrats à temps partiel pour certains rôles spécifiques
    if poste in ["Manager", "Chef de projet", "Directeur de département"]:
        type_contrat = random.choice([t for t in types_contrat if t != "temps partiel"])
    else:
        type_contrat = Type_contrat if Type_contrat else random.choice(types_contrat)
    
    return {
        "ID Employé": fake.uuid4(),
        "Nom": lastname,
        "Prénom": firstname,
        "Genre": random.choice(["M", "F"]),
        "Date de naissance": date_naissance,
        "Âge": pd.Timestamp.now().year - date_naissance.year,
        "Adresse Email": f"{firstname.lower()}.{lastname.lower()}@xxx.tn",  # Now using the actual firstname and lastname
        "Numéro de téléphone": fake.phone_number(),
        "Adresse postale": fake.address(),
        "Département": random.choice(departements),
        "Date d'embauche": date_embauche,
        "Date de départ": quit_date,
        "Ancienneté (années)": quit_date.year - date_embauche.year if quit_date else pd.Timestamp.now().year - date_embauche.year,
        "Poste": poste if poste else random.choice(postes),
        "Type de contrat": type_contrat,
        "Salaire": Salaire if Salaire else random.randint(16000, 60000),
        "Bonus": random.randint(0, 5000),
        "Congés disponibles (jours)": random.randint(0, 30),
    }


# Générer un sous-ensemble de managers
nb_managers = 10
managers = [generer_employe("Manager") for _ in range(nb_managers)]
for manager in managers:
    manager["Manager"] = "NONE"

# Générer un sous-ensemble de directeurs de département
nb_directeurs_departement = len(departements)
directeurs_departements = [generer_employe(poste="Directeur de département") for _ in range(nb_directeurs_departement)]

# Générer un sous-ensemble de chefs de projet
nb_chefs_projet = 15
chefs_projet = [generer_employe(poste="Chef de projet") for _ in range(nb_chefs_projet)]

# Génération des autres employés
nb_stagiaires = 30
stagiaires = [generer_employe(Type_contrat="stage", Salaire=random.randint(200, 600)) for _ in range(nb_stagiaires)]

# Génération des autres employés avec un manager assigné aléatoirement
nb_employes = 900
employes = [generer_employe() for _ in range(nb_employes)]

# Associer un manager à chaque employé
for employe in employes:
    manager = random.choice(managers)
    employe["Manager"] = f"{manager['Prénom']} {manager['Nom']}"
#ressources humaine
postes_rh = [
    "Responsable du recrutement",
    "Chargé(e) de recrutement",
    "Chargé(e) de marque employeur",
    "Responsable de la gestion des talents",
    "Chargé(e) de formation",
    "Coach interne",
    "Responsable de la paie",
    "Chargé(e) de l’administration du personnel",
    "Gestionnaire de paie",
    "Responsable des relations sociales",
    "Chargé(e) des relations sociales",
    "Gestionnaire des conflits",
    "Responsable de la gestion de la performance",
    "Chargé(e) de l'évaluation des performances",
    "Responsable HSE (Hygiène, Sécurité, Environnement)",
    "Chargé(e) du bien-être au travail",
    "Responsable SIRH",
    "Analyste SIRH",
    "Responsable de la diversité et inclusion",
    "Chargé(e) de la RSE"
]
nb_rh = len(postes_rh)
# Generate employees for the HR department with specified roles from postes_rh list
rh = [generer_employe() for _ in range(nb_rh)]

# Assign each HR employee a specific position, a fixed manager, and department
for i, ressourceHumaine in enumerate(rh):
    ressourceHumaine["Poste"] = postes_rh[i]  # Assign the specific role from postes_rh
    ressourceHumaine["Manager"] = "Kevin Woods"  # Fixed manager name for all HR employees
    ressourceHumaine["Département"] = "Ressources Humaines"  # Consistent department name


# Fusionner tous les employés dans un seul DataFrame
all_employes = managers + directeurs_departements + chefs_projet + employes + stagiaires + rh
df = pd.DataFrame(all_employes)
df.to_csv("employes_xxx_dataset_informations.csv", index=False)

print("Données d'employés générées et sauvegardées dans 'employes_xxx_dataset_informations.csv'")
