#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "Data Test - Compare newly added to retrieved Log",
     reference =  "",
     reference_text = "",
     functionality_required =   ["WMLS_GetFromStore:log",
                                 "WMLS_AddToStore:log" ],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

  
#########
# SETUP #
#########

log('Setup start')

log("Retrieving well/wellbore name")

# get dataset well 1
WMLS_GetFromStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="utf-8"?>
                                   <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                     <wellbore uidWell="$server_w1_uid$" uid="$server_w1_wb1_uid$">
                                     </wellbore>
                                   </wellbores>
                                """, OptionsIn={'returnElements':'id-only'}) 
check_ReturnValue_Success()
check_XMLout_NumberOfObjects(1)
set('well_name', get_XMLout_Element_String('nameWell'))
set("wellbore_name", get_XMLout_Element_String('name'))
partial_success("retrieved well/wellbore name")
  
  
#############
# TEST BODY #
#############

log('Script procedure start')


# 1. Load the object

set("log_name","Energistics Certification log Test30")

set('log_xml',"""
<logs xmlns="http://www.witsml.org/schemas/1series" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="$server_schema_version$">
    <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$">
        <nameWell>$well_name$</nameWell>
        <nameWellbore>$wellbore_name$</nameWellbore>
        <name>$log_name$</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Baker Hughes INTEQ</serviceCompany>
        <runNumber>12</runNumber>
        <creationDate>2001-06-18T13:20:00.000Z</creationDate>
        <description>Drilling Data Log</description>
        <indexType>measured depth</indexType>
        <startIndex uom="m">499</startIndex>
        <endIndex uom="m">509.01</endIndex>
        <stepIncrement uom="m">0</stepIncrement>
        <direction>increasing</direction>
        <indexCurve>Mdepth</indexCurve>
        <nullValue>-999.25</nullValue>
        <logParam index="1" name="MRES" uom="ohm.m" description="Mud Resistivity" uid="lp-1">1.25</logParam>
        <logParam index="2" name="BDIA" uom="in" description="Bit Diameter" uid="lp-2">12.25</logParam>
        <logCurveInfo uid="lci-1">
            <mnemonic>Mdepth</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>m</unit>
            <mnemAlias>md</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Measured depth</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-2">
            <mnemonic>Vdepth</mnemonic>
            <classWitsml>TVD of hole</classWitsml>
            <unit>m</unit>
            <mnemAlias>tvd</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Vertical depth</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-3">
            <mnemonic>Bit Dist</mnemonic>
            <classWitsml>measured depth of DST bottom</classWitsml>
            <unit>m</unit>
            <mnemAlias>distBit</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Distance drilled by bit</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-4">
            <mnemonic>TQ on btm</mnemonic>
            <classWitsml>torque (average)</classWitsml>
            <unit>kft.lbf</unit>
            <mnemAlias>tqOnBot</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>On bottom torque</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-5">
            <mnemonic>TQ off btm</mnemonic>
            <classWitsml>torque (average)</classWitsml>
            <unit>kft.lbf</unit>
            <mnemAlias>toOffBot</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Off bottom torque</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-6">
            <mnemonic>ROP</mnemonic>
            <classWitsml>rate of penetration (average)</classWitsml>
            <unit>m/h</unit>
            <mnemAlias>ropAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Drill rate</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-7">
            <mnemonic>WOP</mnemonic>
            <classWitsml>weight on bit (average)</classWitsml>
            <unit>klbf</unit>
            <mnemAlias>wobAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Weight on bit</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-8">
            <mnemonic>HKLD</mnemonic>
            <classWitsml>hookload (average)</classWitsml>
            <unit>klbf</unit>
            <mnemAlias>hkldAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Hookload</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-9">
            <mnemonic>Surf RPM</mnemonic>
            <classWitsml>rotary speed (average)</classWitsml>
            <unit>rpm</unit>
            <mnemAlias>rpmAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>RPM measured at surface</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-10">
            <mnemonic>Mtr RPM</mnemonic>
            <classWitsml>measured motor speed</classWitsml>
            <unit>rpm</unit>
            <mnemAlias>mmrpm</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Calculated motor RPM</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-11">
            <mnemonic>Avg TQ</mnemonic>
            <classWitsml>torque (average)</classWitsml>
            <unit>kft.lbf</unit>
            <mnemAlias>tqAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Average drilling torque</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-12">
            <mnemonic>Max TQ</mnemonic>
            <classWitsml>torque (maximum)</classWitsml>
            <unit>kft.lbf</unit>
            <mnemAlias>torque (maximum)</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Maximum drilling torque</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-13">
            <mnemonic>Min TQ</mnemonic>
            <classWitsml>torque (average)</classWitsml>
            <unit>kft.lbf</unit>
            <mnemAlias>tqMn</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Minimum drilling torque</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-14">
            <mnemonic>MaxMin TQ1</mnemonic>
            <classWitsml>torque (maximum)</classWitsml>
            <unit>kft.lbf</unit>
            <mnemAlias>tqMx-Mn</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Maximum - minimum drilling torque</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-15">
            <mnemonic>MaxMin TQ2</mnemonic>
            <classWitsml>flow rate in (average)</classWitsml>
            <unit>galUS/min</unit>
            <mnemAlias>flowInAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Average mud flow in</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-16">
            <mnemonic>Pump p avg</mnemonic>
            <classWitsml>pressure at pump (average)</classWitsml>
            <unit>lbf/in2</unit>
            <mnemAlias>presPumpAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Average pump pressure</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-17">
            <mnemonic>Mud D avg</mnemonic>
            <classWitsml>mud density in (average)</classWitsml>
            <unit>g/cm3</unit>
            <mnemAlias>wtMudInAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Average mud density</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-18">
            <mnemonic>Mud Temp avg</mnemonic>
            <classWitsml>mud temperature in (average)</classWitsml>
            <unit>degC</unit>
            <mnemAlias>tempMudInAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Average mud temperature</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-19">
            <mnemonic>Bit RPM</mnemonic>
            <classWitsml>rotary speed (average)</classWitsml>
            <unit>rpm</unit>
            <mnemAlias>rpmBitAv</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>Bit RPM</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-20">
            <mnemonic>DXC</mnemonic>
            <classWitsml>drilling exponent (corrected)</classWitsml>
            <unit>Euc</unit>
            <mnemAlias>dxc</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>d exponent</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="lci-21">
            <mnemonic>ECD</mnemonic>
            <classWitsml>ecdTd ???????????</classWitsml>
            <unit>g/cm3</unit>
            <mnemAlias>ecdTd</mnemAlias>
            <nullValue>-999.25</nullValue>
            <minIndex uom="m">499</minIndex>
            <maxIndex uom="m">509.01</maxIndex>
            <curveDescription>equivalent circulating density</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>Mdepth,Vdepth,Bit Dist,TQ on btm,TQ off btm,ROP,WOP,HKLD,Surf RPM,Mtr RPM,Avg TQ,Max TQ,Min TQ,MaxMin TQ1,MaxMin TQ2,Pump p avg,Mud D avg,Mud Temp avg,Bit RPM,DXC,ECD</mnemonicList>
            <unitList>m,m,m,kft.lbf,kft.lbf,m/h,klbf,klbf,rpm,rpm,kft.lbf,kft.lbf,kft.lbf,kft.lbf,galUS/min,lbf/in2,g/cm3,degC,rpm,Euc,g/cm3</unitList>
            <data>499,498.99,1.25,0,1.45,3.67,11.02,187.66,0.29,116.24,0.01,0.05,0.01,0,886.03,1089.99,1.11,14.67,0.29,1.12,1.11</data>
            <data>500.01,500,1.9,0.01,1.42,9.94,11.32,185.7,0.29,116.24,0.01,0.01,0.01,0,795.19,973.48,1.11,14.67,0.29,0.95,1.11</data>
            <data>501.03,501.02,2.92,0.02,1.41,20.46,11.62,184.23,0.29,120,0.01,0.01,0.01,0,796.68,956.25,1.11,14.67,0.29,0.83,1.11</data>
            <data>502.01,502,3.9,0.06,1.44,21.73,10.37,185.49,0.29,120,0.01,0.01,0.01,0,802.96,1005.68,1.1,14.66,0.3,0.8,1.11</data>
            <data>503.01,503,4.9,0.11,1.48,17.65,10.31,185.55,0.29,118.09,0.01,0.01,0.01,0,801.19,1007.77,1.11,14.66,0.3,0.83,1.11</data>
            <data>504.05,504.04,5.94,0.18,1.55,15.58,10.4,185.43,0.29,120,0.01,0.01,0.01,0,800.83,1015.89,1.1,14.67,0.29,0.86,1.11</data>
            <data>505.03,505.00,612.03,1.83,3.32,37.11,18.5,243.38,91.93,0,8.07,8.35,7.68,0.19,900.07,3205,1.26,29.67,93.74,0.75,1.31</data>
            <data>506.04,505.95,613.04,1.9,3.4,9.85,27.79,233.9,79,0,8.31,10.24,6.83,1.02,907.9,3210,1.26,29.8,95,1.09,1.31</data>
            <data>507.04,506.91,614.04,1.97,3.46,32.44,23.13,238.59,77.35,0,7.93,8.96,7.76,0.14,911.55,3223.33,1.26,29.88,89.19,0.78,1.31</data>
            <data>508.01,507.84,615.01,2,3.49,29.03,19.38,242.36,90.59,0,8.32,8.78,7.76,0.32,899.74,3222.17,1.26,29.95,91.66,0.8,1.31</data>
            <data>509.01,508.75,616.01,2.08,3.54,13.09,15.89,245.92,93.38,0,7.62,11.87,6.43,0.86,900.93,3215.78,1.26,30.06,98.51,0.92,1.31</data>
        </logData>
        <commonData>
            <dTimCreation>2003-11-24T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2003-11-24T08:17:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the log object.</comments>
        </commonData>
    </log>
</logs>""")  


WMLS_AddToStore(WMLTYPEIN_LOG, "$log_xml$")  
check_ReturnValue_Success()
partial_success("WMLS_AddToStore succeeded log")
set('uid', get_SuppMsgOut_uid_String())
log_variable('uid')
new_object_created(WMLTYPEIN_LOG, "$uid$", uidWell="$server_w1_uid$", uidWellbore="$server_w1_wb1_uid$")

# 2. Get the object

WMLS_GetFromStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                     <log uid="$uid$" uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$"/>
                                   </logs>
                                """, OptionsIn={'returnElements':'all'})  
check_ReturnValue_Success()
check_XMLout_NumberOfObjects(1)
partial_success("WMLS_GetFromStore succeeded log")


# 3. Check the received object against the loaded object

check_XMLout_XMLNormalizedString(WMLTYPEIN_LOG, "$log_xml$")
partial_success("Object retrieved matches object loaded")


log('Script procedure end')

success()
