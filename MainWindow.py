# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QSizePolicy,
    QTextEdit, QToolButton, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(585, 390)
        self.Drawframe = QFrame(Widget)
        self.Drawframe.setObjectName(u"Drawframe")
        self.Drawframe.setGeometry(QRect(70, 0, 521, 401))
        self.Drawframe.setStyleSheet(u"background-color: rgb(139, 183, 255);")
        self.Drawframe.setFrameShape(QFrame.StyledPanel)
        self.Drawframe.setFrameShadow(QFrame.Raised)
        self.Menu = QFrame(Widget)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setGeometry(QRect(0, 0, 71, 391))
        self.Menu.setStyleSheet(u"background-color: rgb(156, 169, 255);\n"
"")
        self.Menu.setFrameShape(QFrame.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.DrawFigure = QToolButton(self.Menu)
        self.DrawFigure.setObjectName(u"DrawFigure")
        self.DrawFigure.setGeometry(QRect(0, 20, 71, 31))
        self.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.PutDot = QToolButton(self.Menu)
        self.PutDot.setObjectName(u"PutDot")
        self.PutDot.setGeometry(QRect(0, 60, 71, 31))
        self.PutDot.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.TurnFigure = QToolButton(self.Menu)
        self.TurnFigure.setObjectName(u"TurnFigure")
        self.TurnFigure.setGeometry(QRect(0, 160, 71, 31))
        self.TurnFigure.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Angle = QLineEdit(self.Menu)
        self.Angle.setObjectName(u"Angle")
        self.Angle.setGeometry(QRect(0, 140, 71, 20))
        self.Angle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget = QWidget(self.Menu)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 200, 71, 211))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.LogText = QTextEdit(self.widget)
        self.LogText.setObjectName(u"LogText")
        self.LogText.setGeometry(QRect(0, 0, 71, 191))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.DrawFigure.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \n"
"\u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.PutDot.setText(QCoreApplication.translate("Widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c\n"
"\u0442\u043e\u0447\u043a\u0443", None))
        self.TurnFigure.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442", None))
    # retranslateUi

