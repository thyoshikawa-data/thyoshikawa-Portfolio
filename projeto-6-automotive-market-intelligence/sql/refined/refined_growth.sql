CREATE TABLE REFINED_GROWTH AS
SELECT 
    search_term,
    category,

    MIN(interest_score) AS min_score,
    MAX(interest_score) AS max_score,

    ROUND(
        ((MAX(interest_score) - MIN(interest_score))
        / NULLIF(MIN(interest_score),0)) * 100,
        2
    ) AS growth_percent

FROM TRUSTED_MARKET_TRENDS
GROUP BY search_term, category;
