# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import calculation

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (QFile, QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QPen, QPolygon, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QSizePolicy,
                               QTextEdit, QToolButton, QWidget)


"""
    Автосгенерированн код из граф. редактора, для упрощения работы, повторная генерация может быть вызвана через
    pyside6-uic form.ui -o MainWindow.py это создаст отдельный файл, из которого можно будет взять код и после испльзовать.

    Примерная логика отрисовок
    В MainWidget будем привязывать сигналы  к событиям у классов Menu и DrawFrame
    контроллер (Menu) и модель+отрисовка - DrawDrame
    Общий алгоритм: вид рисования (новая точка или новая фигура) будет определяться свойством у DrawFrame.mode,
    Данное свойство будет влиять на работу срабатывания клика по фрейму и выполняться логика методов DrawFrame.

    Логика взаимодействи:
        При клике по кнопке Меню, вызывается сигнал (см документацию), благодаря которому вызвается событие в DrawFrame

"""


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
        self.setupUi()
#        Ui_Widget().setupUi(self)
#        self.load_ui()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Widget")
        self.resize(585, 390)
        self.Menu = Menu(self)

        self.Drawframe = DrawFrame(self)

        # MONE DRAW PUT_DOT
        self.mode = 'NONE'

        self.Menu.DrawFigure.clicked.connect(self.drawing)
        self.Menu.PutDot.clicked.connect(self.put_dot)
        self.Menu.TurnFigure.clicked.connect(self.rotate)

        # Привязать сигнал Menu к событию DrawFrame

        self.retranslateUi()

    def drawing(self):
        self.Drawframe.drawing()

        if self.Drawframe.mode == 'DRAW':
            self.Menu.DrawFigure.setStyleSheet(u"color: rgb(124,252,0);")
        else:
            self.Menu.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Menu.PutDot.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Menu.TurnFigure.setStyleSheet(u"color: rgb(72, 66, 255);")

    def put_dot(self):

        self.Menu.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Menu.PutDot.setStyleSheet(u"color: rgb(124,252,0);")
        self.Menu.TurnFigure.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Drawframe.put_dot()

    def rotate(self):

        self.Menu.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Menu.PutDot.setStyleSheet(u"color: rgb(72, 66, 255);")
        self.Menu.TurnFigure.setStyleSheet(u"color: rgb(124,252,0);")
        self.Drawframe.corner = float(self.Menu.Angle.text())
        self.Drawframe.rotate()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate(
            "Widget", u"Widget", None))
        self.Menu.DrawFigure.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \n"
                                                                "\u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.Menu.PutDot.setText(QCoreApplication.translate("Widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c\n"
                                                            "\u0442\u043e\u0447\u043a\u0443", None))
        self.Menu.TurnFigure.setText(QCoreApplication.translate(
            "Widget", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442", None))
    # retranslateUi

    def load_ui(self):
        """Стандартный класс загрузки ui если не будем использовать то к удалению"""
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


class Menu(QFrame):
    """Класс-контроллер содержит необходимые кнопки"""

    def __init__(self, parent):
        super().__init__(parent)

        # self.setDot = Signal()
        # self.startDrawFigure = Signal()
        # self.endDrawFigure = Signal()

        self.setObjectName(u"Menu")
        self.setGeometry(QRect(0, 0, 71, 391))
        self.setStyleSheet(u"background-color: rgb(156, 169, 255);\n""")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.DrawFigure = QToolButton(self)
        self.DrawFigure.setObjectName(u"DrawFigure")
        self.DrawFigure.setGeometry(QRect(0, 20, 71, 31))
        self.DrawFigure.setStyleSheet(u"color: rgb(72, 66, 255);")

        self.PutDot = QToolButton(self)
        self.PutDot.setObjectName(u"PutDot")
        self.PutDot.setGeometry(QRect(0, 60, 71, 31))
        self.PutDot.setStyleSheet(u"color: rgb(72, 66, 255);")

        self.TurnFigure = QToolButton(self)
        self.TurnFigure.setObjectName(u"TurnFigure")
        self.TurnFigure.setGeometry(QRect(0, 160, 71, 31))
        self.TurnFigure.setStyleSheet(u"color: rgb(72, 66, 255);")

        self.Angle = QLineEdit(self)
        self.Angle.setObjectName(u"Angle")
        self.Angle.setGeometry(QRect(0, 140, 71, 20))
        self.Angle.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # self.log_widget = QWidget(self)
        # self.log_widget.setObjectName(u"LogWiget")
        # self.log_widget.setGeometry(QRect(0, 200, 71, 211))
        # self.log_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # self.LogText = QTextEdit(self.log_widget)
        # self.LogText.setObjectName(u"LogText")
        # self.LogText.setGeometry(QRect(0, 0, 71, 191))


class DrawFrame(QFrame):
    """Класс модель-отображение
    Отвечает и за отрисовку и за расчеты
    """

    def __init__(self, parent):
        super().__init__(parent)
        # MONE DRAW PUT_DOT
        self._mode = 'NONE'

        self.corner = 0
        self.figure = []
        self.turned_figure = []

        self.setObjectName(u"Drawframe")
        self.setGeometry(QRect(70, 0, 521, 401))
        self.setStyleSheet(u"background-color: rgb(139, 183, 255);")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.dot = [self.width()/2,
                    self.height()/2]

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        self._mode = new_mode

    @property
    def dot(self):
        return self._dot

    @dot.setter
    def dot(self, new_dot):
        self._dot = new_dot

    @property
    def figure(self):
        return self._figure

    @figure.setter
    def figure(self, new_figure):
        self._figure = new_figure

    @property
    def corner(self):
        return self._corner

    @corner.setter
    def corner(self, new_corner):
        self._corner = new_corner

    @property
    def turned_figure(self):
        return self._turned_figure

    @turned_figure.setter
    def turned_figure(self, new_turned):

        self._turned_figure = new_turned

    def drawing(self):
        if self.mode != 'DRAW':
            self.figure = []
            self.turned_figure = []

            self.mode = 'DRAW'
        else:
            self.mode = 'NONE'

        self.update()

    def mousePressEvent(self, QMouseEvent):
        if self.mode == 'DRAW':
            self.figure.append([QMouseEvent.position().x(),
                               QMouseEvent.position().y()])
        elif self.mode == "PUT_DOT":
            self.dot = [QMouseEvent.position().x(), QMouseEvent.position().y()]

        self.update()

    def put_dot(self):
        self.mode = "PUT_DOT"

    def rotate(self):
        self.turned_figure = calculation.turnFigure(self.figure,
                                                    self.corner,
                                                    self.dot,
                                                    self.width(),
                                                    self.height())
   
        self.update()

    def paintEvent(self, event):
        """Отрисовка точки и фигуры"""
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.drawLine(self.width()/2, 0, self.width()/2, self.height())
        painter.drawLine(0, self.height()/2, self.width(), self.height()/2)

        if self.mode != 'DRAW':
            points = QPolygon([
                QPoint(coord[0], coord[1]) for coord in self.figure])
            painter.drawPolygon(points)

        # Рисуем точки для фигуры
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        for point in self.figure:
            painter.drawEllipse(point[0], point[1], 5, 5)

        # Рисуем точки для повернутой фигуры и ее саму
        painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        points = QPolygon([
            QPoint(coord[0], coord[1]) for coord in self.turned_figure])
        painter.drawPolygon(points)

        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))

        for point in self.turned_figure:
            painter.drawEllipse(point[0], point[1], 5, 5)

        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.drawEllipse(self.dot[0], self.dot[1], 5, 5)

        painter.end()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
