-- Write your PostgreSQL query statement below

SELECT t1.id
FROM weather t1
JOIN weather t2
  ON t1.recordDate = t2.recordDate + 1
WHERE t1.temperature > t2.temperature;
