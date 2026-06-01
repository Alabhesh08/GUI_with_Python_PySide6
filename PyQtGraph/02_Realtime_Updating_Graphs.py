from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint


# We're going to update our data every 50ms, 
# although PyQtGraph can plot data much more quickly than this it can get hard to watch!
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.plot_graph.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.plot_graph.plot(self.x, self.y, pen=pen)

          # ... init continued ...
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())