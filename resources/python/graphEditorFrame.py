#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Thu Jan  5 14:24:58 2006

import wx

class graphEditorFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        # this is passed in by the calling code
        wxpcCanvas = kwds['wxpcCanvas']
        # we have to delete it from the keywords, some of the wrapped code
        # doesn't like it.
        del kwds['wxpcCanvas']
        
        # begin wxGlade: graphEditorFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.mainPanel = wx.Panel(self, -1)
        self.main_splitter = wx.SplitterWindow(self.mainPanel, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_1_pane_2 = wx.Panel(self.main_splitter, -1)
        self.window_1_pane_1 = wx.Panel(self.main_splitter, -1)
        self.module_palette_splitter = wx.SplitterWindow(self.window_1_pane_1, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_2_pane_2 = wx.Panel(self.module_palette_splitter, -1)
        self.window_2_pane_1 = wx.Panel(self.module_palette_splitter, -1)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.fileNewId = wx.NewId()
        self.fileOpenId = wx.NewId()
        self.fileOpenSegmentId = wx.NewId()
        self.fileSaveId = wx.NewId()
        self.fileSaveSelectedId = wx.NewId()
        self.fileExportAsDOTId = wx.NewId()
        self.fileExportSelectedAsDOTId = wx.NewId()
        self.fileExitId = wx.NewId()
        self.windowMainID = wx.NewId()
        self.helpShowHelpId = wx.NewId()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.fileNewId, "&New\tCtrl-N", "Create new network.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileOpenId, "&Open\tCtrl-O", "Open and load existing network.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileOpenSegmentId, "Open as Se&gment\tCtrl-G", "Open a DeVIDE network as a segment in the copy buffer.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileSaveId, "&Save\tCtrl-S", "Save the current network.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileSaveSelectedId, "Save se&lected Glyphs\tCtrl-L", "Save the selected glyphs as a network.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(self.fileExportAsDOTId, "&Export as DOT file\tCtrl-E", "Export the current network as a GraphViz DOT file.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.fileExportSelectedAsDOTId, "Export selection as DOT file", "Export the selected glyphs as a GraphViz DOT file.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(self.fileExitId, "E&xit\tCtrl-Q", "Exit DeVIDE!", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&File")
        self.editMenu = wx.Menu()
        self.frame_1_menubar.Append(self.editMenu, "&Edit")
        self.execution_menu = wx.Menu()
        self.frame_1_menubar.Append(self.execution_menu, "E&xecution")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.windowMainID, "&Main window", "Show the DeVIDE main window.", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&Window")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.helpShowHelpId, "Show &Help\tF1", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&Help")
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        self.label_2_copy = wx.StaticText(self.window_2_pane_1, -1, "Module Categories List")
        self.moduleCatsListBoxId = wx.NewId()
        self.moduleCatsListBox = wx.ListBox(self.window_2_pane_1, self.moduleCatsListBoxId, choices=[], style=wx.LB_EXTENDED|wx.LB_NEEDED_SB)
        self.label_1 = wx.StaticText(self.window_2_pane_2, -1, "Modules List")
        self.modulesListBoxId = wx.NewId()
        self.modulesListBox = wx.ListBox(self.window_2_pane_2, self.modulesListBoxId, choices=[], style=wx.LB_SINGLE|wx.LB_NEEDED_SB)
        self.rescanButtonId = wx.NewId()
        self.rescanButton = wx.Button(self.window_1_pane_1, self.rescanButtonId, "Rescan")
        self.canvas = wxpcCanvas(self.window_1_pane_2, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: graphEditorFrame.__set_properties
        self.SetTitle("DeVIDE Graph Editor Canvas")
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Welcome to the DeVIDE Graph Editor"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: graphEditorFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_12.Add((0, 150), 0, wx.ADJUST_MINSIZE, 0)
        sizer_12_copy.Add(self.label_2_copy, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 4)
        sizer_12_copy.Add(self.moduleCatsListBox, 1, wx.EXPAND, 0)
        sizer_12.Add(sizer_12_copy, 1, wx.EXPAND, 0)
        self.window_2_pane_1.SetAutoLayout(True)
        self.window_2_pane_1.SetSizer(sizer_12)
        sizer_12.Fit(self.window_2_pane_1)
        sizer_12.SetSizeHints(self.window_2_pane_1)
        sizer_13.Add((0, 150), 0, wx.ADJUST_MINSIZE, 0)
        sizer_7.Add(self.label_1, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 4)
        sizer_7.Add(self.modulesListBox, 1, wx.EXPAND, 0)
        sizer_13.Add(sizer_7, 1, wx.EXPAND, 0)
        self.window_2_pane_2.SetAutoLayout(True)
        self.window_2_pane_2.SetSizer(sizer_13)
        sizer_13.Fit(self.window_2_pane_2)
        sizer_13.SetSizeHints(self.window_2_pane_2)
        self.module_palette_splitter.SplitHorizontally(self.window_2_pane_1, self.window_2_pane_2)
        sizer_10.Add(self.module_palette_splitter, 1, wx.EXPAND, 0)
        sizer_10.Add(self.rescanButton, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 7)
        sizer_10.Add((150, 0), 0, wx.ADJUST_MINSIZE, 0)
        self.window_1_pane_1.SetAutoLayout(True)
        self.window_1_pane_1.SetSizer(sizer_10)
        sizer_10.Fit(self.window_1_pane_1)
        sizer_10.SetSizeHints(self.window_1_pane_1)
        sizer_8.Add(self.canvas, 1, wx.EXPAND, 0)
        sizer_8.Add((400, 0), 0, 0, 0)
        self.window_1_pane_2.SetAutoLayout(True)
        self.window_1_pane_2.SetSizer(sizer_8)
        sizer_8.Fit(self.window_1_pane_2)
        sizer_8.SetSizeHints(self.window_1_pane_2)
        self.main_splitter.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 152)
        sizer_2.Add(self.main_splitter, 1, wx.EXPAND, 0)
        sizer_2.Add((0, 400), 0, 0, 0)
        sizer_6.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_6, 1, wx.ALL|wx.EXPAND, 7)
        self.mainPanel.SetAutoLayout(True)
        self.mainPanel.SetSizer(sizer_5)
        sizer_5.Fit(self.mainPanel)
        sizer_5.SetSizeHints(self.mainPanel)
        sizer_1.Add(self.mainPanel, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class graphEditorFrame


