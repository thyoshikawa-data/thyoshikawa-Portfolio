CREATE TABLE REFINED_MARKET_SHARE AS
SELECT 
    category,
    search_term,

    ROUND(
        AVG(interest_score), 2
    ) AS avg_interest_score

FROM TRUSTED_MARKET_TRENDS
GROUP BY category, search_term;
