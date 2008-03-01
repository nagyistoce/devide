# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkGraphHierarchicalBundle(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkGraphHierarchicalBundle(), 'Processing.',
            ('vtkAbstractGraph', 'vtkTree'), ('vtkPolyData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
