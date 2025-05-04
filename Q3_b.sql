-- SQL query to find the average salary of employees for each department, sorted in descending order of average salary
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;
