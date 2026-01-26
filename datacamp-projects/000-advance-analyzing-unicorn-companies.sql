-- Date: 2026-01-24
-- Name: 000-advance-analyzing-unicorn-companies
-- Problem: Top 3 Industries for Unicorns (DataCamp Project)
-- Insight: Modular CTEs to isolate ranking logic from metric calculation.
-- Complexity: O(N log N) due to sorting in the Top Industries CTE (most expensive operation)
-- Datacamp project link: https://app.datacamp.com/learn/projects/1531


WITH CTE_UNICORNS AS (
	SELECT
		i.industry AS industry,
		EXTRACT(YEAR FROM d.date_joined) AS year,
		count(distinct(c.company_id)) AS num_unicorns,
		AVG(f.valuation)/1000000000 AS avg_val_raw
	FROM companies c
	INNER JOIN dates d ON c.company_id = d.company_id
	INNER JOIN funding f ON c.company_id = f.company_id
	INNER JOIN industries i ON c.company_id = i.company_id
	WHERE EXTRACT(YEAR FROM d.date_joined) IN (2019, 2020, 2021)
	GROUP BY i.industry, EXTRACT(YEAR FROM d.date_joined)
),
CTE_TOP_INDUSTRIES AS (
	SELECT
		industry,
	 	SUM(num_unicorns) AS total_unicorns
	FROM CTE_UNICORNS
	GROUP BY industry
	ORDER BY total_unicorns DESC
	LIMIT 3
)
SELECT 
  U.industry, 
  U.year, 
  U.num_unicorns, 
  ROUND(U.avg_val_raw,2) AS average_valuation_billions
FROM CTE_UNICORNS U
INNER JOIN CTE_TOP_INDUSTRIES TI ON U.industry = TI.industry
ORDER BY year DESC, num_unicorns DESC
