﻿ # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyTextBrowser import *

try:
  _fromUtf8 = QString.fromUtf8
except AttributeError:
  def _fromUtf8(s):
    return s

try:
  _encoding = QApplication.UnicodeUTF8
  def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
  def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig)

class MyTabWidget(QTabWidget):
  def __init__(self,parent=None):
    super(MyTabWidget,self).__init__(parent)    

    tab = MyTextBrowser(self)
    self.addTab(tab, _fromUtf8('測試用Tab'))
