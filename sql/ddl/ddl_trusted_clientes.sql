-- Camada TRUSTED
CREATE TABLE TRUSTED_SELIC AS
SELECT 
    TO_DATE(data_raw, 'YYYY-MM-DD') AS data,
    TO_NUMBER(valor_raw) AS valor,
    data_carga
FROM RAW_SELIC
WHERE valor_raw IS NOT NULL;
