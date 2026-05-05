CREATE TABLE REFINED_COHORT AS
SELECT 
    fk_contact,
    TRUNC(MIN(date_purchase), 'MM') AS cohort_month,
    COUNT(*) AS total_compras
FROM TRUSTED_TRANSACTIONS
GROUP BY fk_contact;
