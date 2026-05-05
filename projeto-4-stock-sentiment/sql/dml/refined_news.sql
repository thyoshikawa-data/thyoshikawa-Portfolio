SELECT 
    ticker,
    COUNT(*) AS total_noticias,
    SUM(CASE WHEN snippet LIKE '%alta%' THEN 1 ELSE 0 END) AS positivas,
    SUM(CASE WHEN snippet LIKE '%queda%' THEN 1 ELSE 0 END) AS negativas
FROM RAW_NEWS_STOCKS
GROUP BY ticker;
