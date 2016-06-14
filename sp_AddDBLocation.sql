USE [beer_analysis]
GO

/****** Object:  StoredProcedure [dbo].[sp_AddDBLocation]    Script Date: 6/13/2016 9:22:07 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[sp_AddDBLocation] 
	(@pcountry_nm as varchar(255),
	@pcreate_dt  as datetime,
	@plocation_id  as nchar(10),
	@pplanning_fg  as char(2),
	@pclosed_fg  as char(2),
	@pprimary_fg  as char(2),
	@plat  as numeric (18,10),
	@plon  numeric (18,10),
	@plocality_nm varchar (255),
	@plocation_type varchar (50),
	@plocation_type_nm  varchar (100),
	@plocation_nm  varchar (255),
	@popentopublic_fg  char(2),
	@pphone_no  varchar (50),
	@ppostal_cd  varchar (50),
	@pregion_nm  varchar (50),
	@pstatus  varchar (50),
	@pstatus_disp  varchar (50),
	@pstreet_addr  varchar (255),
	@pupdate_dt  datetime,
	@pwebsite_url  varchar (255),
	@pbrewery_id  char(10))
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- look for location
	DECLARE @loc_chk int
	SET @loc_chk = NULL

	SET @loc_chk = 
		(SELECT id 
		FROM tbl_db_location
		WHERE location_id = @plocation_id) 

	IF (@loc_chk IS NULL) --if no location exists, we can insert the record

		BEGIN
			
			    -- Look for location ID
			DECLARE @brewery_id int
			SET @brewery_id = NULL

			SET @brewery_id = 
				(SELECT id 
				FROM tbl_db_brewery 
				WHERE brewery_id = @pbrewery_id)

				INSERT INTO tbl_db_location([country_nm]
										  ,[create_dt]
										  ,[location_id]
										  ,[planning_fg]
										  ,[closed_fg]
										  ,[primary_fg]
										  ,[lat]
										  ,[lon]
										  ,[locality_nm]
										  ,[location_type]
										  ,[location_type_nm]
										  ,[location_nm]
										  ,[opentopublic_fg]
										  ,[phone_no]
										  ,[postal_cd]
										  ,[region_nm]
										  ,[status]
										  ,[status_disp]
										  ,[street_addr]
										  ,[update_dt]
										  ,[website_url]
										  ,[brewery_id])
				SELECT 
			   @pcountry_nm
			  ,@pcreate_dt
			  ,@plocation_id
			  ,CASE 
				WHEN @pplanning_fg = 'Y' THEN 1 
				ELSE 0
			  END
			  ,CASE 
				WHEN @pclosed_fg = 'Y' THEN 1 
				ELSE 0
			  END
			  ,CASE 
				WHEN @pprimary_fg = 'Y' THEN 1 
				ELSE 0
			  END
			  ,@plat
			  ,@plon
			  ,@plocality_nm
			  ,@plocation_type
			  ,@plocation_type_nm
			  ,@plocation_nm
			  ,CASE 
				WHEN @popentopublic_fg = 'Y' THEN 1 
				ELSE 0
			  END
			  ,@pphone_no
			  ,@ppostal_cd
			  ,@pregion_nm
			  ,@pstatus
			  ,@pstatus_disp
			  ,@pstreet_addr
			  ,@pupdate_dt
			  ,@pwebsite_url
			  ,@brewery_id
		
		END


	
END

GO


