-- RAW → TRUSTED
INSERT INTO TRUSTED_NOTICIAS
SELECT 
    LOWER(titulo),
    link,
    LOWER(snippet),
    data_carga
FROM RAW_NOTICIAS;

-- TRUSTED → REFINED
INSERT INTO REFINED_NOTICIAS
SELECT 
    CASE 
        WHEN snippet LIKE '%selic%' THEN 'SELIC'
        WHEN snippet LIKE '%inflação%' THEN 'INFLACAO'
        WHEN snippet LIKE '%juros%' THEN 'JUROS'
        ELSE 'OUTROS'
    END,
    COUNT(*)
FROM TRUSTED_NOTICIAS
GROUP BY 
    CASE 
        WHEN snippet LIKE '%selic%' THEN 'SELIC'
        WHEN snippet LIKE '%inflação%' THEN 'INFLACAO'
        WHEN snippet LIKE '%juros%' THEN 'JUROS'
        ELSE 'OUTROS'
    END;
