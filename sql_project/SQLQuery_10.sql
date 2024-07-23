SELECT 
S.CompanyName,
S.SupplierID,
COUNT (P.SupplierID) as SalesAmount
FROM
Products P
JOIN 
Suppliers S ON S.SupplierID= P.SupplierID
GROUP BY
S.CompanyName, S.SupplierID
ORDER BY 
SalesAmount DESC