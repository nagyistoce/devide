# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkTreeWriter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkTreeWriter(), 'Writing vtkTree.',
            ('vtkTree',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
