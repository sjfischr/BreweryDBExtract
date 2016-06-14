USE [beer_analysis]
GO

/****** Object:  StoredProcedure [dbo].[sp_AddDBBrewery]    Script Date: 6/13/2016 9:21:55 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_AddDBBrewery] 
	@pBreweryID nchar(10),
	@pBreweryNM varchar(255),
	@pBreweryNMShort varchar(255),
	@pBreweryDesc varchar(max),
	@pBreweryCreateDt datetime,
	@pBreweryUpdatedDt datetime,
	@pBreweryEstYear int,
	@pBreweryImage varchar(255),
	@pBreweryStatus varchar(50),
	@pBreweryStatusDisp varchar(50),
	@pBreweryOrganic char(20),
	@pBreweryWebsite varchar(255)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

	--1. See if brewery already exists
	DECLARE @brewery_chk int
	SET @brewery_chk = 0

	SET @brewery_chk = 
		(SELECT id 
		FROM tbl_db_brewery 
		WHERE brewery_id = @pBreweryID)

	IF (@brewery_chk IS NULL) --If we don't have it already, insert new brewery record
		BEGIN
			INSERT INTO tbl_db_brewery(brewery_id, brewery_nm, br_description, established_yr, br_image, isOrganic, brewery_nm_short, br_status, statusDisplay, website, created_dt, modified_dt)
			SELECT @pBreweryID, @pBreweryNM, @pBreweryDesc, @pBreweryEstYear, @pBreweryImage, @pBreweryOrganic, @pBreweryNMShort, @pBreweryStatus, @pBreweryStatusDisp, @pBreweryWebsite, @pBreweryCreateDt, @pBreweryUpdatedDt
		END	

END

GO


