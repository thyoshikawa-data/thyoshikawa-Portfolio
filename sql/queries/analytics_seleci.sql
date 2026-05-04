-- Evolução mensal da SELIC

SELECT 
    TO_CHAR(mes, 'YYYY-MM') AS mes,
    media_selic,
    min_selic,
    max_selic,
    qtd_registros
FROM REFINED_SELIC_MENSAL
ORDER BY mes;
