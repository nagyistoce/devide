from moduleBase import moduleBase
from moduleMixins import scriptedConfigModuleMixin
import moduleUtils
import vtk



class warpPoints(scriptedConfigModuleMixin, moduleBase):
    """Warp input points according to their associated vectors.

    $Revision: 1.1 $
    """

    _defaultVectorsSelectionString = 'Default Active Vectors'
    _userDefinedString = 'User Defined'

    def __init__(self, moduleManager):
        moduleBase.__init__(self, moduleManager)

        self._config.scaleFactor = 1
        self._config.vectorsSelection = self._defaultVectorsSelectionString


        configList = [
            ('Scale factor:', 'scaleFactor', 'base:float', 'text',
             'The warping will be scaled by this factor'),
            ('Vectors selection:', 'vectorsSelection', 'base:str', 'choice',
             'The attribute that will be used as vectors for the warping.',
             (self._defaultVectorsSelectionString, self._userDefinedString))]

        scriptedConfigModuleMixin.__init__(self, configList)

        self._warpVector = vtk.vtkWarpVector()
        
        moduleUtils.setupVTKObjectProgress(self, self._warpVector,
                                           'Warping points.')

        self._createWindow(
            {'Module (self)' : self,
             'vtkWarpVector' : self._warpVector})

        # pass the data down to the underlying logic
        self.configToLogic()
        # and all the way up from logic -> config -> view to make sure
        self.syncViewWithLogic()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.getInputDescriptions())):
            self.setInput(inputIdx, None)

        # this will take care of all display thingies
        scriptedConfigModuleMixin.close(self)
        
        # get rid of our reference
        del self._warpVector

    def executeModule(self):
        self._warpVector.Update()

    def getInputDescriptions(self):
        return ('VTK points/polydata with vector attribute',)

    def setInput(self, idx, inputStream):
        self._warpVector.SetInput(inputStream)

    def getOutputDescriptions(self):
        return ('Warped data',)

    def getOutput(self, idx):
        return self._warpVector.GetOutput()

    def logicToConfig(self):
        self._config.scaleFactor = self._warpVector.GetScaleFactor()

        # the vector choice is the second configTuple
        choice = self._getWidget(1)

        if self._warpVector.GetInput():
            pd = self._warpVector.GetInput().GetPointData()
            if pd:
                # get a list of attribute names
                names = []
                for i in range(pd.GetNumberOfArrays()):
                    names.append(pd.GetArray(i).GetName())
                
                # find out what the choices CURRENTLY are (except for the
                # default and the "user defined")
                choiceNames = []
                ccnt = choice.GetCount()
                for i in range(2,ccnt):
                    choiceNames.append(choice.GetString(i))

                if choiceNames != names:
                    # this means things have changed, we have to rebuild
                    # the choice
                    choice.Clear()
                    choice.Append(self._defaultVectorsSelectionString)
                    choice.Append(self._userDefinedString)
                    for name in names:
                        choice.Append(name)

        vs = self._warpVector.GetInputVectorsSelection()

        if vs:
            si = choice.FindString(vs)
            if si == -1:
                # string not found, that means the user has been playing
                # behind our backs, (or he's loading a valid selection
                # from DVN) so we add it to the choice as well
                choice.Append(vs)
                choice.SetStringSelection(vs)

            else:
                choice.SetSelection(si)

        else:
            # no vector selection, so default
            choice.SetSelection(0)
        
                
    
    def configToLogic(self):
        self._warpVector.SetScaleFactor(self._config.scaleFactor)

        if self._config.vectorsSelection == \
               self._defaultVectorsSelectionString:
            # default
            self._warpVector.SelectInputVectors(None)
            
        else:
            self._warpVector.SelectInputVectors(self._config.vectorsSelection)
