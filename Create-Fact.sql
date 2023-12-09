CREATE TABLE StreamsPopular_Fact (
    Date_Key int NOT NULL,
	Track_Key int NOT NULL,
	Feature_Key int NOT NULL,
	Artist_Key int NOT NULL,
    Popularity int NULL,
	Streams bigint NULL,
);
GO

alter table StreamsPopular_Fact add constraint FK_StreamsPopular_Fact_Date
foreign key (Date_Key) references DimDate (Date_Key);

alter table StreamsPopular_Fact add constraint FK_StreamsPopular_Fact_Track
foreign key (Track_Key) references DimTrack (Track_Key);

alter table StreamsPopular_Fact add constraint FK_StreamsPopular_Fact_Feature
foreign key (Feature_Key) references DimFeature (Feature_Key);

alter table StreamsPopular_Fact add constraint FK_StreamsPopular_Fact_Artist
foreign key (Artist_Key) references DimArtist (Artist_Key);