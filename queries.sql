
-- 📈 ANALYSE DU ROI ET DU CAC PAR CANAL MARKETING
SELECT 
    ms.canal_marketing,
    SUM(DISTINCT ms.budget_depense) AS total_budget_depense,
    COUNT(cc.client_id) AS total_clients_acquis,
    
    -- 1. Calcul du CAC (Coût d'Acquisition Client = Budget / Nombre de clients)
    ROUND(SUM(DISTINCT ms.budget_depense) / COUNT(cc.client_id), 2) AS CAC,
    
    SUM(cc.montant_achat) AS total_chiffre_affaires,
    
    -- 2. Calcul du ROI en % ( (Revenue - Spend) / Spend * 100 )
    ROUND(
        ((SUM(cc.montant_achat) - SUM(DISTINCT ms.budget_depense)) / SUM(DISTINCT ms.budget_depense)) * 100, 
        2
    ) AS ROI_pourcentage
FROM 
    marketing_spend ms
LEFT JOIN 
    customer_conversions cc ON ms.campagne_id = cc.campagne_id
GROUP BY 
    ms.canal_marketing
ORDER BY 
    ROI_pourcentage DESC;
    -- 🧪 EXTRACTION POUR L'A/B TESTING (VERSION A VS VERSION B)
SELECT 
    ms.canal_marketing,
    cc.version_banniere,
    COUNT(cc.client_id) AS nombre_conversions,
    ROUND(AVG(cc.montant_achat), 2) AS panier_moyen
FROM 
    customer_conversions cc
JOIN 
    marketing_spend ms ON cc.campagne_id = ms.campagne_id
GROUP BY 
    ms.canal_marketing, cc.version_banniere
ORDER BY 
    ms.canal_marketing, cc.version_banniere;