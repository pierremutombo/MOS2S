#!/usr/bin/env python3

import time
from collections import defaultdict
from mos2s.airvisualsensor.airvisualsensor import AirVisualSensor
from mos2s.opendatasensor.opendatasensor import OpenDataSensor
from mos2s.core.utils import *
from mos2s.main import *
from mos2s.core.const import CLIENTS, PERIOD, SCOPES


all_data = defaultdict(list)

if __name__ == '__main__':
    
    create_sensors()
    tokens = get_all_tokens()
    print("Init finished")
    print('\n\n')
    '''
        for sensor in AirVisualSensor:
        sensor.print_sensor_attributes()
        print("-----------------------")
        
        for sensor in OpenDataSensor:
        sensor.print_sensor_attributes()
        print("-----------------------")
        '''
            
            for sensor in AirVisualSensor._allSensors:
                # Routine to test an AirVisualSensor
                print('######## -------AirVisualSensor------ ###########')
                #sensor.print_sensor_attributes()
                print('############################################')
                data = sensor.get_sensor_metrics()
                #print(data)
                sensor.update_metrics(data)
                #sensor.print_sensor_attributes()
                sensor.store_metrics(data)
                parsed_data = sensor.parse_data()
                print('############################################')
                print(parsed_data)
                response = post_ingest(client=CLIENTS[0]['CLIENT_ID'],data=[parsed_data],token=tokens)
                print(response)
                print('\n\n')

