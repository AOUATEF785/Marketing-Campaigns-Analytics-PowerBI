import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.proportion import proportions_ztest

# 1. Chargement des données générées
df_conversions = pd.read_csv('customer_conversions.csv')
df_spend = pd.read_csv('marketing_spend.csv')

print("--- ANALYSE EXPLORATOIRE DES BANNIÈRES ---")
# Grouper par version de bannière pour voir les résultats bruts
summary = df_conversions.groupby('version_banniere').agg(
    total_conversions=('client_id', 'count'),
    panier_moyen=('montant_achat', 'mean')
).reset_index()
print(summary)

print("\n --- TEST STATISTIQUE A/B TESTING (Z-TEST) ---")
# Pour faire un test de proportion, on va simuler le nombre total de clics/impressions
# Disons que la Version A a eu 50 000 impressions et la Version B 50 000 impressions
clicks_A = 50000
clicks_B = 50000

conv_A = df_conversions[df_conversions['version_banniere'] == 'Version_A'].shape[0]
conv_B = df_conversions[df_conversions['version_banniere'] == 'Version_B'].shape[0]

successes = np.array([conv_A, conv_B])
samples = np.array([clicks_A, clicks_B])

# Calcul du Z-test et de la p-value
stat, p_value = proportions_ztest(successes, samples, alternative='two-sided')

print(f"Conversions Version A : {conv_A} (Taux: {conv_A/clicks_A:.3%})")
print(f"Conversions Version B : {conv_B} (Taux: {conv_B/clicks_B:.3%})")
print(f"p-value statistique : {p_value:.4f}")

# Conclusion au seuil alpha = 5%
alpha = 0.05
if p_value < alpha:
    print("\nCONCLUSION BUSINESS : La différence est statistiquement SIGNIFICATIVE ! On déploie la Version B à 100%.")
else:
    print("\nCONCLUSION BUSINESS : Pas de différence significative. L'écart est dû au hasard.")