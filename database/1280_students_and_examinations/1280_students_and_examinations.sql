WITH exam_counts AS (
    SELECT
        student_id,
        subject_name,
        COUNT(*) AS attended_exams
    FROM
        Examinations
    GROUP BY
        student_id, subject_name
)
SELECT
    stu.student_id,
    stu.student_name,
    sub.subject_name,
    COALESCE(ec.attended_exams, 0) AS attended_exams
FROM
    Students stu
CROSS JOIN
    Subjects sub
LEFT JOIN
    exam_counts ec
    ON stu.student_id = ec.student_id
    AND sub.subject_name = ec.subject_name
ORDER BY
    stu.student_id, sub.subject_name;
