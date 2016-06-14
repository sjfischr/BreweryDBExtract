#!/usr/local/bin/python
import sys
import requests
import traceback

import pyodbc

def refresh_breweries():

    cnxn = pyodbc.connect([ENTER YOUR DB CONNECTION STRING])

    url = "http://api.brewerydb.com/v2/breweries/?key=[KEY]&withLocations=Y"

    #initial load
    r = requests.get(url).json()
    num_pages = r['numberOfPages']

    #brewery_ids = []
    for i in range(1, num_pages):
        r = requests.get(url, params={'p': i}).json()
        data = r
        breweries = data['data']
        for brewery in breweries:
            #set the sql
            braddsql = 'exec sp_AddDBBrewery ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'

            #brewery_ids.append(brewery['id'])
            brid = brewery['id']
            brnm = brewery['name']
            try:
                brdesc = ''
                brshnm = brewery['nameShortDisplay']
            except:
                pass
            brcreatedt = brewery['createDate']
            try:
                brdesc = ''
                brdesc = brewery['description']
            except:
                pass
            try:
                brest = 0
                brest = brewery['established']
            except:
                pass
            try:
                brorganic = ''
                brorganic = brewery['isOrganic']
            except:
                pass
            try:
                #setting images
                image = ''
                images = brewery['images']
                for image in images:
                    brlarge = images['large']
            except:
                pass
            brstatus = brewery['status']
            brstatusDisp = brewery['statusDisplay']
            brupdatedt = brewery['updateDate']
            try:
                brwebsite = ''
                brwebsite = brewery['website']
            except:
                pass
            dbcursor = cnxn.cursor()
            # param order:
            # @pBreweryID, @pBreweryNM, @pBreweryDesc, @pBreweryEstYear, @pBreweryImage,
            # @pBreweryOrganic, @pBreweryNMShort, @pBreweryStatus, @pBreweryStatusDisp, @pBreweryWebsite,
            # @pBreweryCreateDt, @pBreweryUpdatedDt
            try:
                dbcursor.execute(braddsql, brid, brnm, brshnm, brdesc, brcreatedt, brupdatedt, brest, brlarge, brstatus, brstatusDisp, brorganic, brwebsite)
                #commit and close
                dbcursor.commit()
            except:
                print 'Error in processing page ' + str(i) + ': Adding ' + brid + ' - ' + brnm
                traceback.print_exception
                pass

            #print url
            print 'Page ' + str(i) + ': Adding ' + brid + ' - ' + brnm
            try:
                locations = brewery['locations']
                for brlocation in locations: #for each location
                    countryiso = brlocation['countryIsoCode']
                    loccreatedt = brlocation['createDate']
                    locid = brlocation['id'] #unique ID
                    locinplanning = brlocation['inPlanning']
                    locisclosed = brlocation['isClosed']
                    locisprimary = brlocation['isPrimary']
                    loclat = brlocation['latitude']
                    loclon = brlocation['longitude']
                    try:
                        loclocality = ''
                        loclocality = brlocation['locality']
                    except:
                        pass
                    locloctype = brlocation['locationType']
                    locloctypeDisp = brlocation['locationTypeDisplay']
                    locname = brlocation['name']
                    locopenPublic = brlocation['openToPublic']
                    try:
                        locphone = ''
                        locphone = brlocation['phone']
                    except:
                        pass
                    try:
                        locpostalcd = ''
                        locpostalcd = brlocation['postalCode']
                    except:
                        pass
                    try:
                        locregion = ''
                        locregion = brlocation['region']
                    except:
                        pass
                    locstatus = brlocation['status']
                    locstatusDisp = brlocation['statusDisplay']
                    locaddress = brlocation['streetAddress']
                    locupdatedt = brlocation['updateDate']
                    try:
                        locwebsite = ''
                        locwebsite = brlocation['website']
                    except:
                        pass

                    #call the location SP
                    locaddsql = 'exec sp_AddDBLocation ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
                    dbcursor.execute(locaddsql, countryiso, loccreatedt, locid, locinplanning, locisclosed, locisprimary, loclat, loclon, loclocality, locloctype, locloctypeDisp, locname, locopenPublic, locphone, locpostalcd, locregion, locstatus, locstatusDisp, locaddress, locupdatedt, locaddress, brid)
                    dbcursor.commit()
            except:
                pass
    dbcursor.close #close the cursor

def refresh_hops():
    cnxn = pyodbc.connect([DB CONNECTION])

    #Get the breweries

    #For each brewery, get the beers
    url = "http://api.brewerydb.com/v2/hops/?key=[KEY]"
    dbcursor = cnxn.cursor()

    #initial load
    r = requests.get(url).json()
    num_pages = r['numberOfPages']

    for i in range(1, num_pages):
        r = requests.get(url, params={'p': i}).json()
        data = r
        hops = data['data']
        for hop in hops:
            id = hop['id']
            name = hop['name']
            try:
                description = ''
                description = hop['description']
            except:
                pass
            try:
                countryOfOrigin = ''
                countryOfOrigin = hop['countryOfOrigin']
            except:
                pass
            try:
                alphaAcidMin = 0.0
                alphaAcidMin = hop['alphaAcidMin']
            except:
                pass
            try:
                alphaAcidMax = 0.0
                alphaAcidMax = hop['alphaAcidMax']
            except:
                pass
            try:
                betaAcidMin = 0.0
                betaAcidMin = hop['betaAcidMin']
            except:
                pass
            try:
                betaAcidMax = 0.0
                betaAcidMax = hop['betaAcidMax']
            except:
                pass
            try:
                humuleneMin = 0.0
                humuleneMin = hop['humuleneMin']
            except:
                pass
            try:
                humuleneMax = 0.0
                humuleneMax = hop['humuleneMax']
            except:
                pass
            try:
                caryophylleneMin = 0.0
                caryophylleneMin = hop['caryophylleneMin']
            except:
                pass
            try:
                caryophylleneMax = 0.0
                caryophylleneMax = hop['caryophylleneMax']
            except:
                pass
            try:
                cohumuloneMin = 0.0
                cohumuloneMin = hop['cohumuloneMin']
            except:
                pass
            try:
                cohumuloneMax = 0.0
                cohumuloneMax = hop['cohumuloneMax']
            except:
                pass
            try:
                myrceneMin = 0.0
                myrceneMin = hop['myrceneMin']
            except:
                pass
            try:
                myrceneMax = 0.0
                myrceneMax = hop['myrceneMax']
            except:
                pass
            try:
                farneseneMin = 0.0
                farneseneMin = hop['farneseneMin']
            except:
                pass
            try:
                farneseneMax = 0.0
                farneseneMax = hop['farneseneMax']
            except:
                pass
            try:
                isNoble = ''
                isNoble = hop['isNoble']
            except:
                pass
            try:
                forBittering = ''
                forBittering = hop['forBittering']
            except:
                pass
            try:
                forFlavor = ''
                forFlavor = hop['forFlavor']
            except:
                pass
            try:
                forAroma = ''
                forAroma = hop['forAroma']
            except:
                pass

    #insert the hop records
            #call the location SP
            #try:
            hopaddsql = 'exec sp_AddDBHop ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
            dbcursor.execute(hopaddsql, id, name, description, countryOfOrigin, alphaAcidMin, alphaAcidMax, betaAcidMin, betaAcidMax, humuleneMin, humuleneMax, caryophylleneMin, caryophylleneMax, cohumuloneMin, cohumuloneMax, myrceneMin, myrceneMax, farneseneMin, farneseneMax, isNoble, forBittering, forFlavor, forAroma)
            dbcursor.commit()
            #except:
            #    print 'Error in processing page ' + str(i) + ': Adding ' + str(id) + ' - ' + name
            #    traceback.print_exception
            #    pass
            dbcursor.close #close the cursor


def converttoFloat(inputNum):
    try:
        flnum = float(inputNum)
    except:
        flnum = 0.0

def refresh_beers():

    #Get the breweries

    cnxn = pyodbc.connect([DB CONNECTION])
    dbcursor = cnxn.cursor()
    getbrewsql = 'exec sp_GetDBBreweries'
    dbcursor.execute(getbrewsql)
    resultsarr = dbcursor.fetchall()

    for result in resultsarr:
        #For each brewery, get the beers
        brewery = result[0].strip()
        url = "http://api.brewerydb.com/v2/brewery/" + brewery + "/beers/?key=[KEY]"
        #initial load
        data = requests.get(url).json()
        #num_pages = r['numberOfPages']

        try: #make certain the brewery has beer!
            beers = data['data']
        except: #there are no beers
            pass

        for beer in beers:
            id = beer['id']
            name = beer['name']
            try:
                abv = beer['abv']
            except:
                abv = 0
                pass
            try:
                ibu = beer['ibu']
            except:
                ibu = 0
                pass
            try:
                glasswareId = beer['glasswareId']
            except:
                glasswareId = 0
                pass
            try:
                srmId = beer['srmId']
            except:
                srmId = 0
                pass
            try:
                availableId = 0
                availableId = beer['availableId']
            except:
                pass
            try:
                styleId = beer['styleId']
            except:
                styleId = 0
                pass
            try:
                isOrganic = beer['isOrganic']
            except:
                isOrganic = 'NA'
                pass
            try:
                hasLabels = beer['hasLabels']
            except:
                hasLabels = 'NA'
                pass
            try:
                year = beer['year']
            except:
                year = 0
                pass
            try:
                status = beer['status']
            except:
                pass
            createDate = beer['createDate']
            try:
                updateDate = beer['updateDate']
            except:
                updateDate = '1900-01-01'
                pass

            beeraddsql = 'exec sp_AddDBBeer ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
            dbcursor.execute(beeraddsql, id, name, abv, ibu, glasswareId, srmId, availableId, styleId, isOrganic, hasLabels, year, status, createDate, updateDate, brewery)
            dbcursor.commit()
            print 'Adding brewery ' + brewery + ' beer ' + name

refresh_beers()
