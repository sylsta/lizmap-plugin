# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lizmap.ui'
#
# Created: Mon Jan 14 14:57:19 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_lizmap(object):
    def setupUi(self, lizmap):
        lizmap.setObjectName(_fromUtf8("lizmap"))
        lizmap.resize(1001, 604)
        self.gridLayout = QtGui.QGridLayout(lizmap)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonClose = QtGui.QDialogButtonBox(lizmap)
        self.buttonClose.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.gridLayout.addWidget(self.buttonClose, 4, 8, 1, 1)
        self.btSync = QtGui.QPushButton(lizmap)
        self.btSync.setEnabled(True)
        self.btSync.setObjectName(_fromUtf8("btSync"))
        self.gridLayout.addWidget(self.btSync, 1, 8, 1, 1)
        self.tabWidget = QtGui.QTabWidget(lizmap)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.inLayerTitle = QtGui.QLineEdit(self.tab_2)
        self.inLayerTitle.setObjectName(_fromUtf8("inLayerTitle"))
        self.verticalLayout.addWidget(self.inLayerTitle)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.teLayerAbstract = QtGui.QTextEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teLayerAbstract.sizePolicy().hasHeightForWidth())
        self.teLayerAbstract.setSizePolicy(sizePolicy)
        self.teLayerAbstract.setObjectName(_fromUtf8("teLayerAbstract"))
        self.verticalLayout.addWidget(self.teLayerAbstract)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.inLayerLink = QtGui.QLineEdit(self.tab_2)
        self.inLayerLink.setObjectName(_fromUtf8("inLayerLink"))
        self.verticalLayout.addWidget(self.inLayerLink)
        self.cbToggled = QtGui.QCheckBox(self.tab_2)
        self.cbToggled.setObjectName(_fromUtf8("cbToggled"))
        self.verticalLayout.addWidget(self.cbToggled)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.cbPopup = QtGui.QCheckBox(self.tab_2)
        self.cbPopup.setObjectName(_fromUtf8("cbPopup"))
        self.horizontalLayout_7.addWidget(self.cbPopup)
        self.btConfigurePopup = QtGui.QPushButton(self.tab_2)
        self.btConfigurePopup.setObjectName(_fromUtf8("btConfigurePopup"))
        self.horizontalLayout_7.addWidget(self.btConfigurePopup)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.cbGroupAsLayer = QtGui.QCheckBox(self.tab_2)
        self.cbGroupAsLayer.setObjectName(_fromUtf8("cbGroupAsLayer"))
        self.verticalLayout.addWidget(self.cbGroupAsLayer)
        self.cbLayerIsBaseLayer = QtGui.QCheckBox(self.tab_2)
        self.cbLayerIsBaseLayer.setObjectName(_fromUtf8("cbLayerIsBaseLayer"))
        self.verticalLayout.addWidget(self.cbLayerIsBaseLayer)
        self.cbSingleTile = QtGui.QCheckBox(self.tab_2)
        self.cbSingleTile.setObjectName(_fromUtf8("cbSingleTile"))
        self.verticalLayout.addWidget(self.cbSingleTile)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.liImageFormat = QtGui.QComboBox(self.tab_2)
        self.liImageFormat.setObjectName(_fromUtf8("liImageFormat"))
        self.liImageFormat.addItem(_fromUtf8(""))
        self.liImageFormat.addItem(_fromUtf8(""))
        self.liImageFormat.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.liImageFormat)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.cbCached = QtGui.QCheckBox(self.tab_2)
        self.cbCached.setObjectName(_fromUtf8("cbCached"))
        self.verticalLayout.addWidget(self.cbCached)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.inCacheExpiration = QtGui.QSpinBox(self.tab_2)
        self.inCacheExpiration.setMaximum(2592000)
        self.inCacheExpiration.setObjectName(_fromUtf8("inCacheExpiration"))
        self.horizontalLayout_2.addWidget(self.inCacheExpiration)
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_2.addWidget(self.label_16)
        self.inMetatileSize = QtGui.QLineEdit(self.tab_2)
        self.inMetatileSize.setObjectName(_fromUtf8("inMetatileSize"))
        self.horizontalLayout_2.addWidget(self.inMetatileSize)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.treeLayer = QtGui.QTreeWidget(self.tab_2)
        self.treeLayer.setColumnCount(1)
        self.treeLayer.setObjectName(_fromUtf8("treeLayer"))
        self.treeLayer.headerItem().setText(0, _fromUtf8("Name"))
        self.treeLayer.header().setDefaultSectionSize(50)
        self.treeLayer.header().setMinimumSectionSize(50)
        self.treeLayer.header().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.treeLayer, 0, 0, 2, 1)
        self.cbRootGroupsAsBlock = QtGui.QCheckBox(self.tab_2)
        self.cbRootGroupsAsBlock.setObjectName(_fromUtf8("cbRootGroupsAsBlock"))
        self.gridLayout_2.addWidget(self.cbRootGroupsAsBlock, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_2.addWidget(self.label_15)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        self.inMinScale = QtGui.QLineEdit(self.tab_3)
        self.inMinScale.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inMinScale.setMaxLength(10)
        self.inMinScale.setObjectName(_fromUtf8("inMinScale"))
        self.horizontalLayout_12.addWidget(self.inMinScale)
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_12.addWidget(self.label_14)
        self.inMaxScale = QtGui.QLineEdit(self.tab_3)
        self.inMaxScale.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inMaxScale.setMaxLength(10)
        self.inMaxScale.setObjectName(_fromUtf8("inMaxScale"))
        self.horizontalLayout_12.addWidget(self.inMaxScale)
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_12.addWidget(self.label_17)
        self.inZoomLevelNumber = QtGui.QLineEdit(self.tab_3)
        self.inZoomLevelNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inZoomLevelNumber.setMaxLength(2)
        self.inZoomLevelNumber.setObjectName(_fromUtf8("inZoomLevelNumber"))
        self.horizontalLayout_12.addWidget(self.inZoomLevelNumber)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.label_18 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_2.addWidget(self.label_18)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_15.addWidget(self.label_19)
        self.inMapScales = QtGui.QLineEdit(self.tab_3)
        self.inMapScales.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inMapScales.setObjectName(_fromUtf8("inMapScales"))
        self.horizontalLayout_15.addWidget(self.inMapScales)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.label_20 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_23 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_2.addWidget(self.label_23)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.cbOsmMapnik = QtGui.QCheckBox(self.tab_3)
        self.cbOsmMapnik.setObjectName(_fromUtf8("cbOsmMapnik"))
        self.horizontalLayout_9.addWidget(self.cbOsmMapnik)
        self.cbOsmMapquest = QtGui.QCheckBox(self.tab_3)
        self.cbOsmMapquest.setObjectName(_fromUtf8("cbOsmMapquest"))
        self.horizontalLayout_9.addWidget(self.cbOsmMapquest)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.label_22 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_2.addWidget(self.label_22)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_13.addWidget(self.label_11)
        self.inGoogleKey = QtGui.QLineEdit(self.tab_3)
        self.inGoogleKey.setMaximumSize(QtCore.QSize(100, 16777215))
        self.inGoogleKey.setObjectName(_fromUtf8("inGoogleKey"))
        self.horizontalLayout_13.addWidget(self.inGoogleKey)
        self.cbGoogleStreets = QtGui.QCheckBox(self.tab_3)
        self.cbGoogleStreets.setObjectName(_fromUtf8("cbGoogleStreets"))
        self.horizontalLayout_13.addWidget(self.cbGoogleStreets)
        self.cbGoogleSatellite = QtGui.QCheckBox(self.tab_3)
        self.cbGoogleSatellite.setObjectName(_fromUtf8("cbGoogleSatellite"))
        self.horizontalLayout_13.addWidget(self.cbGoogleSatellite)
        self.cbGoogleHybrid = QtGui.QCheckBox(self.tab_3)
        self.cbGoogleHybrid.setObjectName(_fromUtf8("cbGoogleHybrid"))
        self.horizontalLayout_13.addWidget(self.cbGoogleHybrid)
        self.cbGoogleTerrain = QtGui.QCheckBox(self.tab_3)
        self.cbGoogleTerrain.setObjectName(_fromUtf8("cbGoogleTerrain"))
        self.horizontalLayout_13.addWidget(self.cbGoogleTerrain)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_27 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.verticalLayout_3.addWidget(self.label_27)
        self.label_28 = QtGui.QLabel(self.tab)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_3.addWidget(self.label_28)
        self.twLocateByLayerList = QtGui.QTableWidget(self.tab)
        self.twLocateByLayerList.setObjectName(_fromUtf8("twLocateByLayerList"))
        self.twLocateByLayerList.setColumnCount(4)
        self.twLocateByLayerList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twLocateByLayerList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twLocateByLayerList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twLocateByLayerList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twLocateByLayerList.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.twLocateByLayerList)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.liLocateByLayerLayers = QtGui.QComboBox(self.tab)
        self.liLocateByLayerLayers.setObjectName(_fromUtf8("liLocateByLayerLayers"))
        self.horizontalLayout_16.addWidget(self.liLocateByLayerLayers)
        self.liLocateByLayerFields = QtGui.QComboBox(self.tab)
        self.liLocateByLayerFields.setObjectName(_fromUtf8("liLocateByLayerFields"))
        self.horizontalLayout_16.addWidget(self.liLocateByLayerFields)
        self.cbLocateByLayerDisplayGeom = QtGui.QCheckBox(self.tab)
        self.cbLocateByLayerDisplayGeom.setObjectName(_fromUtf8("cbLocateByLayerDisplayGeom"))
        self.horizontalLayout_16.addWidget(self.cbLocateByLayerDisplayGeom)
        self.btLocateByLayerAdd = QtGui.QPushButton(self.tab)
        self.btLocateByLayerAdd.setObjectName(_fromUtf8("btLocateByLayerAdd"))
        self.horizontalLayout_16.addWidget(self.btLocateByLayerAdd)
        self.btLocateByLayerDel = QtGui.QPushButton(self.tab)
        self.btLocateByLayerDel.setObjectName(_fromUtf8("btLocateByLayerDel"))
        self.horizontalLayout_16.addWidget(self.btLocateByLayerDel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_ftp = QtGui.QWidget()
        self.tab_ftp.setObjectName(_fromUtf8("tab_ftp"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_ftp)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem3, 13, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_ftp)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_10.addWidget(self.label_24, 6, 0, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_ftp)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.inHost = QtGui.QLineEdit(self.tab_ftp)
        self.inHost.setObjectName(_fromUtf8("inHost"))
        self.horizontalLayout.addWidget(self.inHost)
        self.label_2 = QtGui.QLabel(self.tab_ftp)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.inPort = QtGui.QLineEdit(self.tab_ftp)
        self.inPort.setObjectName(_fromUtf8("inPort"))
        self.horizontalLayout.addWidget(self.inPort)
        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.tab_ftp)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.inUsername = QtGui.QLineEdit(self.tab_ftp)
        self.inUsername.setObjectName(_fromUtf8("inUsername"))
        self.horizontalLayout_3.addWidget(self.inUsername)
        self.label_4 = QtGui.QLabel(self.tab_ftp)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.inPassword = QtGui.QLineEdit(self.tab_ftp)
        self.inPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.inPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.inPassword.setObjectName(_fromUtf8("inPassword"))
        self.horizontalLayout_3.addWidget(self.inPassword)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.lbWinscpSession = QtGui.QLabel(self.tab_ftp)
        self.lbWinscpSession.setObjectName(_fromUtf8("lbWinscpSession"))
        self.horizontalLayout_11.addWidget(self.lbWinscpSession)
        self.inWinscpSession = QtGui.QLineEdit(self.tab_ftp)
        self.inWinscpSession.setObjectName(_fromUtf8("inWinscpSession"))
        self.horizontalLayout_11.addWidget(self.inWinscpSession)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.gridLayout_10.addLayout(self.horizontalLayout_11, 11, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_ftp)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_10.addWidget(self.label_25, 3, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem5, 5, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab_ftp)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_10.addWidget(self.label_26, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lbWinscpIn = QtGui.QLabel(self.tab_ftp)
        self.lbWinscpIn.setObjectName(_fromUtf8("lbWinscpIn"))
        self.horizontalLayout_10.addWidget(self.lbWinscpIn)
        self.inWinscpPath = QtGui.QLineEdit(self.tab_ftp)
        self.inWinscpPath.setObjectName(_fromUtf8("inWinscpPath"))
        self.horizontalLayout_10.addWidget(self.inWinscpPath)
        self.btWinscpPath = QtGui.QPushButton(self.tab_ftp)
        self.btWinscpPath.setObjectName(_fromUtf8("btWinscpPath"))
        self.horizontalLayout_10.addWidget(self.btWinscpPath)
        self.gridLayout_10.addLayout(self.horizontalLayout_10, 7, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.tab_ftp)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.inLocaldir = QtGui.QLineEdit(self.tab_ftp)
        self.inLocaldir.setEnabled(False)
        self.inLocaldir.setObjectName(_fromUtf8("inLocaldir"))
        self.horizontalLayout_5.addWidget(self.inLocaldir)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.tab_ftp)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.inRemotedir = QtGui.QLineEdit(self.tab_ftp)
        self.inRemotedir.setObjectName(_fromUtf8("inRemotedir"))
        self.horizontalLayout_6.addWidget(self.inRemotedir)
        self.gridLayout_8.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 4, 0, 1, 1)
        self.lbWinscpHelp = QtGui.QLabel(self.tab_ftp)
        self.lbWinscpHelp.setObjectName(_fromUtf8("lbWinscpHelp"))
        self.gridLayout_10.addWidget(self.lbWinscpHelp, 9, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem6, 2, 0, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.lbWinscpCriteria = QtGui.QLabel(self.tab_ftp)
        self.lbWinscpCriteria.setObjectName(_fromUtf8("lbWinscpCriteria"))
        self.horizontalLayout_14.addWidget(self.lbWinscpCriteria)
        self.inWinscpCriteria = QtGui.QLineEdit(self.tab_ftp)
        self.inWinscpCriteria.setObjectName(_fromUtf8("inWinscpCriteria"))
        self.horizontalLayout_14.addWidget(self.inWinscpCriteria)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem7)
        self.gridLayout_10.addLayout(self.horizontalLayout_14, 12, 0, 1, 1)
        self.tabWidget.addTab(self.tab_ftp, _fromUtf8(""))
        self.tab_main = QtGui.QWidget()
        self.tab_main.setObjectName(_fromUtf8("tab_main"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_main)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.outLog = QtGui.QTextEdit(self.tab_main)
        self.outLog.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.outLog.setReadOnly(True)
        self.outLog.setObjectName(_fromUtf8("outLog"))
        self.gridLayout_5.addWidget(self.outLog, 0, 0, 1, 5)
        self.btClearlog = QtGui.QPushButton(self.tab_main)
        self.btClearlog.setObjectName(_fromUtf8("btClearlog"))
        self.gridLayout_5.addWidget(self.btClearlog, 1, 0, 2, 1)
        self.btCancelFtpSync = QtGui.QPushButton(self.tab_main)
        self.btCancelFtpSync.setEnabled(True)
        self.btCancelFtpSync.setObjectName(_fromUtf8("btCancelFtpSync"))
        self.gridLayout_5.addWidget(self.btCancelFtpSync, 1, 4, 1, 1)
        self.outState = QtGui.QLabel(self.tab_main)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.outState.setFont(font)
        self.outState.setText(_fromUtf8(""))
        self.outState.setObjectName(_fromUtf8("outState"))
        self.gridLayout_5.addWidget(self.outState, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_main, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 9)
        self.btSave = QtGui.QPushButton(lizmap)
        self.btSave.setObjectName(_fromUtf8("btSave"))
        self.gridLayout.addWidget(self.btSave, 1, 6, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 5, 1, 1)
        self.btHelp = QtGui.QPushButton(lizmap)
        self.btHelp.setObjectName(_fromUtf8("btHelp"))
        self.gridLayout.addWidget(self.btHelp, 1, 3, 1, 1)

        self.retranslateUi(lizmap)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonClose, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), lizmap.close)
        QtCore.QMetaObject.connectSlotsByName(lizmap)
        lizmap.setTabOrder(self.tabWidget, self.treeLayer)
        lizmap.setTabOrder(self.treeLayer, self.inLayerTitle)
        lizmap.setTabOrder(self.inLayerTitle, self.teLayerAbstract)
        lizmap.setTabOrder(self.teLayerAbstract, self.inLayerLink)
        lizmap.setTabOrder(self.inLayerLink, self.cbToggled)
        lizmap.setTabOrder(self.cbToggled, self.cbPopup)
        lizmap.setTabOrder(self.cbPopup, self.btConfigurePopup)
        lizmap.setTabOrder(self.btConfigurePopup, self.cbGroupAsLayer)
        lizmap.setTabOrder(self.cbGroupAsLayer, self.cbLayerIsBaseLayer)
        lizmap.setTabOrder(self.cbLayerIsBaseLayer, self.cbSingleTile)
        lizmap.setTabOrder(self.cbSingleTile, self.liImageFormat)
        lizmap.setTabOrder(self.liImageFormat, self.cbCached)
        lizmap.setTabOrder(self.cbCached, self.inCacheExpiration)
        lizmap.setTabOrder(self.inCacheExpiration, self.inMetatileSize)
        lizmap.setTabOrder(self.inMetatileSize, self.inMinScale)
        lizmap.setTabOrder(self.inMinScale, self.inMaxScale)
        lizmap.setTabOrder(self.inMaxScale, self.inZoomLevelNumber)
        lizmap.setTabOrder(self.inZoomLevelNumber, self.inMapScales)
        lizmap.setTabOrder(self.inMapScales, self.cbOsmMapnik)
        lizmap.setTabOrder(self.cbOsmMapnik, self.cbOsmMapquest)
        lizmap.setTabOrder(self.cbOsmMapquest, self.inGoogleKey)
        lizmap.setTabOrder(self.inGoogleKey, self.cbGoogleStreets)
        lizmap.setTabOrder(self.cbGoogleStreets, self.cbGoogleSatellite)
        lizmap.setTabOrder(self.cbGoogleSatellite, self.cbGoogleHybrid)
        lizmap.setTabOrder(self.cbGoogleHybrid, self.cbGoogleTerrain)
        lizmap.setTabOrder(self.cbGoogleTerrain, self.inHost)
        lizmap.setTabOrder(self.inHost, self.inPort)
        lizmap.setTabOrder(self.inPort, self.inUsername)
        lizmap.setTabOrder(self.inUsername, self.inPassword)
        lizmap.setTabOrder(self.inPassword, self.inRemotedir)
        lizmap.setTabOrder(self.inRemotedir, self.inLocaldir)
        lizmap.setTabOrder(self.inLocaldir, self.inWinscpPath)
        lizmap.setTabOrder(self.inWinscpPath, self.btWinscpPath)
        lizmap.setTabOrder(self.btWinscpPath, self.inWinscpSession)
        lizmap.setTabOrder(self.inWinscpSession, self.inWinscpCriteria)
        lizmap.setTabOrder(self.inWinscpCriteria, self.outLog)
        lizmap.setTabOrder(self.outLog, self.btClearlog)
        lizmap.setTabOrder(self.btClearlog, self.buttonClose)
        lizmap.setTabOrder(self.buttonClose, self.btSync)
        lizmap.setTabOrder(self.btSync, self.btCancelFtpSync)
        lizmap.setTabOrder(self.btCancelFtpSync, self.btSave)
        lizmap.setTabOrder(self.btSave, self.btHelp)

    def retranslateUi(self, lizmap):
        lizmap.setWindowTitle(QtGui.QApplication.translate("lizmap", "LizMap", None, QtGui.QApplication.UnicodeUTF8))
        self.btSync.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.btSync.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.abstract", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.link", None, QtGui.QApplication.UnicodeUTF8))
        self.cbToggled.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.toggled", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPopup.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.popup", None, QtGui.QApplication.UnicodeUTF8))
        self.btConfigurePopup.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.popup.configure", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGroupAsLayer.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.groupAsLayer", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLayerIsBaseLayer.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.baselayer", None, QtGui.QApplication.UnicodeUTF8))
        self.cbSingleTile.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.singletile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.imageFormat.label", None, QtGui.QApplication.UnicodeUTF8))
        self.liImageFormat.setItemText(0, QtGui.QApplication.translate("lizmap", "png", None, QtGui.QApplication.UnicodeUTF8))
        self.liImageFormat.setItemText(1, QtGui.QApplication.translate("lizmap", "png; mode=8bit", None, QtGui.QApplication.UnicodeUTF8))
        self.liImageFormat.setItemText(2, QtGui.QApplication.translate("lizmap", "jpeg", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCached.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.cached", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.cacheExpiration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.layer.metatileSize", None, QtGui.QApplication.UnicodeUTF8))
        self.inMetatileSize.setInputMask(QtGui.QApplication.translate("lizmap", "0,0;_", None, QtGui.QApplication.UnicodeUTF8))
        self.cbRootGroupsAsBlock.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.rootGroupsAsBlock", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("lizmap", "ui.tab.layers.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.scales.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.minScale.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.maxScale.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.zoomLevelNumber.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.or.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.mapScales.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.public.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.public.help", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.openstreetmap.label", None, QtGui.QApplication.UnicodeUTF8))
        self.cbOsmMapnik.setText(QtGui.QApplication.translate("lizmap", "OSM Mapnik", None, QtGui.QApplication.UnicodeUTF8))
        self.cbOsmMapquest.setText(QtGui.QApplication.translate("lizmap", "OSM Mapquest", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("lizmap", "ui.tab.map.google.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("lizmap", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGoogleStreets.setText(QtGui.QApplication.translate("lizmap", "Streets", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGoogleSatellite.setText(QtGui.QApplication.translate("lizmap", "Satellite", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGoogleHybrid.setText(QtGui.QApplication.translate("lizmap", "Hybrid", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGoogleTerrain.setText(QtGui.QApplication.translate("lizmap", "Terrain", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("lizmap", "ui.tab.map.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("lizmap", "ui.tab.tools.locateByLayer.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("lizmap", "ui.tab.tools.locateByLayer.description", None, QtGui.QApplication.UnicodeUTF8))
        item = self.twLocateByLayerList.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("lizmap", "twLocateByLayer.col.layer", None, QtGui.QApplication.UnicodeUTF8))
        item = self.twLocateByLayerList.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("lizmap", "twLocateByLayer.col.field", None, QtGui.QApplication.UnicodeUTF8))
        item = self.twLocateByLayerList.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("lizmap", "twLocateByLayer.col.displayGeom", None, QtGui.QApplication.UnicodeUTF8))
        item = self.twLocateByLayerList.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("lizmap", "twLocateByLayer.col.id", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLocateByLayerDisplayGeom.setText(QtGui.QApplication.translate("lizmap", "ui.tab.tools.locateByLayer.cbDisplayGeom", None, QtGui.QApplication.UnicodeUTF8))
        self.btLocateByLayerAdd.setText(QtGui.QApplication.translate("lizmap", "ui.tab.tools.btLocateByLayerAdd", None, QtGui.QApplication.UnicodeUTF8))
        self.btLocateByLayerDel.setText(QtGui.QApplication.translate("lizmap", "ui.tab.tools.btLocateByLayerDel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("lizmap", "ui.tab.tools.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.title.winscp", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.host.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.port.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.username.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.password.label", None, QtGui.QApplication.UnicodeUTF8))
        self.lbWinscpSession.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.winscp.session", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.title.directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.title.parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.lbWinscpIn.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.winscp.label", None, QtGui.QApplication.UnicodeUTF8))
        self.btWinscpPath.setText(QtGui.QApplication.translate("lizmap", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.localdir.label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.remotedir.label", None, QtGui.QApplication.UnicodeUTF8))
        self.lbWinscpHelp.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.winscp.help.label", None, QtGui.QApplication.UnicodeUTF8))
        self.lbWinscpCriteria.setText(QtGui.QApplication.translate("lizmap", "ui.tab.ftp.winscp.criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ftp), QtGui.QApplication.translate("lizmap", "ui.tab.ftp.label", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearlog.setText(QtGui.QApplication.translate("lizmap", "ui.tab.log.btClearLog.label", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancelFtpSync.setText(QtGui.QApplication.translate("lizmap", "ui.tab.log.btCancelSync.label", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), QtGui.QApplication.translate("lizmap", "ui.tab.log.label", None, QtGui.QApplication.UnicodeUTF8))
        self.btSave.setText(QtGui.QApplication.translate("lizmap", "ui.tab.layers.btSave.label", None, QtGui.QApplication.UnicodeUTF8))
        self.btHelp.setText(QtGui.QApplication.translate("lizmap", "ui.main.btHelp", None, QtGui.QApplication.UnicodeUTF8))

