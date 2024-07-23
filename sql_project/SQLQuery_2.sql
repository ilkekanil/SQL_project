SELECT 
    E.EmployeeID,
    E.FirstName,
    E.LastName,
    COUNT(O.OrderID) AS TotalOrders,
    SUM(OD.Quantity) AS TotalQuantitySold,
    SUM(OD.Quantity * OD.UnitPrice) AS TotalRevenue
FROM 
    Employees E
JOIN 
    Orders O ON E.EmployeeID = O.EmployeeID
JOIN 
    [Order Details] OD ON O.OrderID = OD.OrderID
GROUP BY 
    E.EmployeeID, E.FirstName, E.LastName
ORDER BY 
    TotalOrders DESC;
