CREATE TABLE TRUSTED_ROUTES AS
SELECT 
    route_dep,
    COUNT(*) AS total_viagens,
    AVG(gmv_success) AS ticket_medio
FROM TRUSTED_TRANSACTIONS
GROUP BY route_dep;
