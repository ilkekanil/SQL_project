SELECT 
O.EmployeeID,
E.LastName,
E.FirstName,
COUNT (O.EmployeeID) as CountNumber
FROM
Orders O
JOIN 
Employees E ON E.EmployeeID= O.EmployeeID
GROUP BY
E.LastName, E.FirstName, O.EmployeeID
ORDER BY 
CountNumber DESC