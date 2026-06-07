 
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

canaux = ['Facebook Ads', 'Google Ads', 'Influenceurs']
campagnes_data = []
campagne_id = 101

for canal in canaux:
    for i in range(4):
        budget = np.random.randint(5000, 25000)
        campagnes_data.append({
            'campagne_id': campagne_id,
            'canal_marketing': canal,
            'nom_campagne': f"Campagne_{canal[:3]}_{i+1}",
            'budget_depense': budget
        })
        campagne_id += 1

df_spend = pd.DataFrame(campagnes_data)
df_spend.to_csv('marketing_spend.csv', index=False)
print(" Fichier 'marketing_spend.csv' genere avec succes !")

n_conversions = 15000
conversions_data = []
campagnes_ids = df_spend['campagne_id'].tolist()
start_date = datetime(2026, 1, 1)

for i in range(n_conversions):
    c_id = np.random.choice(campagnes_ids)
    canal = df_spend[df_spend['campagne_id'] == c_id]['canal_marketing'].values[0]
    
    if canal == 'Influenceurs':
        montant = np.random.exponential(scale=120) + 20
        statut_achat = np.random.choice([1, 0], p=[0.15, 0.85])
    elif canal == 'Facebook Ads':
        montant = np.random.exponential(scale=70) + 15
        statut_achat = np.random.choice([1, 0], p=[0.08, 0.92])
    else:
        montant = np.random.exponential(scale=85) + 10
        statut_achat = np.random.choice([1, 0], p=[0.05, 0.95])
        
    if statut_achat == 1:
        date_conversion = start_date + timedelta(days=int(np.random.randint(0, 90)))
        conversions_data.append({
            'client_id': f"CUST_{10000 + i}",
            'campagne_id': c_id,
            'date_conversion': date_conversion.strftime('%Y-%m-%d'),
            'montant_achat': round(montant, 2),
            'version_banniere': np.random.choice(['Version_A', 'Version_B'], p=[0.5, 0.5])
        })

df_conversions = pd.DataFrame(conversions_data)
df_conversions.to_csv('customer_conversions.csv', index=False)
print(f"Fichier 'customer_conversions.csv' genere avec {len(df_conversions)} ventes !")