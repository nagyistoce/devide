# $Id: module_utils.py,v 1.7 2002/06/10 16:58:33 cpbotha Exp $

from wxPython.wx import *
from wxPython.xrc import *
from external.vtkPipeline.vtkPipeline import \
     vtkPipelineBrowser
from external.vtkPipeline.ConfigVtkObj import ConfigVtkObj

def bind_CSAEO(module, view_frame):
    # it seems wxID_CANCEL (and probably some others) is an exception
    # if you use XMLID on it, it just don't work dude
    EVT_BUTTON(view_frame, wxID_CANCEL,
               lambda e, vf=view_frame: vf.Show(false))
    EVT_BUTTON(view_frame, wxID_OK,
               lambda e, m=module, vf=view_frame: (m.apply_config(),
                                                   vf.Show(false)))
    EVT_BUTTON(view_frame, XMLID('MV_ID_SYNC'),
               lambda e, m=module: m.sync_config())
    EVT_BUTTON(view_frame, XMLID('MV_ID_APPLY'),
               lambda e, m=module: m.apply_config())
    EVT_BUTTON(view_frame, XMLID('MV_ID_EXECUTE'),
               lambda e, m=module: (m.apply_config(),
                                    m.execute_module()))
    
