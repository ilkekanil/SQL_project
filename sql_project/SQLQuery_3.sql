SELECT 
    YEAR(O.OrderDate) AS Year,
    SUM(OD.Quantity) AS TotalQuantitySold,
    SUM(OD.Quantity * OD.UnitPrice) AS TotalRevenue
FROM 
    Orders O
JOIN 
    [Order Details] OD ON O.OrderID = OD.OrderID
GROUP BY 
    YEAR(O.OrderDate)
ORDER BY 
    Year;
