# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkSQLTableReader(SimpleVTKClassModuleBase):
    def __init__(self, module_manager):
        SimpleVTKClassModuleBase.__init__(
            self, module_manager,
            vtk.vtkSQLTableReader(), 'Reading vtkSQLTable.',
            (), ('vtkSQLTable',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
