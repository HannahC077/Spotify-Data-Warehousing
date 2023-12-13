SELECT dt.explicit, AVG(sp.Popularity) AS average_popularity, SUM(sp.Streams) AS total_streams
FROM [dbo].DimTrack AS dt
JOIN [dbo].StreamsPopular_Fact AS sp ON dt.Track_Key = sp.Track_Key
GROUP BY dt.explicit;