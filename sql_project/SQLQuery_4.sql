SELECT 
    C.CustomerID,
    C.CompanyName,
    COUNT(O.OrderID) AS TotalOrders,
    SUM(OD.Quantity * OD.UnitPrice ) AS TotalSpent,
    MAX(O.OrderDate) AS LastOrderDate
FROM 
    Customers C
JOIN 
    Orders O ON C.CustomerID = O.CustomerID
JOIN 
    [Order Details] OD ON O.OrderID = OD.OrderID
GROUP BY 
    C.CustomerID, C.CompanyName
ORDER BY 
    TotalOrders DESC;
