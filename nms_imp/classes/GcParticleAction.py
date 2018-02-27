# GcParticleAction struct

from .Struct import Struct

STRUCTNAME = 'GcParticleAction'

class GcParticleAction(Struct):
    def __init__(self, **kwargs):
        super(GcParticleAction, self).__init__()

        """ Contents of the struct """
        self.data['Effect'] = kwargs.get('Effect', "")
        self.data['Joint'] = kwargs.get('Joint', "")
        self.data['Exact'] = bool(kwargs.get('Exact', False))
        """ End of the struct contents"""

        # Parent needed so that it can be a SubElement of something
        self.parent = None
        self.STRUCTNAME = STRUCTNAME
