from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_cricket_run_counter

class Widget(QWidget, Ui_cricket_run_counter):
    def __init__(self):
        super().__init__()

        
        self.setupUi(self)
        self.setWindowTitle("Crickert Run Counter!")
        self.reset()

        self.run1_button.clicked.connect(lambda: self.add_runs(1))
        self.run4_button.clicked.connect(lambda: self.add_runs(4))
        self.run6_button.clicked.connect(lambda: self.add_runs(6))

        self.ball_button.clicked.connect(self.add_ball)
        self.wicket_button.clicked.connect(self.add_wicket)

        self.reset_button.clicked.connect(self.reset)

    def reset(self):
        self.runs_total = 0
        self.wkts = 0
        self.total_balls = 0
        self.crr = 0
        self.update_overs()
        self.update_runs()

    def add_runs(self, i):
        self.runs_total = self.runs_total + i
        self.update_runs()

    def add_wicket(self):
        self.wkts += 1
        self.update_runs()

    def add_ball(self):
        self.total_balls += 1
        self.update_overs()

    def update_runs(self):
        self.runs_label.setText(f"Score : {self.runs_total}/{self.wkts}")
        
        try:
            self.crr = self.runs_total / self.overs
        except ZeroDivisionError:
            self.crr = 0
    
        self.crr_label.setText(f"Current Run Rate (CRR) : {self.crr}")

    def update_overs(self):
        overs_whole = self.total_balls // 6
        over_balls = self.total_balls % 6
        self.overs = self.total_balls/6
        self.overs_label.setText(f"Overs : {overs_whole}.{over_balls}")
        self.update_runs()
