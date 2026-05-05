CREATE TABLE REFINED_ROUTES AS
SELECT 
    route_dep,
    COUNT(*) AS total_viagens,
    AVG(gmv_success) AS ticket_medio,
    SUM(gmv_success) AS receita_total
FROM TRUSTED_TRANSACTIONS
GROUP BY route_dep;
