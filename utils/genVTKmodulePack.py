import vtk

# parameters that need to be filled in:
# moduleName, vtkObjectName, progressText, inputDescriptions, outputDescrs
moduleSkeleton1 = "# class generated by " \
                  "DeVIDE::createDeVIDEModuleFromVTKObject\n" \
                  "from module_kits.vtk_kit.mixins " \
                  "import SimpleVTKClassModuleBase\n" \
                  "import vtk\n\n" \
                  "class %s(SimpleVTKClassModuleBase):\n" \
                  "    def __init__(self, moduleManager):\n" \
                  "        SimpleVTKClassModuleBase.__init__(\n" \
                  "            self, moduleManager,\n" \
                  "            vtk.%s(), '%s',\n" \
                  "            %s, %s,\n" \
                  "            replaceDoc=True,\n" \
                  "            inputFunctions=%s, outputFunctions=%s)\n"

excludeList = ['vtkDataWriter', 'vtkDataReader', # two helper classes
               'vtkStructuredPointsGeometryFilter', # deprecated after 4.0
               'vtkDemandDrivenPipeline', # CRASH
               'vtkStreamingDemandDrivenPipeline', # CRASH
               'vtkAlgorithm' # abstract (kinda)
               ]

def createDeVIDEModuleFromVTKObject(vtkObjName):
    """Returns tuple with first element the name of the module,
    the second element a string representing the complete code, the third
    element a tuple of categories to which the module belongs.
    """

    # instantiate it
    vtkObj = getattr(vtk, vtkObjName)()

    
    if vtkObjName.endswith('Writer'):
        moduleName = vtkObjName

        # with moduleName[:-6] we snip off the 'Writer'
        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Writing %s.' % (moduleName[:-6],),
                                        (vtkObjName[:-6],), (),
                                        None, None)
        return (moduleName, moduleText, 'VTK basic writer')
        
    elif vtkObjName.endswith('Reader'):
        moduleName = vtkObjName

        # with moduleName[:-6] we snip off the 'Reader'
        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Reading %s.' % (moduleName[:-6],),
                                        (), (vtkObjName[:-6],),
                                        None, None)
        return (moduleName, moduleText, 'VTK basic readers')

    else:

        # determine number and types of inputs, building up list of
        # input types as we go along
        num_i = vtkObj.GetNumberOfInputPorts()
        ip_types = []
        for i in range(num_i):
            ip_inf = vtkObj.GetInputPortInformation(i)
            ip_typ = ip_inf.Get(vtk.vtkAlgorithm.INPUT_REQUIRED_DATA_TYPE())
            ip_types.append(ip_typ)
        # we need a tuple for creating the DeVIDE module
        ip_types = tuple(ip_types)

        # do the same for the outputs
        num_o = vtkObj.GetNumberOfOutputPorts()
        op_types = []
        for i in range(num_o):
            op_inf = vtkObj.GetOutputPortInformation(i)
            op_typ = op_inf.Get(vtk.vtkDataObject.DATA_TYPE_NAME())
            op_types.append(op_typ)

        op_types = tuple(op_types)

        # and create the module
        moduleName = vtkObjName
        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Processing.',
                                        ip_types, op_types,
                                        None, None)

        return (moduleName, moduleText, 'VTK basic filters')
        

def blaat():
    # use GetInputPortInformation() INPUT_REQUIRED_DATA_TYPE
    # GetNumberOfInputPorts()

    if vtkObj.IsA('vtkPolyDataAlgorithm'):
        moduleName = vtkObjName

        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Processing.',
                                        ('vtkPolyData',), ('vtkPolyData',),
                                        None, None)
        return (moduleName, moduleText, 'vtkPolyToPoly')

    # now all the vtkImageSource derivatives ------------------------------
    # ---------------------------------------------------------------------
    
    elif vtkObj.IsA('vtkImageTwoInputFilter'):
        moduleName = vtkObjName

        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Processing.',
                                        ('Input 1 (vtkImageData)',
                                         'Input 2 (vtkImageData)'),
                                        ('vtkImageData',),
                                        ('SetInput1(inputStream)',
                                         'SetInput2(inputStream)'), None)

        return (moduleName, moduleText, 'vtkImageToImage')
        
    elif vtkObj.IsA('vtkImageMultipleInputFilter'):
        moduleName = vtkObjName
        inputDescriptions = ('Input 1 (vtkImageData)',
                             'Input 2 (vtkImageData)',
                             'Input 3 (vtkImageData)',
                             'Input 4 (vtkImageData)',
                             'Input 5 (vtkImageData)')
        inputMethods = ('SetInput(0, inputStream)',
                        'SetInput(1, inputStream)',
                        'SetInput(2, inputStream)',
                        'SetInput(3, inputStream)',
                        'SetInput(4, inputStream)')

        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Processing.',
                                        inputDescriptions,
                                        ('vtkImageData',),
                                        inputMethods, None)

        return (moduleName, moduleText, 'vtkImageToImage')

    elif vtkObj.IsA('vtkImageToImageFilter'):
        moduleName = vtkObjName

        moduleText = moduleSkeleton1 % (moduleName, vtkObjName,
                                        'Processing.',
                                        ('vtkImageData',), ('vtkImageData',),
                                        None, None)
        return (moduleName, moduleText, 'vtkImageToImage')

    else:
        return (None, None, None)
        


def main():
    list1 = [i for i in dir(vtk)
             if i.startswith('vtk') and i not in excludeList]
    list2 = []

    # objects that can be instantiated 
    for vtkobj in list1:
        try:
            print vtkobj
            a = getattr(vtk, vtkobj)()
        except:
            # if it can't be instantiated, we can't use it
            pass
        else:
            if a.IsA('vtkAlgorithm'):
                list2.append(vtkobj)

    # list2 will now be parsed and modules will be generated
    # we have to start our conditionals with the most specific cases
    # and work down to the more general cases.
    moduleListStrings = ['# Generated by '\
                         'DeVIDE::createDeVIDEModuleFromVTKObject\n']

    for vtkObjName in list2:
        moduleName, moduleText, moduleCats = createDeVIDEModuleFromVTKObject(
            vtkObjName)
        
        if moduleName:
            f = open('%s.py' % (moduleName,), 'w')
            f.write(moduleText)

            moduleListStrings.append("class %s:" % (moduleName,))
            moduleListStrings.append("    kits = ['vtk_kit']")
            moduleListStrings.append("    cats = ['%s']\n" % (moduleCats,))

            #moduleListStrings.append("'%s' : %s," % (moduleName, moduleCats))
            f.close()
            print "Wrote %s.py." % (moduleName,)

    if len(moduleListStrings):
        # snip off the last ,
        #moduleListStrings[-1] = moduleListStrings[-1][:-1]
        moduleListString = '\n'.join(moduleListStrings)

        f = open('module_index.py', 'w')
        f.write(moduleListString)
        f.close()
        print "\nWrote module_index.py.\n"


if __name__ == '__main__':
    main()
