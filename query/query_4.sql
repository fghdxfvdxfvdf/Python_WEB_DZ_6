-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT AVG(gr.grade) AS avg_grade 
FROM grades gr;
