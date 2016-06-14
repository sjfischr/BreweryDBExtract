USE [beer_analysis]
GO

/****** Object:  StoredProcedure [dbo].[sp_AddDBBeer]    Script Date: 6/13/2016 9:21:50 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

========================
CREATE PROCEDURE [dbo].[sp_AddDBBeer] 

	(@pbeer_id nchar(10),
	@pname varchar(500),
	@pabv decimal(18, 2),
	@pibu decimal(18, 2),
	@pglasswareId int,
	@psrmId int,
	@pavailableId int,
	@pstyleId int,
	@pisOrganic char(2),
	@phasLabels char(2),
	@pyear int,
	@pstatus char(10),
	@pcreateDate datetime,
	@pupdateDate datetime,
	@pbrewery_id char(10)
	)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- look for brewery
			DECLARE @brewery_id int
			SET @brewery_id = NULL

			SET @brewery_id = 
				(SELECT id 
				FROM tbl_db_brewery 
				WHERE brewery_id = @pbrewery_id)


	--insert the beer
	INSERT INTO tbl_db_beers(
	beer_id,
	name,
	abv,
	ibu,
	glasswareId,
	srmId,
	availableId,
	styleId,
	isOrganic,
	hasLabels,
	[year],
	[status],
	createDate,
	updateDate,
	brewery_id)
	SELECT
	@pbeer_id,
	@pname,
	@pabv,
	@pibu,
	@pglasswareId,
	@psrmId,
	@pavailableId,
	@pstyleId,
	@pisOrganic,
	@phasLabels,
	@pyear,
	@pstatus,
	@pcreateDate,
	@pupdateDate,
	@brewery_id

	--finally, update the brewery table with a sys update record
	UPDATE tbl_db_brewery
	SET refresh_dt = GETDATE() 
	WHERE id = @brewery_id
		
	
END


GO


