# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joncrall/code/hotspotter/_frontend/MainSkel.ui'
#
# Created: Thu Dec 19 15:59:49 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainSkel(object):
    def setupUi(self, mainSkel):
        mainSkel.setObjectName(_fromUtf8("mainSkel"))
        mainSkel.resize(927, 573)
        self.centralwidget = QtGui.QWidget(mainSkel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.root_hlayout = QtGui.QHBoxLayout()
        self.root_hlayout.setObjectName(_fromUtf8("root_hlayout"))
        self.tablesTabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablesTabWidget.sizePolicy().hasHeightForWidth())
        self.tablesTabWidget.setSizePolicy(sizePolicy)
        self.tablesTabWidget.setObjectName(_fromUtf8("tablesTabWidget"))
        self.image_view = QtGui.QWidget()
        self.image_view.setMinimumSize(QtCore.QSize(445, 0))
        self.image_view.setObjectName(_fromUtf8("image_view"))
        self.gridLayout_3 = QtGui.QGridLayout(self.image_view)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.image_TBL = QtGui.QTableWidget(self.image_view)
        self.image_TBL.setObjectName(_fromUtf8("image_TBL"))
        self.image_TBL.setColumnCount(0)
        self.image_TBL.setRowCount(0)
        self.verticalLayout.addWidget(self.image_TBL)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tablesTabWidget.addTab(self.image_view, _fromUtf8(""))
        self.chip_view = QtGui.QWidget()
        self.chip_view.setObjectName(_fromUtf8("chip_view"))
        self.gridLayout_4 = QtGui.QGridLayout(self.chip_view)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chip_TBL = QtGui.QTableWidget(self.chip_view)
        self.chip_TBL.setObjectName(_fromUtf8("chip_TBL"))
        self.chip_TBL.setColumnCount(0)
        self.chip_TBL.setRowCount(0)
        self.verticalLayout_3.addWidget(self.chip_TBL)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tablesTabWidget.addTab(self.chip_view, _fromUtf8(""))
        self.result_view = QtGui.QWidget()
        self.result_view.setObjectName(_fromUtf8("result_view"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.result_view)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.res_TBL = QtGui.QTableWidget(self.result_view)
        self.res_TBL.setObjectName(_fromUtf8("res_TBL"))
        self.res_TBL.setColumnCount(0)
        self.res_TBL.setRowCount(0)
        self.verticalLayout_4.addWidget(self.res_TBL)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tablesTabWidget.addTab(self.result_view, _fromUtf8(""))
        self.root_hlayout.addWidget(self.tablesTabWidget)
        self.gridLayout_2.addLayout(self.root_hlayout, 1, 1, 1, 1)
        self.status_HLayout = QtGui.QHBoxLayout()
        self.status_HLayout.setObjectName(_fromUtf8("status_HLayout"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.status_HLayout.addWidget(self.progressBar)
        self.gridLayout_2.addLayout(self.status_HLayout, 2, 1, 1, 1)
        mainSkel.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainSkel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 927, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        self.menuBatch = QtGui.QMenu(self.menubar)
        self.menuBatch.setObjectName(_fromUtf8("menuBatch"))
        mainSkel.setMenuBar(self.menubar)
        self.actionOpen_Database = QtGui.QAction(mainSkel)
        self.actionOpen_Database.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen_Database.setObjectName(_fromUtf8("actionOpen_Database"))
        self.actionSave_Database = QtGui.QAction(mainSkel)
        self.actionSave_Database.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave_Database.setObjectName(_fromUtf8("actionSave_Database"))
        self.actionImport_Img_file = QtGui.QAction(mainSkel)
        self.actionImport_Img_file.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionImport_Img_file.setObjectName(_fromUtf8("actionImport_Img_file"))
        self.actionOpen_Data_Directory = QtGui.QAction(mainSkel)
        self.actionOpen_Data_Directory.setObjectName(_fromUtf8("actionOpen_Data_Directory"))
        self.actionOpen_Source_Directory = QtGui.QAction(mainSkel)
        self.actionOpen_Source_Directory.setObjectName(_fromUtf8("actionOpen_Source_Directory"))
        self.actionTogEll = QtGui.QAction(mainSkel)
        self.actionTogEll.setEnabled(True)
        self.actionTogEll.setObjectName(_fromUtf8("actionTogEll"))
        self.actionUndockDisplay = QtGui.QAction(mainSkel)
        self.actionUndockDisplay.setObjectName(_fromUtf8("actionUndockDisplay"))
        self.actionTogPlt = QtGui.QAction(mainSkel)
        self.actionTogPlt.setObjectName(_fromUtf8("actionTogPlt"))
        self.actionHelpCMD = QtGui.QAction(mainSkel)
        self.actionHelpCMD.setObjectName(_fromUtf8("actionHelpCMD"))
        self.actionHelpGUI = QtGui.QAction(mainSkel)
        self.actionHelpGUI.setObjectName(_fromUtf8("actionHelpGUI"))
        self.actionAbout = QtGui.QAction(mainSkel)
        self.actionAbout.setEnabled(False)
        self.actionAbout.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelpWorkflow = QtGui.QAction(mainSkel)
        self.actionHelpWorkflow.setObjectName(_fromUtf8("actionHelpWorkflow"))
        self.actionTogPts = QtGui.QAction(mainSkel)
        self.actionTogPts.setObjectName(_fromUtf8("actionTogPts"))
        self.actionAdd_Chip = QtGui.QAction(mainSkel)
        self.actionAdd_Chip.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAdd_Chip.setObjectName(_fromUtf8("actionAdd_Chip"))
        self.actionReselect_ROI = QtGui.QAction(mainSkel)
        self.actionReselect_ROI.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionReselect_ROI.setObjectName(_fromUtf8("actionReselect_ROI"))
        self.actionNext = QtGui.QAction(mainSkel)
        self.actionNext.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNext.setObjectName(_fromUtf8("actionNext"))
        self.actionDelete_Chip = QtGui.QAction(mainSkel)
        self.actionDelete_Chip.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_Chip.setObjectName(_fromUtf8("actionDelete_Chip"))
        self.actionQuery = QtGui.QAction(mainSkel)
        self.actionQuery.setEnabled(True)
        self.actionQuery.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionQuery.setObjectName(_fromUtf8("actionQuery"))
        self.actionPrev = QtGui.QAction(mainSkel)
        self.actionPrev.setObjectName(_fromUtf8("actionPrev"))
        self.actionWriteLogs = QtGui.QAction(mainSkel)
        self.actionWriteLogs.setEnabled(False)
        self.actionWriteLogs.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionWriteLogs.setObjectName(_fromUtf8("actionWriteLogs"))
        self.actionOpen_Internal_Directory = QtGui.QAction(mainSkel)
        self.actionOpen_Internal_Directory.setObjectName(_fromUtf8("actionOpen_Internal_Directory"))
        self.actionPreferences = QtGui.QAction(mainSkel)
        self.actionPreferences.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionQuit = QtGui.QAction(mainSkel)
        self.actionQuit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionConvertImage2Chip = QtGui.QAction(mainSkel)
        self.actionConvertImage2Chip.setEnabled(True)
        self.actionConvertImage2Chip.setObjectName(_fromUtf8("actionConvertImage2Chip"))
        self.actionBatch_Change_Name = QtGui.QAction(mainSkel)
        self.actionBatch_Change_Name.setObjectName(_fromUtf8("actionBatch_Change_Name"))
        self.actionReselect_Ori = QtGui.QAction(mainSkel)
        self.actionReselect_Ori.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionReselect_Ori.setObjectName(_fromUtf8("actionReselect_Ori"))
        self.actionAdd_Metadata_Property = QtGui.QAction(mainSkel)
        self.actionAdd_Metadata_Property.setObjectName(_fromUtf8("actionAdd_Metadata_Property"))
        self.actionAutoassign = QtGui.QAction(mainSkel)
        self.actionAutoassign.setObjectName(_fromUtf8("actionAutoassign"))
        self.actionRankErrorExpt = QtGui.QAction(mainSkel)
        self.actionRankErrorExpt.setObjectName(_fromUtf8("actionRankErrorExpt"))
        self.actionName_Consistency_Experiment = QtGui.QAction(mainSkel)
        self.actionName_Consistency_Experiment.setObjectName(_fromUtf8("actionName_Consistency_Experiment"))
        self.actionIncrease_ROI_Size = QtGui.QAction(mainSkel)
        self.actionIncrease_ROI_Size.setObjectName(_fromUtf8("actionIncrease_ROI_Size"))
        self.actionView_Docs = QtGui.QAction(mainSkel)
        self.actionView_Docs.setEnabled(False)
        self.actionView_Docs.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_Docs.setObjectName(_fromUtf8("actionView_Docs"))
        self.actionAutoassign_2 = QtGui.QAction(mainSkel)
        self.actionAutoassign_2.setObjectName(_fromUtf8("actionAutoassign_2"))
        self.actionNew_Database = QtGui.QAction(mainSkel)
        self.actionNew_Database.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNew_Database.setObjectName(_fromUtf8("actionNew_Database"))
        self.actionImport_Img_dir = QtGui.QAction(mainSkel)
        self.actionImport_Img_dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionImport_Img_dir.setObjectName(_fromUtf8("actionImport_Img_dir"))
        self.actionPrecompute_Queries = QtGui.QAction(mainSkel)
        self.actionPrecompute_Queries.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPrecompute_Queries.setObjectName(_fromUtf8("actionPrecompute_Queries"))
        self.actionPrecomputeChipsFeatures = QtGui.QAction(mainSkel)
        self.actionPrecomputeChipsFeatures.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPrecomputeChipsFeatures.setObjectName(_fromUtf8("actionPrecomputeChipsFeatures"))
        self.actionView_DBDir = QtGui.QAction(mainSkel)
        self.actionView_DBDir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_DBDir.setObjectName(_fromUtf8("actionView_DBDir"))
        self.actionScale_all_ROIS = QtGui.QAction(mainSkel)
        self.actionScale_all_ROIS.setEnabled(False)
        self.actionScale_all_ROIS.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionScale_all_ROIS.setObjectName(_fromUtf8("actionScale_all_ROIS"))
        self.actionConvert_all_images_into_chips = QtGui.QAction(mainSkel)
        self.actionConvert_all_images_into_chips.setEnabled(False)
        self.actionConvert_all_images_into_chips.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionConvert_all_images_into_chips.setObjectName(_fromUtf8("actionConvert_all_images_into_chips"))
        self.actionNew_Chip_Property = QtGui.QAction(mainSkel)
        self.actionNew_Chip_Property.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNew_Chip_Property.setObjectName(_fromUtf8("actionNew_Chip_Property"))
        self.actionDelete_computed_directory = QtGui.QAction(mainSkel)
        self.actionDelete_computed_directory.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_computed_directory.setObjectName(_fromUtf8("actionDelete_computed_directory"))
        self.actionDelete_global_preferences = QtGui.QAction(mainSkel)
        self.actionDelete_global_preferences.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_global_preferences.setObjectName(_fromUtf8("actionDelete_global_preferences"))
        self.actionView_Computed_Dir = QtGui.QAction(mainSkel)
        self.actionView_Computed_Dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_Computed_Dir.setObjectName(_fromUtf8("actionView_Computed_Dir"))
        self.actionView_Global_Dir = QtGui.QAction(mainSkel)
        self.actionView_Global_Dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_Global_Dir.setObjectName(_fromUtf8("actionView_Global_Dir"))
        self.actionLayout_Figures = QtGui.QAction(mainSkel)
        self.actionLayout_Figures.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionLayout_Figures.setObjectName(_fromUtf8("actionLayout_Figures"))
        self.actionDev_Mode_IPython = QtGui.QAction(mainSkel)
        self.actionDev_Mode_IPython.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDev_Mode_IPython.setObjectName(_fromUtf8("actionDev_Mode_IPython"))
        self.menuFile.addAction(self.actionNew_Database)
        self.menuFile.addAction(self.actionOpen_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Img_file)
        self.menuFile.addAction(self.actionImport_Img_dir)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuOptions.addAction(self.actionLayout_Figures)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionView_Docs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionView_DBDir)
        self.menuHelp.addAction(self.actionView_Computed_Dir)
        self.menuHelp.addAction(self.actionView_Global_Dir)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionWriteLogs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDelete_computed_directory)
        self.menuHelp.addAction(self.actionDelete_global_preferences)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDev_Mode_IPython)
        self.menuActions.addAction(self.actionAdd_Chip)
        self.menuActions.addAction(self.actionNew_Chip_Property)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionQuery)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionReselect_ROI)
        self.menuActions.addAction(self.actionReselect_Ori)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionNext)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionDelete_Chip)
        self.menuBatch.addAction(self.actionPrecomputeChipsFeatures)
        self.menuBatch.addAction(self.actionPrecompute_Queries)
        self.menuBatch.addSeparator()
        self.menuBatch.addAction(self.actionScale_all_ROIS)
        self.menuBatch.addSeparator()
        self.menuBatch.addAction(self.actionConvert_all_images_into_chips)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuBatch.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainSkel)
        self.tablesTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainSkel)

    def retranslateUi(self, mainSkel):
        mainSkel.setWindowTitle(QtGui.QApplication.translate("mainSkel", "HotSpotter", None, QtGui.QApplication.UnicodeUTF8))
        self.image_TBL.setSortingEnabled(True)
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.image_view), QtGui.QApplication.translate("mainSkel", "Image Table", None, QtGui.QApplication.UnicodeUTF8))
        self.chip_TBL.setSortingEnabled(True)
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.chip_view), QtGui.QApplication.translate("mainSkel", "Chip Table", None, QtGui.QApplication.UnicodeUTF8))
        self.res_TBL.setSortingEnabled(True)
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.result_view), QtGui.QApplication.translate("mainSkel", "Results Table", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainSkel", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("mainSkel", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainSkel", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("mainSkel", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBatch.setTitle(QtGui.QApplication.translate("mainSkel", "Batch", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Database.setText(QtGui.QApplication.translate("mainSkel", "Open Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Database.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Database.setText(QtGui.QApplication.translate("mainSkel", "Save Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Database.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Img_file.setText(QtGui.QApplication.translate("mainSkel", "Import Images (select file)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Img_file.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Data_Directory.setText(QtGui.QApplication.translate("mainSkel", "View Data Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Source_Directory.setText(QtGui.QApplication.translate("mainSkel", "View Source Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogEll.setText(QtGui.QApplication.translate("mainSkel", "Toggle Ellipses", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogEll.setShortcut(QtGui.QApplication.translate("mainSkel", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndockDisplay.setText(QtGui.QApplication.translate("mainSkel", "Undock Display", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogPlt.setText(QtGui.QApplication.translate("mainSkel", "Toggle PlotWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpCMD.setText(QtGui.QApplication.translate("mainSkel", "Command Line Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpGUI.setText(QtGui.QApplication.translate("mainSkel", "GUI Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainSkel", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpWorkflow.setText(QtGui.QApplication.translate("mainSkel", "Workflow Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogPts.setText(QtGui.QApplication.translate("mainSkel", "Toggle Points", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogPts.setShortcut(QtGui.QApplication.translate("mainSkel", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Chip.setText(QtGui.QApplication.translate("mainSkel", "Add Chip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Chip.setShortcut(QtGui.QApplication.translate("mainSkel", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReselect_ROI.setText(QtGui.QApplication.translate("mainSkel", "Reselect ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReselect_ROI.setShortcut(QtGui.QApplication.translate("mainSkel", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setText(QtGui.QApplication.translate("mainSkel", "Select Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setToolTip(QtGui.QApplication.translate("mainSkel", "Selects the next unidentified CID or Untagged GID", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setShortcut(QtGui.QApplication.translate("mainSkel", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Chip.setText(QtGui.QApplication.translate("mainSkel", "Delete Chip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Chip.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuery.setText(QtGui.QApplication.translate("mainSkel", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuery.setShortcut(QtGui.QApplication.translate("mainSkel", "Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrev.setText(QtGui.QApplication.translate("mainSkel", "Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWriteLogs.setText(QtGui.QApplication.translate("mainSkel", "Write Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Internal_Directory.setText(QtGui.QApplication.translate("mainSkel", "View Internal Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("mainSkel", "Edit Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("mainSkel", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvertImage2Chip.setText(QtGui.QApplication.translate("mainSkel", "Convert All Images to Chips", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBatch_Change_Name.setText(QtGui.QApplication.translate("mainSkel", "Batch Change Name", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReselect_Ori.setText(QtGui.QApplication.translate("mainSkel", "Reselect Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReselect_Ori.setShortcut(QtGui.QApplication.translate("mainSkel", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Metadata_Property.setText(QtGui.QApplication.translate("mainSkel", "Add Chip Property", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoassign.setText(QtGui.QApplication.translate("mainSkel", "Assign Matches Above Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRankErrorExpt.setText(QtGui.QApplication.translate("mainSkel", "Rank Error Experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionName_Consistency_Experiment.setText(QtGui.QApplication.translate("mainSkel", "Name Consistency", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_ROI_Size.setText(QtGui.QApplication.translate("mainSkel", "Increase all ROI Sizes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Docs.setText(QtGui.QApplication.translate("mainSkel", "View Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoassign_2.setText(QtGui.QApplication.translate("mainSkel", "Auto-Assign Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Database.setText(QtGui.QApplication.translate("mainSkel", "New Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Database.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Img_dir.setText(QtGui.QApplication.translate("mainSkel", "Import Images (select directory)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrecompute_Queries.setText(QtGui.QApplication.translate("mainSkel", "Precompute Queries", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrecomputeChipsFeatures.setText(QtGui.QApplication.translate("mainSkel", "Precompute Chips/Features", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrecomputeChipsFeatures.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Return", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_DBDir.setText(QtGui.QApplication.translate("mainSkel", "View Database Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScale_all_ROIS.setText(QtGui.QApplication.translate("mainSkel", "Scale all ROIs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert_all_images_into_chips.setText(QtGui.QApplication.translate("mainSkel", "Convert all images into chips", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Chip_Property.setText(QtGui.QApplication.translate("mainSkel", "New Chip Property", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_computed_directory.setText(QtGui.QApplication.translate("mainSkel", "Delete Computed Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_global_preferences.setText(QtGui.QApplication.translate("mainSkel", "Delete Global Prefs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Computed_Dir.setText(QtGui.QApplication.translate("mainSkel", "View Computed Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Global_Dir.setText(QtGui.QApplication.translate("mainSkel", "View Global Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLayout_Figures.setText(QtGui.QApplication.translate("mainSkel", "Layout Figures", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLayout_Figures.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDev_Mode_IPython.setText(QtGui.QApplication.translate("mainSkel", "Developer Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDev_Mode_IPython.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Alt+Shift+D", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainSkel = QtGui.QMainWindow()
    ui = Ui_mainSkel()
    ui.setupUi(mainSkel)
    mainSkel.show()
    sys.exit(app.exec_())

