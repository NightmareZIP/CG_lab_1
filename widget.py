# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys


from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (QFile, QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
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

        #Привязать сигнал Menu к событию DrawFrame

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Menu.DrawFigure.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \n"
    "\u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.Menu.PutDot.setText(QCoreApplication.translate("Widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c\n"
    "\u0442\u043e\u0447\u043a\u0443", None))
        self.Menu.TurnFigure.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442", None))
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

        self.log_widget = QWidget(self)
        self.log_widget.setObjectName(u"LogWiget")
        self.log_widget.setGeometry(QRect(0, 200, 71, 211))
        self.log_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.LogText = QTextEdit(self.log_widget)
        self.LogText.setObjectName(u"LogText")
        self.LogText.setGeometry(QRect(0, 0, 71, 191))


class DrawFrame(QFrame):
    """Класс модель-отображение
    Отвечает и за отрисовку и за расчеты
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName(u"Drawframe")
        self.setGeometry(QRect(70, 0, 521, 401))
        self.setStyleSheet(u"background-color: rgb(139, 183, 255);")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
