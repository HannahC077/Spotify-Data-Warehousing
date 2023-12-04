    CREATE TABLE DimDate (
        Date_Key int NOT NULL IDENTITY(1,1),
        Release_Date date NOT NULL,
        Date_ID nvarchar(255) NOT NULL,  --surrogate key
        -- Month_Number int NOT NULL,
        -- Month_Name nvarchar(50) NOT NULL,
        -- Day int NOT NULL,
        -- Quarter int NOT NULL,
        Year int NOT NULL
    );
    GO

    CREATE TABLE DimTrack (
        Track_Key int NOT NULL IDENTITY(1,1),
        Track_ID nvarchar(255) NOT NULL,
        Title nvarchar(255) NOT NULL,
        Track_Number int NOT NULL,
        Track_Type nvarchar(255) NOT NULL,
        Explicit smallint NOT NULL,
        Duration_ms int NOT NULL,
        Album_Type nvarchar(255) NOT NULL,
        Album_Total_Tracks int NOT NULL,
        Active_Ind smallint NOT NULL DEFAULT 1
    );
    GO

    CREATE TABLE DimFeature (
        Feature_Key int NOT NULL IDENTITY(1,1),
        Feature_ID nvarchar(255) NOT NULL, --surrogate key
        Valence numeric(38, 30) NOT NULL,
        Acousticness numeric(38, 30) NOT NULL,
        Danceability numeric(38, 30) NOT NULL,
        Energy numeric(38, 30) NOT NULL,
        Instrumentalness numeric(38, 30) NOT NULL,
        KeyFeature int NOT NULL, 
        Liveness numeric(38, 30) NOT NULL,
        Loudness numeric(38, 30) NOT NULL,
        Mode smallint NOT NULL,
        Speechiness numeric(38, 30) NOT NULL,
        Tempo numeric(38, 30) NOT NULL
    );
    GO

    CREATE TABLE DimArtist (
        Artist_Key int NOT NULL IDENTITY(1,1),
        Artist_ID nvarchar(255) NOT NULL,
        Artist_Name nvarchar(255) NOT NULL,
        Active_Ind smallint NOT NULL DEFAULT 1
    );
    GO

    alter table DimDate add primary key (Date_Key);
    alter table DimTrack add primary key (Track_Key);
    alter table DimFeature add primary key (Feature_Key);
    alter table DimArtist add primary key (Artist_Key);
    GO