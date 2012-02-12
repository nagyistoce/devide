# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkImageMask(SimpleVTKClassModuleBase):
    def __init__(self, module_manager):
        SimpleVTKClassModuleBase.__init__(
            self, module_manager,
            vtk.vtkImageMask(), 'Processing.',
            ('vtkImageData', 'vtkImageData'), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
