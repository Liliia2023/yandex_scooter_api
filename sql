/*1*/
SELECT co.login,
       COUNT(os."courierId") AS in_delivery
FROM "Orders" AS os
JOIN "Couriers" AS co 
    ON co.id = os."courierId"
WHERE os."inDelivery" = true
GROUP BY co.login;

/*2*/

SELECT track, 
    CASE
      WHEN finished = true THEN 2
      WHEN cancelled = true THEN -1
      WHEN "inDelivery" = true THEN 1
      ELSE 0 
    END AS status
FROM "Orders"
ORDER BY status;
