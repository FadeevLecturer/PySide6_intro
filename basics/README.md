# PySide. Основы

## Установка `PySide`

Установить `PySide6` можно используя `pip`

```sh
pip install PySide6
```


## Пространство имен `PySide`

В `PySide` можно выделить три основных модуля.

1. [QtCore](https://doc.qt.io/qtforpython/PySide6/QtCore/index.html#module-PySide6.QtCore) --- ядро библиотеки, предоставляет доступ к ключевому функционалу, который не завязан на графическом интерфейсе: сигналы, слоты, базовые классы и др.
2. [QtGui](https://doc.qt.io/qtforpython/PySide6/QtGui/index.html#module-PySide6.QtGui) --- расширяет ядро некоторыми элементами `gui`: события, экраны, окна и др.
3. [QtWidgets](https://doc.qt.io/qtforpython/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets) --- содержит в себе набор готовых к использованию элементов интерфейса (виджетов): кнопки и многое другое.

```{note}
С полным списком модулей можно ознакомиться [здесь](https://doc.qt.io/qtforpython/modules.html).
```

Часто в приложении используются десятки имен из модулей `PySide`. В связи с этим нередко встречается `wildcard` импорты следующего вида:  

```python
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
```

В данном случае это не так страшно, т.к. все имена в модулях `PySide` имеют специфическую форму и не перекрываются с именами встроенной библиотеки. В крупных программах принято реализовывать графический интерфейс и остальную логику программы в разных местах, что ещё в большей степени нивелирует проблему "запутанности" пространства имен.   

## Qt приложение. `QApplication`

Чтобы разрабатывать приложение с графическим интерфейсом на основе `Qt` необходимо в первую очередь создать объект типа [QApplication](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QApplication.html). При этом такой объект **должен быть ровно один** вне зависимости от обстоятельств, количества окон у приложения и т.п. `QApplication` делает очень много закулисной работы по обработке событий и организации виджетов. 

Самое примитивное приложение на `PySide` без каких либо окон выглядит примерно так.
```python
import sys
from PySide6.QtWidgets import QApplication


app = QApplication(sys.argv)
app.exec()
print("Application is closed!")
```

Команда `app.exec()` запускает [цикл событий](https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB_%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9) ([event loop](https://en.wikipedia.org/wiki/Event_loop)), который ожидает [события](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5) ([events](https://en.wikipedia.org/wiki/Event-driven_programming)) и вызывает соответствующий обработчик события (`event handler`). Цикл события из себя представляет бесконечный цикл типа `while`, выход из которого осуществляется при возникновении события `exit`. 

Важно понимать, что когда `Qt` приложение запущено (`app.exec()`), программа попадает в событийный цикл, из которого она не выйдет, пока приложение не будет закрыто. Иными словами исполнение кода в скрипте `python` приостанавливается, управление потоком исполнения программы передаётся `Qt`. Так, инструкция `print` в скрипте выше не выполнится до тех пор, пока не будет вызван метод `app.exit()`, к которому мы не предоставили прямого доступа.

Итого, в примере выше цикл событий будет крутиться в пустую, так как мы не обрабатываем ни одного события. Создадим окно у приложения, чтобы начать обрабатывать хоть какие-то события.

## Главное окно приложения. `QMainWindow`

`QApplication` самого по себе недостаточно, чтобы на экране появился графический интерфейс. Для этого необходимо создать какой-нибудь элемент интерфейса (`widget`) и вывести его на экран, т.к. по умолчанию они скрыты. Для главного окна приложения удобнее всего использовать виджет [QMainWindow](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html).

Следующий пример расширяет предыдущий, добавляя создание экземпляр класса `QMainWindow` и выводя его на экран методом [show](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.show) (по умолчанию все виджеты скрыты). 

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.show()
app.exec()
print("Application is closed!")
```

При запуске этого приложения должно появиться окно, которое в зависимости от операционной системы может выглядеть следующим образом.
```{figure} ../_static/lecture_specific/qt/main_window_1.png
```

```{note}
У метода `show` есть аналоги 
[showFullScreen](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.showFullScreen), 
[showNormal](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.showNormal), 
[showMaximized](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.showMaximized) и 
[showMinimized](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.showMinimized).
```

Это окно уже можно
- перемещать;
- менять его размер, растягивая или сжимая его, а также растягивая его на весь экран;
- сворачивать и разворачивать обратно;
- закрывать его.

Т.е. `Qt` сам сгенерировал ряд элементов графического интерфейса, а также реализовал обработку ряда событий (например, нажатие на кнопку закрытия приложения). 
  
При этом только после закрытия этого окна программа покинет цикл событий, сработает инструкция `print` и в консоли появится сообщение "Application is closed!".

## Кастомизация `QMainWindow`

В предыдущем примере окно было создано с дефолтным размером, дефолтной иконкой и дефолтным заголовком "python", который даже полностью не влезает из-за размеров окна. Все это можно настроить под свои нужды. 

- Размер окна можно изменить методом [setGeometry](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.setGeometry), который на вход принимает четыре параметра: координаты `x` и `y` левого верхнего угла окна, ширину `w` и высоту `h` окна. Ось $Ox$ и $Oy$ направлены слева направо и сверху вниз соответственно.
```{figure} ../_static/lecture_specific/qt/geometry.png
```

- Заголовок окна можно изменить методом [setWindowTitle](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.setWindowTitle), который на вход принимает строку.

- Иконку окна можно изменить с помощью метода [setWindowIcon](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.setWindowIcon), которая на вход принимает объект [QtGui.QIcon](https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html).
Конструктор `QIcon` в свою очередь на вход принимает изображение или строку, содержащую путь к файлу с иконкой. 

Изменим размер, заголовок и иконку окна из предыдущего примера. Можно было бы вызывать все перечисленные методы у уже существующего окна, но гораздо нагляднее будет унаследовать от класса `QMainWindow` и модифицировать окно в момент инициализации.

```python
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon


path_to_the_icon = os.path.join("..", "icons", "phys.png")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("My Qt Application")
        self.setWindowIcon(QIcon(path_to_the_icon))


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
```

Разберем этот пример детальнее, так как модификацию `Qt` виджетов часто удобнее всего делать именно так.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
```
Мы собираемся модифицировать класс `QMainWindow`, поэтому от него и наследуемся. В методе `__init__` в первую очередь делегируем инициализацию окна базовому классу.

```python
self.setGeometry(100, 100, 300, 200)
self.setWindowTitle("My Qt Application")
self.setWindowIcon(QIcon(path_to_the_icon))
```
Затем настраиваем положение и размер окна, его заголовок и путь к окну.

```{note}
Для простоты в примере создаётся окно в абсолютных единицах, но можно было бы настроить геометрию окна под разрешение экрана. Метод [primaryScreen](https://doc.qt.io/qtforpython/PySide6/QtGui/QGuiApplication.html#PySide6.QtGui.PySide6.QtGui.QGuiApplication.primaryScreen) объекта `QApplication` возвращает объект [QtGui.QScreen](https://doc.qt.io/qtforpython/PySide6/QtGui/QScreen.html), который позволяет получить информацию о главном экране (ситуация несколько усложняется, если экранов несколько), в том числе и геометрию экрана методом [availableGeometry](https://doc.qt.io/qtforpython/PySide6/QtGui/QScreen.html#PySide6.QtGui.PySide6.QtGui.QScreen.availableGeometry).
```
```python
main_window = MainWindow()
```
Ну и создаем мы теперь экземпляр нового класса `MainWindow`, а не исходного `QMainWindow`.

В итоге должны получить нечто следующее.
```{figure} ../_static/lecture_specific/qt/main_window_2.png
```
 
## Виджет `QLabel`

Чтобы внутри окна появились элементы графического управления необходимо добавить виджеты. Все виджеты располагаются в модуле `QtWidgets`, в том числе и один из самых простых --- [QLabel](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html), который позволяет отображать текст (или изображение, но об этом в следующем разделе).

Любой виджет принимает ссылку на родительский виджет `parent`. `QLabel` на вход принимает ещё и `python` строку. Метод [setALignment](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.PySide6.QtWidgets.QLabel.setAlignment) ожидает на вход [Qt.Core.AlignmentFlag](https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.AlignmentFlag) и отвечает за выравнивание текста по центру (`QtCore.Qt.AlignCenter`), по левому краю (`QtCore.Qt.AlignRight`) и т.п.

Чтобы добавить виджет на окно, мало просто указать `parent` при его создании. Необходимо также сказать самому окну этот виджет отрисовать. Пока у нас всего один виджет можно воспользоваться методом [QMainWindow.setCentralWidget](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.PySide6.QtWidgets.QMainWindow.setCentralWidget), чтобы сразу добавить наш текст в центр окна.

```python
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QIcon, Qt


path_to_the_icon = os.path.join("..", "icons", "../python.png")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("My Qt Application")
        self.setWindowIcon(QIcon(path_to_the_icon))

        self.label = QLabel("Hello, World!",  parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
```

```{figure} ../_static/lecture_specific/qt/label_1.png
```
## Макеты. `Layout`

Добавить несколько виджетов на окно проще всего используя макеты (`layout`). 

Вообще говоря, можно расположить виджеты на окне, указав окно в качестве родителя (`parent`) и вызвав метод `setGeometry`. При таком подходе можно указывать произвольное положение кнопок, но нет никакой гарантии, что с изменением геометрии самого окна элементы будут адекватно перестраиваться.

`Qt` предоставляет набор стандартных макетов, которые сами следят за эффективным использованием пространства, занимаемого элементами интерфейса. Чтобы установить макет, необходимо вызвать метод [setLayout](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.setLayout) у какого-нибудь разумного виджета (), но у [QMainWindow](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.setLayout)



Чтобы добавить несколько виджетов на окно, необходимо:
- установить в качестве центрального виджет [QWidget](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html), т.к. у `QMainWindow` всегда должен быть центральный виджет;
- расположить внутри центрального виджета все остальные, используя макеты (`layouts`).

```{note}
Подробнее о макетах можно почитать [здесь](https://doc.qt.io/qtforpython/overviews/layout.html#layout-management).
```

### `QHBoxLayout` и `QVBoxLayout`

Макет [QHBoxLayout](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QHBoxLayout.html) выравнивает виджеты горизонтально слева направо , а [QVBoxLayout](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QVBoxLayout.html) вертикально сверху вниз. У обоих из них есть среди прочих следующие методы:

- [addWidget](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QBoxLayout.html#PySide6.QtWidgets.PySide6.QtWidgets.QBoxLayout.addWidget) --- добавляет виджет. В качестве параметра `alignment` можно указать выравнивание, как и `QLabel`;
- [addSpacing](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QBoxLayout.html#PySide6.QtWidgets.PySide6.QtWidgets.QBoxLayout.addSpacing) --- добавляет пустой заполнитель заданного размера;
- [addLayout](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QBoxLayout.html#PySide6.QtWidgets.PySide6.QtWidgets.QBoxLayout.addLayout) --- добавляет подмакет. Например, можно встроить `QHBoxLayout` в `QVBoxLayout`. 

Макет сам распределяет пространство, которое будет занимать виджет исходя из геометрии окна, политики размера каждого из виджетов ([QSizePolicy](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSizePolicy.html), который среди прочего определяем минимальный размер виджета) и коэффициента растяжения (`stretching`), который определяет насколько жадно этот виджет будет занимать пространство. По умолчанию под каждый виджет отводится одинаковое количество места, но если указать параметр `stretch` (его принимают все три вышеописанных метода), то виджета с большим значением будет занимать больше пространства.

В качестве примера, создадим два виджета `QLabel`, положим в них картинку методом [setPixmap](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.PySide6.QtWidgets.QLabel.setPixmap), который ожидает на вход объект [QPixmap](https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html), и добавим их в макет.

````{tabbed} QHBoxLayout
```python
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon, Qt, QPixmap


path_to_the_icon = os.path.join("..", "icons", "phys.png")
path_to_py_logo = os.path.join("..", "icons", "python.png")
path_to_qt_logo = os.path.join("..", "icons", "qt.png")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("My Qt Application")
        self.setWindowIcon(QIcon(path_to_the_icon))

        widget = QWidget(parent=self)
        self.setCentralWidget(widget)

        python_logo = QPixmap(path_to_py_logo)
        python_logo_label = QLabel()
        python_logo_label.setPixmap(python_logo)

        qt_logo = QPixmap(path_to_qt_logo)
        qt_logo_label = QLabel()
        qt_logo_label.setPixmap(qt_logo)

        layout = QHBoxLayout()
        layout.addWidget(python_logo_label, alignment=Qt.AlignCenter)
        layout.addWidget(qt_logo_label, alignment=Qt.AlignCenter)
        widget.setLayout(layout)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
```
```{figure} ../_static/lecture_specific/qt/HBoxLayout.png
```

````
````{tabbed} QVBoxLayout
```python
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, Qt, QPixmap


path_to_the_icon = os.path.join("..", "icons", "phys.png")
path_to_py_logo = os.path.join("..", "icons", "python.png")
path_to_qt_logo = os.path.join("..", "icons", "qt.png")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("My Qt Application")
        self.setWindowIcon(QIcon(path_to_the_icon))

        widget = QWidget(parent=self)
        self.setCentralWidget(widget)

        python_logo = QPixmap(path_to_py_logo)
        python_logo_label = QLabel()
        python_logo_label.setPixmap(python_logo)

        qt_logo = QPixmap(path_to_qt_logo)
        qt_logo_label = QLabel()
        qt_logo_label.setPixmap(qt_logo)

        layout = QVBoxLayout()
        layout.addWidget(python_logo_label, alignment=Qt.AlignCenter)
        layout.addWidget(qt_logo_label, alignment=Qt.AlignCenter)
        widget.setLayout(layout)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
```
```{figure} ../_static/lecture_specific/qt/VBoxLayout.png
```
````

# PySide6_intro