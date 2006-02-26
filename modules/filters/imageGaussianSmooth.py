# imageGaussianSmooth copyright (c) 2003 by Charl P. Botha cpbotha@ieee.org
# $Id$
# performs image smoothing by convolving with a Gaussian

import genUtils
from moduleBase import moduleBase
from moduleMixins import vtkPipelineConfigModuleMixin
import moduleUtils
import vtk
from module_kits.vtk_kit.mixins import VTKErrorFuncMixin

class imageGaussianSmooth(moduleBase, vtkPipelineConfigModuleMixin,
                          VTKErrorFuncMixin):

    """Performs 3D Gaussian filtering of the input volume.
    """

    def __init__(self, moduleManager):
        moduleBase.__init__(self, moduleManager)

        self._imageGaussianSmooth = vtk.vtkImageGaussianSmooth()

        moduleUtils.setupVTKObjectProgress(self, self._imageGaussianSmooth,
                                           'Smoothing image with Gaussian')
        self.add_vtk_error_handler(self._imageGaussianSmooth)

        self._config.standardDeviation = (2.0, 2.0, 2.0)
        self._config.radiusCutoff = (1.5, 1.5, 1.5)

        self._viewFrame = None
        self._createViewFrame()

        self.configToLogic()
        self.logicToConfig()
        self.configToView()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        self.setInput(0, None)
        # don't forget to call the close() method of the vtkPipeline mixin
        vtkPipelineConfigModuleMixin.close(self)
        # take out our view interface
        self._viewFrame.Destroy()
        # get rid of our reference
        del self._imageGaussianSmooth
        # and finally call our base dtor
        moduleBase.close(self)
        
    def getInputDescriptions(self):
        return ('vtkImageData',)

    def setInput(self, idx, inputStream):
        self._imageGaussianSmooth.SetInput(inputStream)

    def getOutputDescriptions(self):
        return (self._imageGaussianSmooth.GetOutput().GetClassName(),)

    def getOutput(self, idx):
        return self._imageGaussianSmooth.GetOutput()

    def logicToConfig(self):
        self._config.standardDeviation = self._imageGaussianSmooth.\
                                         GetStandardDeviations()
        self._config.radiusCutoff = self._imageGaussianSmooth.\
                                    GetRadiusFactors()

    def configToLogic(self):
        self._imageGaussianSmooth.SetStandardDeviations(
            self._config.standardDeviation)
        self._imageGaussianSmooth.SetRadiusFactors(
            self._config.radiusCutoff)

    def viewToConfig(self):
        # continue with textToTuple in genUtils
        stdText = self._viewFrame.stdTextCtrl.GetValue()
        self._config.standardDeviation = genUtils.textToTypeTuple(
            stdText, self._config.standardDeviation, 3, float)
        
        cutoffText = self._viewFrame.radiusCutoffTextCtrl.GetValue()
        self._config.radiusCutoff = genUtils.textToTypeTuple(
            cutoffText, self._config.radiusCutoff, 3, float)

    def configToView(self):
        stdText = '(%.2f, %.2f, %.2f)' % self._config.standardDeviation
        self._viewFrame.stdTextCtrl.SetValue(stdText)

        cutoffText = '(%.2f, %.2f, %.2f)' % self._config.radiusCutoff
        self._viewFrame.radiusCutoffTextCtrl.SetValue(cutoffText)

    def executeModule(self):
        self._imageGaussianSmooth.Update()
        self.check_vtk_error()

    def view(self, parent_window=None):
        # if the window was visible already. just raise it
        if not self._viewFrame.Show(True):
            self._viewFrame.Raise()

    def _createViewFrame(self):
        self._moduleManager.importReload(
            'modules.filters.resources.python.imageGaussianSmoothViewFrame')
        import modules.filters.resources.python.imageGaussianSmoothViewFrame

        self._viewFrame = moduleUtils.instantiateModuleViewFrame(
            self, self._moduleManager,
            modules.filters.resources.python.imageGaussianSmoothViewFrame.\
            imageGaussianSmoothViewFrame)

        objectDict = {'vtkImageGaussianSmooth' : self._imageGaussianSmooth}
        moduleUtils.createStandardObjectAndPipelineIntrospection(
            self, self._viewFrame, self._viewFrame.viewFramePanel,
            objectDict, None)

        moduleUtils.createECASButtons(self, self._viewFrame,
                                      self._viewFrame.viewFramePanel)
