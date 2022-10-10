# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (QFile, QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QPen, QPolygon, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QSizePolicy,
                               QTextEdit, QToolButton, QWidget, QVBoxLayout, QHBoxLayout)




class MainWidget(QWidget):
    """
    TODO привести все к нормлаьной модели MVC полностью реализовывать не будем пожалуй,
    Сделаем так: есть условный Frame - Drawframe, в нем будет логика по отрисовке и необходимым рассчетом, т.е и модель и отображение
    Menu - контроллер, т.е он вносит изменения и вызывает события
    и создать полноценные классы, у которых появятся нормальные события  и сигналы
    Класс для работы с главным виджетом и его детьми


    """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"background-color: rgb(156, 169, 255);\n""")
        self.setupUi()


    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Widget")
        self.resize(585, 390)
        
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        menuWidget = QFrame(self)
        menuWidget.setStyleSheet(u"background-color: rgb(170, 117, 240);\n""")

        menuWidget.setFixedWidth(100)
        self.layout.addWidget(menuWidget)

        self.Menu = Menu(menuWidget)

        self.Drawframe = DrawFrame(self)
        self.layout.addWidget(self.Drawframe)

        self.Menu.DrawFigure.clicked.connect(self.drawing)

        # Привязать сигнал Menu к событию DrawFrame

        self.retranslateUi()

    def drawing(self):
        self.Drawframe.drawing()

        if self.Drawframe.mode == 'DRAW':
            self.Menu.DrawFigure.setStyleSheet(u"color: rgb(124,252,0);")
        else:
            self.Menu.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")


    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate(
            "Widget", u"Widget", None))
        self.Menu.DrawFigure.setText(QCoreApplication.translate("Widget", "Нарисовать\nкривую Безье", None))

    def load_ui(self):
        """Стандартный класс загрузки ui если не будем использовать то к удалению"""
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


class Menu(QVBoxLayout):
    """Класс-контроллер содержит необходимые кнопки"""

    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName(u"Menu")


        self.DrawFigure = QToolButton()
        self.DrawFigure.setObjectName(u"DrawFigure")
        self.addWidget(self.DrawFigure)
        self.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")

      

class DrawFrame(QFrame):
    """Класс модель-отображение
    Отвечает и за отрисовку и за расчеты
    """

    def __init__(self, parent):
        super().__init__(parent)
        # MONE DRAW PUT_DOT
        self._mode = 'NONE'

        self.figure = []
        self.Bezier = []
        self.setObjectName(u"Drawframe")
        self.setGeometry(QRect(70, 0, 521, 401))
        self.setStyleSheet(u"background-color: rgb(139, 183, 255);")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

    @property
    def bezier(self):
        return self._Bezier

    @bezier.setter
    def mode(self, new_Bezier):
        self._Bezier = new_Bezier
        
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        self._mode = new_mode

    @property
    def figure(self):
        return self._figure

    @figure.setter
    def figure(self, new_figure):
        self._figure = new_figure


    def drawing(self):
        if self.mode != 'DRAW':
            self.figure = []

            self.mode = 'DRAW'
        else:
            self.mode = 'NONE'

        self.update()

    def mousePressEvent(self, QMouseEvent):
        if self.mode == 'DRAW':
            self.figure.append([QMouseEvent.position().x(),
                               QMouseEvent.position().y()])

        self.update()



    def paintEvent(self, event):
        """Отрисовка точки и фигуры"""
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.drawLine(self.width()/2, 0, self.width()/2, self.height())
        painter.drawLine(0, self.height()/2, self.width(), self.height()/2)

        if self.mode != 'DRAW': pass
            # points = QPolygon([
            #     QPoint(coord[0], coord[1]) for coord in self.figure])
            # painter.drawPolygon(points)

        # Рисуем точки для фигуры
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        for point in self.figure:
            painter.drawEllipse(point[0], point[1], 5, 5)

        # Рисуем точки для повернутой фигуры и ее саму
        painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
       
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))


        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))

        painter.end()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
