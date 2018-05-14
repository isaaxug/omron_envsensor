
from logging import getLogger
logger = getLogger('omron_envsensor')

import sys
from omron_envsensor import OmronEnvSensor
from omron_envsensor.sensorbeacon import csv_header

def main():
    sys.stdout.write(csv_header())
    sys.stdout.write("\r\n")

    before_seq = None
    o = OmronEnvSensor('pudge', 0)

    def callback(beacon):
        sys.stdout.write(beacon.csv_format())
        sys.stdout.write("\r\n")

    o.on_message = callback
    o.init()
    o.loop()

if __name__ == '__main__':
    main()
