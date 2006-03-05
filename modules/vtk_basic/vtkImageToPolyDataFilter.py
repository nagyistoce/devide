# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkImageToPolyDataFilter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkImageToPolyDataFilter(), 'Processing.',
            ('vtkImageData',), ('vtkPolyData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)