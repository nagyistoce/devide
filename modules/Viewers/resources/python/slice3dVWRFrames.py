#!/usr/bin/env python
# generated by wxGlade 0.3.2pre2 on Sat Feb 21 21:16:21 2004

from wxPython.wx import *
from wxPython.grid import *

# with the very ugly two lines below, make sure x capture is not used
# this should rather be an ivar of the wxVTKRenderWindowInteractor!
import vtk.wx.wxVTKRenderWindowInteractor
vtk.wx.wxVTKRenderWindowInteractor.WX_USE_X_CAPTURE = 0
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor


class threedFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: threedFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_1 = wxPanel(self, -1)
        self.showControlsButtonId  =  wxNewId()
        self.button_2 = wxButton(self.panel_1, self.showControlsButtonId , "Show Controls")
        self.resetCameraButtonId  =  wxNewId()
        self.resetCameraButton = wxButton(self.panel_1, self.resetCameraButtonId , "Reset Camera")
        self.resetAllButtonId  =  wxNewId()
        self.button = wxButton(self.panel_1, self.resetAllButtonId , "Reset All")
        self.introspectPipelineButtonId  =  wxNewId()
        self.button_5 = wxButton(self.panel_1, self.introspectPipelineButtonId , "Introspect")
        self.projectionChoiceId  =  wxNewId()
        self.projectionChoice = wxChoice(self.panel_1, self.projectionChoiceId , choices=["Perspective", "Orthogonal"])
        self.threedRWI = wxVTKRenderWindowInteractor(self.panel_1, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: threedFrame.__set_properties
        self.SetTitle("Slice3D Viewer")
        self.SetSize((640, 480))
        self.projectionChoice.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: threedFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_8 = wxBoxSizer(wxVERTICAL)
        sizer_2 = wxBoxSizer(wxHORIZONTAL)
        sizer_15 = wxBoxSizer(wxVERTICAL)
        sizer_15.Add(self.button_2, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.resetCameraButton, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.button, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.button_5, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.projectionChoice, 0, wxEXPAND, 0)
        sizer_2.Add(sizer_15, 0, wxRIGHT|wxEXPAND, 4)
        sizer_2.Add(self.threedRWI, 1, wxEXPAND, 0)
        sizer_8.Add(sizer_2, 1, wxALL|wxEXPAND, 7)
        self.panel_1.SetAutoLayout(1)
        self.panel_1.SetSizer(sizer_8)
        sizer_8.Fit(self.panel_1)
        sizer_8.SetSizeHints(self.panel_1)
        sizer_1.Add(self.panel_1, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class threedFrame


class orthoViewFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: orthoViewFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_2 = wxPanel(self, -1)
        self.RWI = wxVTKRenderWindowInteractor(self.panel_2, -1)
        self.closeButtonId  =  wxNewId()
        self.button_1 = wxButton(self.panel_2, self.closeButtonId , "Close")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: orthoViewFrame.__set_properties
        self.SetTitle("Ortho View")
        self.SetSize((480, 433))
        self.RWI.SetSize((-1, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: orthoViewFrame.__do_layout
        sizer_4 = wxBoxSizer(wxVERTICAL)
        sizer_5 = wxBoxSizer(wxVERTICAL)
        sizer_5.Add(self.RWI, 1, wxEXPAND, 0)
        sizer_5.Add(self.button_1, 0, wxALIGN_CENTER_HORIZONTAL, 0)
        self.panel_2.SetAutoLayout(1)
        self.panel_2.SetSizer(sizer_5)
        sizer_5.Fit(self.panel_2)
        sizer_5.SetSizeHints(self.panel_2)
        sizer_4.Add(self.panel_2, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

# end of class orthoViewFrame


class controlFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: controlFrame.__init__
        kwds["style"] = wxCAPTION|wxMINIMIZE_BOX|wxMAXIMIZE_BOX|wxSYSTEM_MENU
        wxFrame.__init__(self, *args, **kwds)
        self.panel_3 = wxPanel(self, -1)
        self.notebook_1 = wxNotebook(self.panel_3, -1, style=0)
        self.notebook_1_pane_2 = wxPanel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wxPanel(self.notebook_1, -1)
        
        # Menu Bar
        self.frame_4_menubar = wxMenuBar()
        self.SetMenuBar(self.frame_4_menubar)
        self.slicesMenu = wxMenu()
        self.frame_4_menubar.Append(self.slicesMenu, "&Slices")
        self.pointsMenu = wxMenu()
        self.frame_4_menubar.Append(self.pointsMenu, "&Points")
        self.objectsMenu = wxMenu()
        self.frame_4_menubar.Append(self.objectsMenu, "&Objects")
        self.implicitsMenu = wxMenu()
        self.frame_4_menubar.Append(self.implicitsMenu, "&Implicits")
        # Menu Bar end
        self.frame_4_statusbar = self.CreateStatusBar(1)
        self.createSliceComboBox = wxComboBox(self.notebook_1_pane_1, -1, choices=["Scapula lateral edge", "Scapula spina", "Axial", "Coronal", "Sagittal"], style=wxCB_DROPDOWN)
        self.createSliceButtonId  =  wxNewId()
        self.button_2_2 = wxButton(self.notebook_1_pane_1, self.createSliceButtonId , "Create Slice")
        self.sliceGrid = wxGrid(self.notebook_1_pane_1, -1)
        self.label_1_2 = wxStaticText(self.notebook_1_pane_1, -1, "Cursor at")
        self.sliceCursorText = wxTextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_4_2 = wxStaticText(self.notebook_1_pane_1, -1, "Name")
        self.sliceCursorNameCombo = wxComboBox(self.notebook_1_pane_1, -1, choices=["Point 1", "Point 2", "Point 3", "Point 4"], style=wxCB_DROPDOWN)
        self.sliceStoreButtonId  =  wxNewId()
        self.button_6_2 = wxButton(self.notebook_1_pane_1, self.sliceStoreButtonId , "Store this point")
        self.pointsGrid = wxGrid(self.notebook_1_pane_1, -1)
        self.label_5_1 = wxStaticText(self.notebook_1_pane_1, -1, "When I click on an object in the scene,")
        self.surfacePickActionChoice = wxChoice(self.notebook_1_pane_1, -1, choices=["do nothing.", "place a point on its surface.", "configure the object.", "show the scalar bar for its input."])
        self.objectsListGrid = wxGrid(self.notebook_1_pane_1, -1)
        self.label_1_2_copy = wxStaticText(self.notebook_1_pane_2, -1, "New implicit name")
        self.implicitNameText = wxTextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_4_2_copy = wxStaticText(self.notebook_1_pane_2, -1, "Type")
        self.implicitTypeChoice = wxChoice(self.notebook_1_pane_2, -1, choices=["choice 1"])
        self.createImplicitButtonId  =  wxNewId()
        self.button_6_2_copy = wxButton(self.notebook_1_pane_2, self.createImplicitButtonId , "Create")
        self.implicitsGrid = wxGrid(self.notebook_1_pane_2, -1)
        self.voiEnabledCheckBoxId  =  wxNewId()
        self.voiEnabledCheckBox = wxCheckBox(self.notebook_1_pane_2, self.voiEnabledCheckBoxId , "VOI extraction:")
        self.label_7 = wxStaticText(self.notebook_1_pane_2, -1, "Bounds")
        self.voiBoundsText = wxTextCtrl(self.notebook_1_pane_2, -1, "", style=wxTE_READONLY)
        self.label_7_1 = wxStaticText(self.notebook_1_pane_2, -1, "Discrete")
        self.voiExtentText = wxTextCtrl(self.notebook_1_pane_2, -1, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: controlFrame.__set_properties
        self.SetTitle("Slice3D Control")
        self.frame_4_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_4_statusbar_fields = ["All hail the mighty Slice3D Control!"]
        for i in range(len(frame_4_statusbar_fields)):
            self.frame_4_statusbar.SetStatusText(frame_4_statusbar_fields[i], i)
        self.createSliceComboBox.SetSelection(0)
        self.sliceGrid.CreateGrid(2, 3)
        self.sliceGrid.EnableEditing(0)
        self.sliceGrid.EnableDragRowSize(0)
        self.sliceGrid.EnableDragGridSize(0)
        self.sliceGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.sliceGrid.SetColLabelValue(0, "Slice name")
        self.sliceGrid.SetColLabelValue(1, "Enabled")
        self.sliceGrid.SetColLabelValue(2, "Interaction")
        self.sliceGrid.SetSize((500, 125))
        self.sliceCursorNameCombo.SetSelection(0)
        self.pointsGrid.CreateGrid(2, 3)
        self.pointsGrid.SetRowLabelSize(30)
        self.pointsGrid.EnableEditing(0)
        self.pointsGrid.EnableDragRowSize(0)
        self.pointsGrid.EnableDragGridSize(0)
        self.pointsGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.pointsGrid.SetColLabelValue(0, "World")
        self.pointsGrid.SetColSize(0, 200)
        self.pointsGrid.SetColLabelValue(1, "Discrete")
        self.pointsGrid.SetColLabelValue(2, "Value")
        self.pointsGrid.SetSize((500, 150))
        self.surfacePickActionChoice.SetSize((200, 34))
        self.surfacePickActionChoice.SetSelection(0)
        self.objectsListGrid.CreateGrid(2, 5)
        self.objectsListGrid.EnableEditing(0)
        self.objectsListGrid.EnableDragRowSize(0)
        self.objectsListGrid.EnableDragGridSize(0)
        self.objectsListGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.objectsListGrid.SetColLabelValue(0, "Object Name")
        self.objectsListGrid.SetColLabelValue(1, "Colour")
        self.objectsListGrid.SetColLabelValue(2, "Visible")
        self.objectsListGrid.SetColLabelValue(3, "Contour")
        self.objectsListGrid.SetColLabelValue(4, "Motion")
        self.objectsListGrid.SetSize((500, 125))
        self.implicitTypeChoice.SetSelection(0)
        self.implicitsGrid.CreateGrid(2, 4)
        self.implicitsGrid.EnableEditing(0)
        self.implicitsGrid.EnableDragRowSize(0)
        self.implicitsGrid.EnableDragGridSize(0)
        self.implicitsGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.implicitsGrid.SetColLabelValue(0, "Name")
        self.implicitsGrid.SetColLabelValue(1, "Type")
        self.implicitsGrid.SetColLabelValue(2, "Enabled")
        self.implicitsGrid.SetColLabelValue(3, "Interaction")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: controlFrame.__do_layout
        sizer_16 = wxBoxSizer(wxVERTICAL)
        sizer_3 = wxBoxSizer(wxVERTICAL)
        sizer_14 = wxBoxSizer(wxVERTICAL)
        sizer_23 = wxBoxSizer(wxVERTICAL)
        sizer_24 = wxBoxSizer(wxVERTICAL)
        sizer_20 = wxStaticBoxSizer(wxStaticBox(self.notebook_1_pane_2, -1, "Miscellaneous"), wxVERTICAL)
        sizer_21 = wxBoxSizer(wxHORIZONTAL)
        sizer_25 = wxStaticBoxSizer(wxStaticBox(self.notebook_1_pane_2, -1, "Implicits"), wxVERTICAL)
        selectedPointsCursorSizer_copy = wxBoxSizer(wxHORIZONTAL)
        sizer_22 = wxBoxSizer(wxVERTICAL)
        sizer_19 = wxStaticBoxSizer(wxStaticBox(self.notebook_1_pane_1, -1, "Objects"), wxVERTICAL)
        sizer_13 = wxBoxSizer(wxHORIZONTAL)
        sizer_17 = wxStaticBoxSizer(wxStaticBox(self.notebook_1_pane_1, -1, "Selected Points"), wxVERTICAL)
        selectedPointsCursorSizer = wxBoxSizer(wxHORIZONTAL)
        sizer_18 = wxStaticBoxSizer(wxStaticBox(self.notebook_1_pane_1, -1, "Slices"), wxVERTICAL)
        sizer_7 = wxBoxSizer(wxHORIZONTAL)
        label_2 = wxStaticText(self.notebook_1_pane_1, -1, "New slice name:")
        sizer_7.Add(label_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_7.Add(self.createSliceComboBox, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_7.Add(self.button_2_2, 0, wxALIGN_CENTER_VERTICAL, 7)
        sizer_7.Add((100, 20), 0, 0, 0)
        sizer_18.Add(sizer_7, 0, wxALL|wxEXPAND, 4)
        sizer_18.Add(self.sliceGrid, 1, wxEXPAND, 4)
        sizer_22.Add(sizer_18, 0, wxLEFT|wxRIGHT|wxTOP, 7)
        selectedPointsCursorSizer.Add(self.label_1_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer.Add(self.sliceCursorText, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer.Add(self.label_4_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer.Add(self.sliceCursorNameCombo, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer.Add(self.button_6_2, 0, wxEXPAND, 0)
        sizer_17.Add(selectedPointsCursorSizer, 0, wxALL|wxEXPAND, 4)
        sizer_17.Add(self.pointsGrid, 1, wxEXPAND, 4)
        sizer_22.Add(sizer_17, 0, wxLEFT|wxRIGHT|wxTOP, 7)
        sizer_13.Add(self.label_5_1, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_13.Add(self.surfacePickActionChoice, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(sizer_13, 0, wxALL, 4)
        sizer_19.Add(self.objectsListGrid, 0, 0, 4)
        sizer_22.Add(sizer_19, 0, wxLEFT|wxRIGHT|wxTOP, 7)
        self.notebook_1_pane_1.SetAutoLayout(1)
        self.notebook_1_pane_1.SetSizer(sizer_22)
        sizer_22.Fit(self.notebook_1_pane_1)
        sizer_22.SetSizeHints(self.notebook_1_pane_1)
        selectedPointsCursorSizer_copy.Add(self.label_1_2_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer_copy.Add(self.implicitNameText, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer_copy.Add(self.label_4_2_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer_copy.Add(self.implicitTypeChoice, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 7)
        selectedPointsCursorSizer_copy.Add(self.button_6_2_copy, 0, wxEXPAND, 0)
        sizer_25.Add(selectedPointsCursorSizer_copy, 0, wxALL|wxEXPAND, 4)
        sizer_25.Add(self.implicitsGrid, 1, wxEXPAND, 0)
        sizer_24.Add(sizer_25, 1, wxBOTTOM|wxEXPAND, 7)
        sizer_21.Add(self.voiEnabledCheckBox, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.label_7, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_21.Add(self.voiBoundsText, 1, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_21.Add(self.label_7_1, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_21.Add(self.voiExtentText, 1, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_20.Add(sizer_21, 0, wxALL|wxEXPAND, 4)
        sizer_24.Add(sizer_20, 0, wxEXPAND, 7)
        sizer_23.Add(sizer_24, 1, wxALL|wxEXPAND, 7)
        self.notebook_1_pane_2.SetAutoLayout(1)
        self.notebook_1_pane_2.SetSizer(sizer_23)
        sizer_23.Fit(self.notebook_1_pane_2)
        sizer_23.SetSizeHints(self.notebook_1_pane_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Main")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Widgets")
        sizer_14.Add(wxNotebookSizer(self.notebook_1), 1, wxEXPAND|wxADJUST_MINSIZE, 0)
        sizer_3.Add(sizer_14, 1, wxALL|wxEXPAND, 7)
        self.panel_3.SetAutoLayout(1)
        self.panel_3.SetSizer(sizer_3)
        sizer_3.Fit(self.panel_3)
        sizer_3.SetSizeHints(self.panel_3)
        sizer_16.Add(self.panel_3, 0, 0, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_16)
        sizer_16.Fit(self)
        sizer_16.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class controlFrame


class objectAnimationFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: objectAnimationFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_4 = wxPanel(self, -1)
        self.resetButtonId  =  wxNewId()
        self.button_3 = wxButton(self.panel_4, self.resetButtonId , "Reset")
        self.frameSliderId  =  wxNewId()
        self.frameSlider = wxSlider(self.panel_4, self.frameSliderId , 0, 0, 10)
        self.label_1 = wxStaticText(self.panel_4, -1, "Objects per Frame")
        self.objectsPerFrameSpinCtrl = wxSpinCtrl(self.panel_4, -1, "1", min=0, max=5)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: objectAnimationFrame.__set_properties
        self.SetTitle("frame_3")
        self.frameSlider.SetSize((250, 15))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: objectAnimationFrame.__do_layout
        sizer_6 = wxBoxSizer(wxVERTICAL)
        sizer_9 = wxBoxSizer(wxVERTICAL)
        sizer_10 = wxBoxSizer(wxVERTICAL)
        sizer_12 = wxBoxSizer(wxHORIZONTAL)
        sizer_11 = wxBoxSizer(wxHORIZONTAL)
        sizer_11.Add(self.button_3, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 7)
        sizer_11.Add(self.frameSlider, 1, wxALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(sizer_11, 1, wxBOTTOM|wxEXPAND, 7)
        sizer_12.Add(self.label_1, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_12.Add(self.objectsPerFrameSpinCtrl, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(sizer_12, 1, wxEXPAND, 0)
        sizer_9.Add(sizer_10, 1, wxALL|wxEXPAND, 7)
        self.panel_4.SetAutoLayout(1)
        self.panel_4.SetSizer(sizer_9)
        sizer_9.Fit(self.panel_4)
        sizer_9.SetSizeHints(self.panel_4)
        sizer_6.Add(self.panel_4, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_6)
        sizer_6.Fit(self)
        sizer_6.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class objectAnimationFrame


