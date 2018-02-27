# GcInventoryTechProbability struct

from .Struct import Struct

STRUCTNAME = 'GcInventoryTechProbability'

class GcInventoryTechProbability(Struct):
    def __init__(self, **kwargs):
        super(GcInventoryTechProbability, self).__init__()

        """ Contents of the struct """
        self.data['Tech'] = kwargs.get('Tech', '')
        self.data['DesiredTechProbability'] = kwargs.get('DesiredTechProbability', 'Never')
        """ End of the struct contents"""

        # Parent needed so that it can be a SubElement of something
        self.parent = None
        self.STRUCTNAME = STRUCTNAME
