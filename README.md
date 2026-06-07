# Advanced Marketing Campaigns Analytics Dashboard (Power BI)

## Project Overview

This project delivers an interactive and intelligent business analytics dashboard built using **Power BI Desktop**. It integrates marketing spend data with customer conversion metrics to evaluate the performance of different acquisition channels (Facebook Ads, Google Ads, and Influencers) and perform fine-grained A/B testing analysis on creative banners.

## Key Business Insights

- **Influencers RoI:** Influencers are the most lucrative channel, generating the highest Revenue (Chiffre d'Affaires) and Peak Conversions with an optimized budget.
- **Google Ads Underperformance:** Despite receiving equal budget distribution, Google Ads significantly underperformed with the lowest customer acquisition volume.
- **A/B Banner Test:** `Version_B` slightly outperforms `Version_A` (51.48% vs 48.52% of total conversions), providing guidance for future creative assets.

## Dashboard Preview

![Dashboard Preview](Dashboard_Marketing.png)
## Advanced Features & DAX Measures Built

- **Data Modeling:** Established automated 1-to-many structural relationships between spend records and customer conversion datasets.
- **Advanced KPIs:** Engineered custom DAX metrics for deep business tracking:
  - **ROAS (Return on Ad Spend):** `ROAS = DIVIDE(SUM(customer_conversions[montant_achat]); SUM(marketing_spend[budget_depense]))`
  - **CAC (Customer Acquisition Cost):** `CAC = DIVIDE(SUM(marketing_spend[budget_depense]); COUNT(customer_conversions[client_id]))`
- **Interactive Visuals:** Built a high-level **Scatter Chart (Nuage de points)** for strategic performance positioning alongside cross-filtering matrices and trend analysis over time.

## Repository Structure

- `Dashboard_Marketing.pbix` - Core Power BI Desktop project file.
- `marketing_spend.csv` - Detailed marketing budget allocation by campaign and channel.
- `customer_conversions.csv` - Granular customer transactions, purchase amounts, and banner versions.
- `images/` - Contains asset screenshot (`image_3ba710.png`).


##Éxplication fine dyal les Visuels (image_3ba710.png)
Les Top KPIs (Les Cartes completely l-fau9)
•	Nombre de client_id (1,455K): Hada huwa l-3addad total d les conversions li jbaow les campagnes completely (1,455 conversion s7i7a).
•	Somme de budget_depense (183K): L-Budget total global li t-khsser 3la les 3 d les canaux marketing.
•	ROAS (80.28): Hada un indicateur intelligent! Kay-byen blli l-Return on Ad Spend global t9riban raw profitable (kull dirham khssrnaha jbat lina l-khir, khsusa b l-9owa d les influenceurs).
•	CAC (125.75): Coût d'Acquisition Client. Kull client jdid t-khsser 3lih f l-Moyen t9riban 125.75 DH bach d-dar la conversion.
Graphique Anneau (A/B Test d les Bannières)
•	Chnou kay-byen: Répartition d les conversions 3la 7sab la version d la bannière.
•	Insight: L-performance dyalhom m-9arba bzzaf! Version_B jab51.48% (749 conversions) w Version_A jab48.52% (706 conversions). Ya3ni Version_B la3ba 7ssen chwya walakin t-9der t-9ol blli les deux versions khddamin properly.
Le Treemap (Somme de montant_achat par canal)
•	Chnou kay-byen: L-7ajm d l-flouss (Chiffre d'Affaires) li d-khlat kull canal marketing.
•	Insight: L-carré l-kbyr complete b l-azraq huwa dyal Influenceurs. Hada huwa l-Malik d l-Dashboard! Huwa li jbaov akhar 3addad d les ventes, f l-wselt m-tabe3 b Facebook Ads, w completely l-te7t Google Ads sghira bzzaf.
Graphique Combiné Ligne/Courbe (Budget vs Conversions)
•	Chnou kay-byen: Comparison direct bin l-Budget li t-khsser (Ligne violette flat) m3a l-3addad d les conversions (Ligne turquoise).
•	Insight: Looki l-farq kbyr! Google Ads m7tot fiha نفس budget dyal l-Influenceurs walakin l-conversions dyalha habtin completely l l-ard (te7t 300). f l-wa9t li l-Influenceurs t-popeyav l-fau9 7da 800 conversion b نفس l-budget!
Nuage de points / Scatter Chart (L-Analyse Intelligente)
•	Chnou kay-byen: Had l-graphe l-fau9 f l-limen kay-byen l-Positionnement Stratégique.
•	Insight: La bulle d l-Influenceurs (orange/bleu completely l-fau9 f l-limen) hiya la plus haute complete, ya3ni 3ndha le plus haut Chiffre d'Affaires m3a budget optimisé. Google Ads w Facebook Ads b9au l-te7t block complete horizontalement.


