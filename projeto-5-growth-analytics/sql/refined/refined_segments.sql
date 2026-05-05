CREATE TABLE REFINED_SEGMENTS AS
SELECT 
    r.fk_contact,
    r.recency,
    r.frequency,
    r.monetary,
    s.r_score,
    s.f_score,
    s.m_score,

    CASE 
        WHEN s.r_score >= 4 AND s.f_score >= 4 AND s.m_score >= 4 THEN 'Campeões'
        WHEN s.m_score >= 4 THEN 'VIP'
        WHEN s.r_score <= 2 THEN 'Em risco'
        WHEN s.f_score <= 2 THEN 'Hibernando'
        ELSE 'Regulares'
    END AS segment

FROM REFINED_RFM r
JOIN REFINED_RFM_SCORE s 
ON r.fk_contact = s.fk_contact;
