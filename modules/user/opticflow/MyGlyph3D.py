import genUtils
from moduleBase import moduleBase
from moduleMixins import scriptedConfigModuleMixin
import moduleUtils
import vtk
import vtktud
from module_kits.vtk_kit.mixins import VTKErrorFuncMixin

class MyGlyph3D(scriptedConfigModuleMixin, moduleBase,
                VTKErrorFuncMixin):

    def __init__(self, moduleManager):
        # initialise our base class
        moduleBase.__init__(self, moduleManager)


        self._glyph3d = vtktud.vtkMyGlyph3D()
        
        moduleUtils.setupVTKObjectProgress(self, self._glyph3d,
                                           'Making 3D glyphs')
        self.add_vtk_error_handler(self._glyph3d)
                                           
        self._config.scaling = 1.0


        configList = [
            ('Scaling:', 'scaling', 'base:float', 'text',
             'Glyphs will be scaled by this factor.')]
        scriptedConfigModuleMixin.__init__(self, configList)        
        

        self._viewFrame = self._createWindow(
            {'Module (self)' : self,
             'vtkMyGlyph3D' : self._glyph3d})

        # pass the data down to the underlying logic
        self.configToLogic()
        # and all the way up from logic -> config -> view to make sure
        self.logicToConfig()
        self.configToView()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.getInputDescriptions())):
            self.setInput(inputIdx, None)

        # this will take care of all display thingies
        scriptedConfigModuleMixin.close(self)

        moduleBase.close(self)
        
        # get rid of our reference
        del self._glyph3d

    def getInputDescriptions(self):
        return ('vtkPolyData',)

    def setInput(self, idx, inputStream):
        self._glyph3d.SetInput(inputStream)

    def getOutputDescriptions(self):
        return ('Glyphs (vtkPolyData)', )

    def getOutput(self, idx):
        return self._glyph3d.GetOutput()

    def logicToConfig(self):
        self._config.scaling = self._glyph3d.GetScaling()
    
    def configToLogic(self):
        self._glyph3d.SetScaling(self._config.scaling)
    
    def executeModule(self):
        self._glyph3d.Update()
        self.check_vtk_error()


