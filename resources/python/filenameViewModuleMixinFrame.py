#!/usr/bin/env python
# generated by wxGlade 0.2.1cvs on Wed Jan 22 15:57:42 2003

from wxPython.wx import *

class filenameViewModuleMixinFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: filenameViewModuleMixinFrame.__init__
        kwds["style"] = wxCAPTION|wxMINIMIZE_BOX|wxMAXIMIZE_BOX|wxSYSTEM_MENU|wxRESIZE_BORDER
        wxFrame.__init__(self, *args, **kwds)
        self.viewFramePanel = wxPanel(self, -1)
        self.label_8_copy_1 = wxStaticText(self.viewFramePanel, -1, "Filename")
        self.filenameText = wxTextCtrl(self.viewFramePanel, -1, "")
        self.browseButtonId  =  wxNewId()
        self.browseButton = wxButton(self.viewFramePanel, self.browseButtonId , "Browse")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: filenameViewModuleMixinFrame.__set_properties
        self.SetTitle("SomeModule")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: filenameViewModuleMixinFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_5 = wxBoxSizer(wxVERTICAL)
        sizer_3 = wxBoxSizer(wxHORIZONTAL)
        sizer_3.Add(self.label_8_copy_1, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_3.Add(self.filenameText, 1, wxALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.browseButton, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_3, 1, wxALL|wxEXPAND, 5)
        self.viewFramePanel.SetAutoLayout(1)
        self.viewFramePanel.SetSizer(sizer_5)
        sizer_5.Fit(self.viewFramePanel)
        sizer_5.SetSizeHints(self.viewFramePanel)
        sizer_1.Add(self.viewFramePanel, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class filenameViewModuleMixinFrame


