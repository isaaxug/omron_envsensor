"""
"""
from __future__ import absolute_import

__version__ = '0.0.1'

from logging import getLogger, NullHandler
logger = getLogger('omron_envsensor')
logger.addHandler(NullHandler())

from .omron import OmronEnvSensor
