SELECT df.valence, df.acousticness, df.danceability, df.energy, AVG(sp.Popularity) AS average_popularity
FROM [dbo].DimFeature AS df,
	[dbo].DimTrack as dt
JOIN [dbo].StreamsPopular_Fact AS sp ON df.Feature_Key = sp.Feature_Key
GROUP BY df.valence, df.acousticness, df.danceability, df.energy
HAVING AVG(sp.Popularity) > 90
ORDER BY average_popularity DESC; 
