# TkMaterialSampler struct

from .Struct import Struct
from .String import String

STRUCTNAME = 'TkMaterialSampler'

class TkMaterialSampler(Struct):
    def __init__(self, **kwargs):
        # size will be a bit off...
        super(TkMaterialSampler, self).__init__()

        """ Contents of the struct """
        self.data['Name'] = String(kwargs.get('Name', ""), 0x20)
        self.data['Map'] = String(kwargs.get('Map', ""), 0x80)
        self.data['IsCube'] = kwargs.get('IsCube', False)
        self.data['UseCompression'] = kwargs.get('UseCompression', True)
        self.data['UseMipMaps'] = kwargs.get('UseMipMaps', True)
        self.data['IsSRGB'] = kwargs.get('IsSRGB', True)        # True image, False for MASKS and NORMAL
        self.data['MaterialAlternativeId'] = String(kwargs.get('MaterialAlternativeId', ""), 0x10)
        self.data['TextureAddressMode'] = kwargs.get('TextureAddressMode', "Wrap")
        self.data['TextureFilterMode'] = kwargs.get('TextureFilterMode', "Trilinear")
        self.data['Anisotropy'] = kwargs.get('Anisotropy', 0)
        """ End of the struct contents"""

        # Parent needed so that it can be a SubElement of something
        self.parent = None
        self.STRUCTNAME = STRUCTNAME
