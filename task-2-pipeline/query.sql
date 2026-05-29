SELECT
    temperature_category,
    AVG(max_temperature) AS avg_max_temperature,
    AVG(min_temperature) AS avg_min_temperature
FROM weather_dataset.weather_data
GROUP BY temperature_category
ORDER BY avg_max_temperature DESC;
