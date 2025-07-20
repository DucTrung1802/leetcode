WITH confirmationRateTable AS
(
    SELECT
        user_id,
        ROUND(
            COUNT(*) FILTER (WHERE action = 'confirmed')::DECIMAL
            / COUNT(*), 
            2
        ) AS confirmation_rate
    FROM
        Confirmations
    GROUP BY
        user_id
)

SELECT sig.user_id, COALESCE(con.confirmation_rate, 0) AS confirmation_rate 
FROM Signups sig
LEFT JOIN confirmationRateTable con
ON sig.user_id = con.user_id

