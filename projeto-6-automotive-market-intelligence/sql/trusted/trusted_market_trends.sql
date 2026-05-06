CREATE TABLE TRUSTED_MARKET_TRENDS AS
SELECT 
    trend_date,
    UPPER(category) AS category,
    search_term,
    interest_score,
    load_date
FROM RAW_MARKET_TRENDS
WHERE trend_date IS NOT NULL
  AND interest_score IS NOT NULL;
