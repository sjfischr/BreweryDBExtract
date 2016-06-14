USE [beer_analysis]
GO

/****** Object:  StoredProcedure [dbo].[sp_AddDBHop]    Script Date: 6/13/2016 9:22:01 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[sp_AddDBHop] 
	@phop_id int,
	@pname varchar(255),
	@pdescription varchar(max),
	@pcountryOfOrigin varchar(255),
	@palphaAcidMin numeric,
	@palphaAcidMax numeric,
	@pbetaAcidMin numeric,
	@pbetaAcidMax numeric,
	@phumuleneMin numeric,
	@phumuleneMax numeric,
	@pcaryophylleneMin numeric,
	@pcaryophylleneMax numeric,
	@pcohumuloneMin numeric,
	@pcohumuloneMax numeric,
	@pmyrceneMin numeric,
	@pmyrceneMax numeric,
	@pfarneseneMin numeric,
	@pfarneseneMax numeric,
	@pisNoble char(2),
	@pforBittering char(2),
	@pforFlavor char(2),
	@pforAroma char(2)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

		--1. See if hop already exists
	DECLARE @hop_chk int
	SET @hop_chk = 0

	SET @hop_chk = 
		(SELECT id 
		FROM tbl_db_hops 
		WHERE hop_id = @phop_id)

	IF (@hop_chk IS NULL) --If we don't have it already, insert new hop record


    INSERT INTO tbl_db_hops
	(hop_id 
	,name
	,description
	,countryOfOrigin
	,alphaAcidMin
	,alphaAcidMax
	,betaAcidMin
	,betaAcidMax
	,humuleneMin
	,humuleneMax
	,caryophylleneMin
	,caryophylleneMax
	,cohumuloneMin
	,cohumuloneMax
	,myrceneMin
	,myrceneMax
	,farneseneMin
	,farneseneMax
	,isNoble
	,forBittering
	,forFlavor
	,forAroma)
	SELECT
	@phop_id
	,@pname
	,@pdescription
	,@pcountryOfOrigin
	,@palphaAcidMin
	,@palphaAcidMax
	,@pbetaAcidMin
	,@pbetaAcidMax
	,@phumuleneMin
	,@phumuleneMax
	,@pcaryophylleneMin
	,@pcaryophylleneMax
	,@pcohumuloneMin
	,@pcohumuloneMax
	,@pmyrceneMin
	,@pmyrceneMax
	,@pfarneseneMin
	,@pfarneseneMax
	,@pisNoble
	,@pforBittering
	,@pforFlavor
	,@pforAroma
END

GO


