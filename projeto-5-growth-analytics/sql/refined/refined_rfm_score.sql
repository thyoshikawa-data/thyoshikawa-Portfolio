CREATE TABLE REFINED_RFM_SCORE AS
SELECT 
    fk_contact,

    NTILE(5) OVER (ORDER BY recency ASC) AS r_score,
    NTILE(5) OVER (ORDER BY frequency DESC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary DESC) AS m_score

FROM REFINED_RFM;
