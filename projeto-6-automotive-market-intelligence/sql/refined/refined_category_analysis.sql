CREATE TABLE REFINED_CATEGORY_ANALYSIS AS
SELECT 
    category,

    ROUND(
        AVG(interest_score),
        2
    ) AS avg_interest,

    MAX(interest_score) AS peak_interest,
    MIN(interest_score) AS min_interest

FROM TRUSTED_MARKET_TRENDS
GROUP BY category;
