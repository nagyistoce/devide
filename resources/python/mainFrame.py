#!/usr/bin/env python
# generated by wxGlade 0.2.1cvs on Thu Jan 23 15:01:14 2003

from wxPython.wx import *

class mainFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: mainFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_1 = wxPanel(self, -1)
        self.frame_1_statusbar = self.CreateStatusBar(1)
        
        # Menu Bar
        self.frame_1_menubar = wxMenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.fileExitId  =  wxNewId()
        self.windowGraphEditorId  =  wxNewId()
        self.windowPythonShellId  =  wxNewId()
        self.helpContentsId  =  wxNewId()
        self.helpAboutId  =  wxNewId()
        wxglade_tmp_menu = wxMenu()
        wxglade_tmp_menu.Append(self.fileExitId , "E&xit", "Exit DSCAS", wxITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wxMenu()
        wxglade_tmp_menu.Append(self.windowGraphEditorId , "&Graph Editor", "Open up the graph editor window", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.windowPythonShellId , "&Python Shell", "Show the Python Shell interface", wxITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&Window")
        wxglade_tmp_menu = wxMenu()
        wxglade_tmp_menu.Append(self.helpContentsId , "&Contents", "Show the main help contents", wxITEM_NORMAL)
        wxglade_tmp_menu.Append(self.helpAboutId , "&About", "Get information about DeVIDE", wxITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&Help")
        # Menu Bar end
        self.progressText = wxStaticText(self.panel_1, -1, "This is quite a long progress message so that even the longest of messages eek.")
        self.progressGauge = wxGauge(self.panel_1, -1, 100)
        self.progressRaiseCheckBox = wxCheckBox(self.panel_1, -1, "Raise this window when the progress is updated.")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: mainFrame.__set_properties
        self.SetTitle("DeVIDE main window")
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Welcome to DeVIDE"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.progressText.SetFont(wxFont(12, wxDEFAULT, wxNORMAL, wxNORMAL, 0, ""))
        self.progressGauge.SetBackgroundColour(wxColour(50, 50, 204))
        self.progressRaiseCheckBox.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: mainFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_3 = wxBoxSizer(wxVERTICAL)
        sizer_3.Add(self.progressText, 0, wxLEFT|wxRIGHT|wxTOP, 5)
        sizer_3.Add(self.progressGauge, 0, wxLEFT|wxRIGHT|wxEXPAND, 5)
        sizer_3.Add(self.progressRaiseCheckBox, 0, wxALL|wxEXPAND|wxALIGN_CENTER_VERTICAL, 5)
        self.panel_1.SetAutoLayout(1)
        self.panel_1.SetSizer(sizer_3)
        sizer_3.Fit(self.panel_1)
        sizer_3.SetSizeHints(self.panel_1)
        sizer_1.Add(self.panel_1, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class mainFrame


