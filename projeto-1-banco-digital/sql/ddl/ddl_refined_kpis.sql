-- Camada REFINED
CREATE TABLE REFINED_SELIC_MENSAL AS
SELECT 
    TRUNC(data, 'MM') AS mes,
    AVG(valor) AS media_selic,
    MIN(valor) AS min_selic,
    MAX(valor) AS max_selic,
    COUNT(*) AS qtd_registros
FROM TRUSTED_SELIC
GROUP BY TRUNC(data, 'MM')
ORDER BY mes;
