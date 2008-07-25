import genUtils
from module_base import ModuleBase
from moduleMixins import NoConfigModuleMixin
import module_utils
import vtk


class polyDataConnect(NoConfigModuleMixin, ModuleBase):

    def __init__(self, module_manager):

        # call parent constructor
        ModuleBase.__init__(self, module_manager)

        self._polyDataConnect = vtk.vtkPolyDataConnectivityFilter()
        # we're not going to use this feature just yet
        self._polyDataConnect.ScalarConnectivityOff()
        #
        self._polyDataConnect.SetExtractionModeToPointSeededRegions()

        module_utils.setupVTKObjectProgress(self, self._polyDataConnect,
                                           'Finding connected surfaces')
        
        # and the mixin constructor
        NoConfigModuleMixin.__init__(
            self,
            {'vtkPolyDataConnectivityFilter' :
             self._polyDataConnect})

        # we'll use this to keep a binding (reference) to the passed object
        self._inputPoints = None
        # this will be our internal list of points
        self._seedIds = []

        self.sync_module_logic_with_config()
        
    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        self.set_input(0, None)
        # don't forget to call the close() method of the vtkPipeline mixin
        NoConfigModuleMixin.close(self)
        # get rid of our reference
        del self._polyDataConnect

    def get_input_descriptions(self):
	return ('vtkPolyData', 'Seed points')
    
    def set_input(self, idx, inputStream):
        if idx == 0:
            # will work for None and not-None
            self._polyDataConnect.SetInput(inputStream)
            if inputStream is not None:
                # new inputStream, so if we have inputPoints, reset
                # (they are dependent on the input polydata)
                self._inputPointsObserver(self._inputPoints)
        else:
            if inputStream is None:
                if self._inputPoints:
                    self._inputPoints.removeObserver(self._inputPointsObserver)
                
            else:
                inputStream.addObserver(self._inputPointsObserver)

            self._inputPoints = inputStream

            # initial update
            self._inputPointsObserver(self._inputPoints)
    
    def get_output_descriptions(self):
	return (self._polyDataConnect.GetOutput().GetClassName(),)
    
    def get_output(self, idx):
        return self._polyDataConnect.GetOutput()

    def logic_to_config(self):
        pass

    def config_to_logic(self):
        pass
    
    def view_to_config(self):
        pass

    def config_to_view(self):
        pass
    
    def execute_module(self):
        self._polyDataConnect.Update()
        
    def _inputPointsObserver(self, obj):
        # extract a list from the input points
        tempList = []
        if self._inputPoints and self._polyDataConnect.GetInput():
            for i in self._inputPoints:
                id = self._polyDataConnect.GetInput().FindPoint(i['world'])
                if id > 0:
                    tempList.append(id)
            
        if tempList != self._seedIds:
            self._seedIds = tempList
            # I'm hoping this clears the list
            self._polyDataConnect.InitializeSeedList()
            for seedId in self._seedIds:
                self._polyDataConnect.AddSeed(seedId)
                print "adding %d" % (seedId)



