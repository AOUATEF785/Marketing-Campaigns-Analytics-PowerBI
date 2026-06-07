# Advanced Marketing Campaigns Analytics Dashboard (Power BI)

## Project Overview

This project delivers an interactive and intelligent business analytics dashboard built using **Power BI Desktop**. It integrates marketing spend data with customer conversion metrics to evaluate the performance of different acquisition channels (Facebook Ads, Google Ads, and Influencers) and perform fine-grained A/B testing analysis on creative banners.

## Key Business Insights

- **Influencers RoI:** Influencers are the most lucrative channel, generating the highest Revenue (Chiffre d'Affaires) and Peak Conversions with an optimized budget.
- **Google Ads Underperformance:** Despite receiving equal budget distribution, Google Ads significantly underperformed with the lowest customer acquisition volume.
- **A/B Banner Test:** `Version_B` slightly outperforms `Version_A` (51.48% vs 48.52% of total conversions), providing guidance for future creative assets.

## Dashboard Preview

![Dashboard Preview](images/image_3ba710.png)

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
