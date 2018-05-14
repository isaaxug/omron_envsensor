
from logging import getLogger
logger = getLogger('omron_envsensor')

from omron_envsensor import OmronEnvSensor

def main():
    import logging
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    before_seq = None
    o = OmronEnvSensor('pudge', 0)

    def callback(beacon):
        beacon.debug_print(logger)

    o.on_message = callback
    o.init()
    o.loop()

if __name__ == '__main__':
    main()
