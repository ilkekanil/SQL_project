SELECT 
P.ProductName,
SUM (OD.Quantity * OD.UnitPrice) as CountNumber
FROM
[Order Details] OD
JOIN 
Products P ON P.ProductID= OD.ProductID
GROUP BY
P.ProductName
ORDER BY 
CountNumber DESC


