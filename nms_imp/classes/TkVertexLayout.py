# TkVertexLayout struct

from .Struct import Struct

STRUCTNAME = 'TkVertexLayout'

class TkVertexLayout(Struct):
    def __init__(self, **kwargs):

        """ Contents of the struct """
        self.ElementCount = kwargs.get('ElementCount', 0)
        self.Stride = kwargs.get('Stride', 0)
        self.PlatformData = kwargs.get('PlatformData', "")
        self.VertexElements = kwargs.get('VertexElements', None)
        """ End of the struct contents"""

        """ Run code to convert struct contents into self.data_dict """
        self._create_dict()

        # Parent needed so that it can be a SubElement of something
        self.parent = None
        self.STRUCTNAME = STRUCTNAME
