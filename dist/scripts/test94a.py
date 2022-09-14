#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "Verify the server supports SQ-016 - What has changed since a specified time ( well )",
     reference =  "6.6.5.17",
     reference_text = "All WITSML servers that support the function MUST support these queries",
     functionality_required =   ["WMLS_AddToStore:well" , 
                                 "WMLS_DeleteFromStore:well",
                                 "WMLS_UpdateInStore:well",
                                 "WMLS_GetFromStore:changeLog" ],
     data_schemas = ["1.4.1.0", "1.4.1.1"],         
                                 
    )
#############
# TEST BODY #
#############

log('Setup start')

set("well_name", "Energistics Certification Well Test94a")

set("well_xml", """<wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
  <well>
    <name>$well_name$</name>
    <nameLegal>Company Legal Name</nameLegal>
    <numLicense>Company License Number</numLicense>
    <numGovt>Govt-Number</numGovt>
    <dTimLicense>2001-05-15T13:20:00Z</dTimLicense>
    <field>Big Field</field>
    <country>US</country>
    <state>TX</state>
    <county>Montgomery</county>
    <region>Region Name</region>
    <district>District Name</district>
    <block>Block Name</block>
    <timeZone>-06:00</timeZone>
    <operator>Operating Company</operator>
    <operatorDiv>Division Name</operatorDiv>
    <pcInterest uom="%">65</pcInterest>
    <numAPI>123-543-987AZ</numAPI>
    <statusWell>drilling</statusWell>
    <purposeWell>exploration</purposeWell>
    <dTimSpud>2001-05-31T08:15:00Z</dTimSpud>
    <dTimPa>2001-07-15T15:30:00Z</dTimPa>
    <wellheadElevation uom="ft">500</wellheadElevation>
    <wellDatum uid="KB">
      <name>Kelly Bushing</name>
      <code>KB</code>
      <elevation uom="ft" datum="SL">78.5</elevation>
    </wellDatum>
    <wellDatum uid="SL">
      <name>Sea Level</name>
      <code>SL</code>
      <datumName namingSystem="EPSG" code="5106">Caspian Sea</datumName>
    </wellDatum>
    <groundElevation uom="ft">250</groundElevation>
    <waterDepth uom="ft">520</waterDepth>
    <wellLocation uid="loc-1">
      <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
      <easting uom="m">425353.84</easting>
      <northing uom="m">6623785.69</northing>
      <description>Location of well surface point in projected system.</description>
    </wellLocation>
    <referencePoint uid="SRP1">
      <name>Slot Bay Centre</name>
      <type>Site Reference Point</type>
      <location uid="loc-1">
        <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
        <easting uom="m">425366.47</easting>
        <northing uom="m">6623781.95</northing>
      </location>
      <location uid="loc-2">
        <wellCRS uidRef="localWell1">WellOneWSP</wellCRS>
        <localX uom="m">12.63</localX>
        <localY uom="m">-3.74</localY>
        <description>Location of the Site Reference Point with respect to the well surface point</description>
      </location>
    </referencePoint>
    <referencePoint uid="WRP2">
      <name>Sea Bed</name>
      <type>Well Reference Point</type>
      <elevation uom="ft" datum="SL">-118.4</elevation>
      <measuredDepth uom="ft" datum="KB">173.09</measuredDepth>
      <location uid="loc-1">
        <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
        <easting uom="m">425353.84</easting>
        <northing uom="m">6623785.69</northing>
      </location>
      <location uid="loc-2">
        <wellCRS uidRef="geog1">ED50</wellCRS>
        <latitude uom="dega">59.743844</latitude>
        <longitude uom="dega">1.67198083</longitude>
      </location>
    </referencePoint>
    <wellCRS uid="geog1">
      <name>ED50</name>
      <geodeticCRS uidRef="4230">4230</geodeticCRS>
      <description>ED50 system with EPSG code 4230.</description>
    </wellCRS>
    <wellCRS uid="proj1">
      <name>ED50 / UTM Zone 31N</name>
      <mapProjectionCRS uidRef="23031">ED50 / UTM Zone 31N</mapProjectionCRS>
    </wellCRS>
    <wellCRS uid="localWell1">
      <name>WellOneWSP</name>
      <localCRS>
        <usesWellAsOrigin>true</usesWellAsOrigin>
        <yAxisAzimuth uom="dega" northDirection="grid north">0</yAxisAzimuth>
        <xRotationCounterClockwise>false</xRotationCounterClockwise>
      </localCRS>
    </wellCRS>
    <commonData>
      <itemState>plan</itemState>
      <comments>These are the comments associated with the Well data object.</comments>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </well>
 </wells>"""
)
  

#############
# TEST BODY #
#############  

log('Script procedure start')

# 1. Add the object

WMLS_AddToStore(WMLTYPEIN_WELL, "$well_xml$")  
check_ReturnValue_Success()
partial_success("WMLS_AddToStore succeeded well")

set('wellUid', get_SuppMsgOut_uid_String())
log_variable('wellUid')
new_object_created(WMLTYPEIN_WELL, "$wellUid$")

# 2. Get ChangeLogs
#get time for 1 hour ago.
set('dTim', timestamp_subtract_seconds(now(), 3600))
WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<changeLogs xmlns="http://www.witsml.org/schemas/1series"  version="$server_schema_version$">
                                                <changeLog> 
                                                    <commonData>
                                                        <dTimLastChange>$dTim$</dTimLastChange>
                                                    </commonData>
                                                </changeLog>
                                        </changeLogs>
                                    """, OptionsIn = { 'returnElements':'latest-change-only' })  

check_ReturnValue_Success()
partial_success("GetFromStore changeLogs after Add succeeded ")

#check to see that the return is valid
check_XMLout_ValidWriteSchema()
partial_success("changeLogs returned are write schema valid ")

#check to see that no changeHistory's exist
check_XMLout_ElementNotIncluded('/changeLogs/changeLog/changeHistory')
partial_success("No changeHistory in changeLogs exist, succeed ")

#find added well's lastChangeType
check_XMLout_ElementValue('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well"]/lastChangeType', 'add')  
partial_success("well changeLog with only Add in lastChangeType succeed ")

# get add dTimLastChange
check_XMLout_ElementIncluded('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well" and lastChangeType="add"]/commonData/dTimLastChange')
partial_success("well changeLog with only add has dTimLastChange succeed ")
addDTim = get_XMLout_Element_String('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well" and lastChangeType="add"]/commonData/dTimLastChange')
set('dTim', addDTim)

# 3 Update the Well
WMLS_UpdateInStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                   <wells xmlns="http://www.witsml.org/schemas/1series"  version="$server_schema_version$">
                                      <well uid="$wellUid$">
                                            <field>Big Field2</field>
                                      </well>
                                   </wells>
                                """)  
check_ReturnValue_Success()
partial_success("UpdateInStore well succeeded ")

#4 ChangeLog for well is update
WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<changeLogs xmlns="http://www.witsml.org/schemas/1series"  version="$server_schema_version$">
                                                <changeLog> 
                                                    <commonData>
                                                        <dTimLastChange>$dTim$</dTimLastChange>
                                                    </commonData>
                                                </changeLog>
                                        </changeLogs>
                                    """, OptionsIn = { 'returnElements':'latest-change-only' })  

check_ReturnValue_Success()
partial_success("GetFromStore changeLogs after Update succeeded ")

#check to see that the return is valid
check_XMLout_ValidWriteSchema()
partial_success("changeLogs returned are write schema valid ")

#check to see that no changeHistory's exist
check_XMLout_ElementNotIncluded('/changeLogs/changeLog/changeHistory')
partial_success("No changeHistory in changeLogs exist, succeed ")

#find update well's lastChangeType
check_XMLout_ElementValue('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well"]/lastChangeType', 'update') 
partial_success("well changeLog with only update in lastChangeType succeed ")

# get update dTimLastChange
check_XMLout_ElementIncluded('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well" and lastChangeType="update"]/commonData/dTimLastChange')
partial_success("well changeLog with only update has dTimLastChange succeed ")
updateDTim = get_XMLout_Element_String('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well" and lastChangeType="update"]/commonData/dTimLastChange')

check_timestamp_Greaterthan(updateDTim, get('dTim'))
partial_success("well changeLog with only update dTimLastChange > changeLog with Add succeed ")
set('dTim', updateDTim)

#5 Delete Well
WMLS_DeleteFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                   <wells xmlns="http://www.witsml.org/schemas/1series"  version="$server_schema_version$">
                                      <well  uid="$wellUid$">
                                      </well>
                                   </wells>
                                """)  
check_ReturnValue_Success()
partial_success("DeleteFromStore well succeeded ")

#6 ChangeLog for well in Delete
WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<changeLogs xmlns="http://www.witsml.org/schemas/1series"  version="$server_schema_version$">
                                                <changeLog> 
                                                    <commonData>
                                                        <dTimLastChange>$dTim$</dTimLastChange>
                                                    </commonData>
                                                </changeLog>
                                        </changeLogs>
                                    """, OptionsIn = { 'returnElements':'latest-change-only' })  

check_ReturnValue_Success()
partial_success("GetFromStore changeLogs after Delete succeeded ")

#check to see that the return is valid
check_XMLout_ValidWriteSchema()
partial_success("changeLogs returned are write schema valid ")

#check to see that no changeHistory's exist
check_XMLout_ElementNotIncluded('/changeLogs/changeLog/changeHistory')
partial_success("No changeHistory in changeLogs exist, succeed ")

#find update well's lastChangeType
check_XMLout_ElementValue('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well"]/lastChangeType', 'delete')
partial_success("well changeLog with only delete in lastChangeType succeed ")

# get delete dTimLastChange
check_XMLout_ElementIncluded('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well" and lastChangeType="delete"]/commonData/dTimLastChange')
partial_success("well changeLog with only delete has dTimLastChange succeed ")
deleteDTim = get_XMLout_Element_String('/changeLogs/changeLog[@uidObject="$wellUid$" and objectType="well" and lastChangeType="delete"]/commonData/dTimLastChange')

check_timestamp_Greaterthan(deleteDTim, get('dTim'))
partial_success("well changeLog with only delete dTimLastChange > changeLog with update succeed ")



log('Script procedure end')

success()
