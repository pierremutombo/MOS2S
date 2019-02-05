#!/usr/bin/env python3

# SENSORS

"""
These are all the 90 sensors we wiil have in the project

thing_id:	The same concept from IDLab IoT stack.
scope_id:	The same concept from IDLab IoT stack.
sensor_type:	1: airvisualsensor (fancy sensor) 2: opendatasensor (not fancy sensor).
sensor_url:	Only for AirVisualSensor. It is provided for the AirVisual API.
sensor_id:	Only for OpendataSensor. Those are the sensor id 
		for the pollution sensor (SDS011) and 
		the weather sensor (DHT22) respectively.
"""


SENSORS = [
{'thing_id':"mos2s.hercules.set1.multisensor1",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/rsoSGy2nRr6DrtN75'},
{'thing_id':"mos2s.hercules.set1.multisensor2",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/orvbSTSMgYeaQteC4'},
{'thing_id':"mos2s.hercules.set1.multisensor3",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/T3dDeSJ9rHyCqcDYs'},
{'thing_id':"mos2s.hercules.set1.multisensor4",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/E9wY3iHRNFxFRLmxv'},
{'thing_id':"mos2s.hercules.set1.multisensor5",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/vvgqW7jvdBTNvLK9D'},
{'thing_id':"mos2s.hercules.set1.multisensor6",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/AxnmFnCmFDnxiLwk9'},
{'thing_id':"mos2s.hercules.set1.multisensor7",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/jNZFyyfcoryhwWR5r'},
{'thing_id':"mos2s.hercules.set1.multisensor8",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/FNsutkaEyStayZrdf'},
{'thing_id':"mos2s.hercules.set1.multisensor9",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/xgJATzGuqybFgFPHF'},
{'thing_id':"mos2s.hercules.set1.multisensor10",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/Bircjdb8tE5BCZpbQ'},
{'thing_id':"mos2s.hercules.set1.multisensor11",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/gW5PXMHzr7Ewv8f6i'},
{'thing_id':"mos2s.hercules.set1.multisensor12",'scope_id':'other.mos2s.hercules.set1','sensor_type':1,'sensor_url':'https://www.airvisual.com/api/v2/node/WnfAqWkntSEt9mZnY'},

]

