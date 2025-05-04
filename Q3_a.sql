-- SQL Query to retrieve the names and salaries of employees in the Engineering department who earn more than 50,000
SELECT name, salary
FROM employees
WHERE department = 'Engineering' AND salary > 50000;
