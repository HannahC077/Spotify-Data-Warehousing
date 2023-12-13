SET DATEFIRST 7; 
SELECT
    DATEPART(WEEKDAY, dd.Release_Date) AS DayOfWeekNumber,
    DATENAME(WEEKDAY, dd.Release_Date) AS DayOfWeekName,
    AVG(sf.Streams) AS AvgStreams
FROM
    StreamsPopular_Fact sf
JOIN DimDate dd ON sf.Date_Key = dd.Date_Key
GROUP BY
    DATEPART(WEEKDAY, dd.Release_Date),
    DATENAME(WEEKDAY, dd.Release_Date)
ORDER BY
    AvgStreams DESC;
