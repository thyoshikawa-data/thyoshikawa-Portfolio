CREATE TABLE REFINED_KPIS AS
SELECT 
    COUNT(DISTINCT fk_contact) AS total_clientes,
    COUNT(*) AS total_pedidos,
    SUM(total_tickets_quantity_success) AS total_passagens,
    SUM(gmv_success) AS receita_total,
    AVG(gmv_success) AS ticket_medio,

    ROUND(
        SUM(CASE WHEN is_return = 1 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2
    ) AS pct_ida_volta

FROM TRUSTED_TRANSACTIONS;
