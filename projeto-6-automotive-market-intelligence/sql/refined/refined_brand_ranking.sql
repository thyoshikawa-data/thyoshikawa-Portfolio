CREATE TABLE REFINED_BRAND_RANKING AS
SELECT 
    search_term,
    category,

    ROUND(
        AVG(interest_score),
        2
    ) AS avg_interest,

    RANK() OVER (
        PARTITION BY category
        ORDER BY AVG(interest_score) DESC
    ) AS ranking

FROM TRUSTED_MARKET_TRENDS
GROUP BY search_term, category;
