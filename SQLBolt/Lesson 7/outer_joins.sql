SELECT DISTINCT building_name FROM buildings
INNER JOIN employees
ON buildings.building_name = employees.building;

SELECT * FROM buildings;

SELECT DISTINCT building_name, role FROM buildings
LEFT JOIN employees
ON buildings.building_name = employees.building;


