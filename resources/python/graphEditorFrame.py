#!/usr/bin/env python
# generated by wxGlade 0.2.1cvs on Sun Jan 26 01:49:36 2003

from wxPython.wx import *

class canvasFrame(wxFrame):
    def __init__(self, *args, **kwds):
	# this class gets passed in as keyword argument (neat huh?)
	wxpcCanvas = kwds['wxpcCanvas']
	# I have to delete it from the keywords, because some of the wrapped
	# code doesn't like it
	del kwds['wxpcCanvas']
        
        # begin wxGlade: canvasFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.mainPanel = wxPanel(self, -1)
        
        # Menu Bar
        self.frame_1_menubar = wxMenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.fileNewId = wxNewId()
        self.fileOpenId = wxNewId()
        self.fileOpenSegmentId = wxNewId()
        self.fileSaveId = wxNewId()
        self.fileSaveSelectedId = wxNewId()
        self.fileExportAsDOTId = wxNewId()
        self.fileExportSelectedAsDOTId = wxNewId()
        self.fileExitId = wxNewId()
        self.helpShowHelpId = wxNewId()
        wxglade_tmp_menu = wxMenu()
        wxglade_tmp_menu.Append(self.fileNewId, "&New\tCtrl-N", "Create new network.", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileOpenId, "&Open\tCtrl-O", "Open and load existing network.", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileOpenSegmentId, "Open as Se&gment\tCtrl-G", "Open a DeVIDE network as a segment in the copy buffer.", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileSaveId, "&Save\tCtrl-S", "Save the current network.", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileSaveSelectedId, "Save se&lected Glyphs\tCtrl-L", "Save the selected glyphs as a network.", wxITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(self.fileExportAsDOTId, "&Export as DOT file\tCtrl-E", "Export the current network as a GraphViz DOT file.", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileExportSelectedAsDOTId, "Export selection as DOT file", "Export the selected glyphs as a GraphViz DOT file.", wxITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(self.fileExitId, "E&xit\tCtrl-Q", "Exit DeVIDE!", wxITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&File")
        self.editMenu = wxMenu()
        self.frame_1_menubar.Append(self.editMenu, "&Edit")
        wxglade_tmp_menu = wxMenu()
        wxglade_tmp_menu.Append(self.helpShowHelpId, "Show &Help\tF1", "", wxITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&Help")
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        self.canvas = wxpcCanvas(self.mainPanel, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: canvasFrame.__set_properties
        self.SetTitle("DeVIDE Graph Editor Canvas")
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Welcome to the DeVIDE Graph Editor"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: canvasFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_5 = wxBoxSizer(wxVERTICAL)
        sizer_6 = wxBoxSizer(wxVERTICAL)
        sizer_2 = wxBoxSizer(wxHORIZONTAL)
        sizer_8 = wxBoxSizer(wxVERTICAL)
        sizer_8.Add(self.canvas, 1, wxEXPAND, 0)
        sizer_8.Add((640, 0), 0, 0, 0)
        sizer_2.Add(sizer_8, 9, wxEXPAND, 0)
        sizer_2.Add((0, 480), 0, 0, 0)
        sizer_6.Add(sizer_2, 1, wxEXPAND, 0)
        sizer_5.Add(sizer_6, 1, wxALL|wxEXPAND, 7)
        self.mainPanel.SetAutoLayout(True)
        self.mainPanel.SetSizer(sizer_5)
        sizer_5.Fit(self.mainPanel)
        sizer_5.SetSizeHints(self.mainPanel)
        sizer_1.Add(self.mainPanel, 1, wxEXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class canvasFrame


class modulePaletteFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: modulePaletteFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_1 = wxPanel(self, -1)
        self.window_1 = wxSplitterWindow(self.panel_1, -1)
        self.window_1_pane_2 = wxPanel(self.window_1, -1)
        self.window_1_pane_1 = wxPanel(self.window_1, -1)
        self.moduleCatsListCtrlId = wxNewId()
        self.moduleCatsListCtrl = wxListCtrl(self.window_1_pane_1, self.moduleCatsListCtrlId, style=wxLC_REPORT|wxSUNKEN_BORDER)
        self.modulesListCtrlId = wxNewId()
        self.modulesListCtrl = wxListCtrl(self.window_1_pane_2, self.modulesListCtrlId, style=wxLC_REPORT|wxLC_SINGLE_SEL|wxSUNKEN_BORDER)
        self.rescanButtonId = wxNewId()
        self.rescanButton = wxButton(self.panel_1, self.rescanButtonId, "Rescan")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: modulePaletteFrame.__set_properties
        self.SetTitle("DeVIDE Graph Editor Module Palette")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: modulePaletteFrame.__do_layout
        sizer_3 = wxBoxSizer(wxVERTICAL)
        sizer_4 = wxBoxSizer(wxVERTICAL)
        sizer_11 = wxBoxSizer(wxHORIZONTAL)
        sizer_9 = wxBoxSizer(wxVERTICAL)
        sizer_11_copy = wxBoxSizer(wxHORIZONTAL)
        sizer_10 = wxBoxSizer(wxHORIZONTAL)
        sizer_10.Add(self.moduleCatsListCtrl, 1, wxEXPAND, 0)
        self.window_1_pane_1.SetAutoLayout(True)
        self.window_1_pane_1.SetSizer(sizer_10)
        sizer_10.Fit(self.window_1_pane_1)
        sizer_10.SetSizeHints(self.window_1_pane_1)
        sizer_11_copy.Add(self.modulesListCtrl, 1, wxEXPAND, 0)
        self.window_1_pane_2.SetAutoLayout(True)
        self.window_1_pane_2.SetSizer(sizer_11_copy)
        sizer_11_copy.Fit(self.window_1_pane_2)
        sizer_11_copy.SetSizeHints(self.window_1_pane_2)
        self.window_1.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2, 156)
        sizer_9.Add(self.window_1, 1, wxEXPAND, 0)
        sizer_9.Add((150, 0), 0, 0, 0)
        sizer_9.Add(self.rescanButton, 0, wxTOP|wxBOTTOM|wxALIGN_CENTER_HORIZONTAL, 7)
        sizer_11.Add(sizer_9, 1, wxEXPAND, 0)
        sizer_11.Add((0, 480), 0, 0, 0)
        sizer_4.Add(sizer_11, 1, wxALL|wxEXPAND, 7)
        self.panel_1.SetAutoLayout(True)
        self.panel_1.SetSizer(sizer_4)
        sizer_4.Fit(self.panel_1)
        sizer_4.SetSizeHints(self.panel_1)
        sizer_3.Add(self.panel_1, 1, wxEXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        sizer_3.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class modulePaletteFrame


