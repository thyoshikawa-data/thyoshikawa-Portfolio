SELECT 
    ticker,
    data,
    close,
    close - LAG(close) OVER (PARTITION BY ticker ORDER BY data) AS variacao
FROM TRUSTED_STOCKS;
