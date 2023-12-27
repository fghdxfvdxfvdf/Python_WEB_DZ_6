-- Знайти які курси які читає певний викладач.

SELECT d.name AS course_name, t.fullname AS teacher_name
FROM disciplines d
JOIN teachers t ON d.teacher_id = t.id;
