from tkinter import *


class Timer:
    def __init__(self, timer_row, timer_name):
        self.running = False
        self.timer_s = 0
        self.timer_m = 0
        self.timer_h = 0
        self.spinbox1 = Spinbox(from_=0, to=8, width=5, command=self.spinbox_used)
        self.spinbox1.grid(row=timer_row, column=2)
        self.spinbox2 = Spinbox(from_=0, to=60, width=5, command=self.spinbox_used)
        self.spinbox2.grid(row=timer_row, column=3)
        self.spinbox3 = Spinbox(from_=0, to=60, width=5, command=self.spinbox_used)
        self.spinbox3.grid(row=timer_row, column=4)
        self.t1_label = Label(text=timer_name, font=("Arial", 15, "bold"))
        self.t1_label.grid(row=timer_row, column=0)
        self.start_button = Button(text="start", command=self.start)
        self.start_button.grid(row=timer_row, column=5)
        self.stop_button = Button(text="stop", command=self.stop, state='disabled')
        self.stop_button.grid(row=timer_row, column=6)
        self.reset_button = Button(text="reset", command=self.reset, state='disabled')
        self.reset_button.grid(row=timer_row, column=7)
        self.timer_1 = Label(text=f"{self.timer_h}:{self.timer_m}:{self.timer_s}", fg="black",
                             font=("Arial", 20, "bold"))
        self.timer_1.grid(row=timer_row, column=1)

    def spinbox_used(self):
        if not self.running:
            self.timer_h = int(self.spinbox1.get())
            self.timer_m = int(self.spinbox2.get())
            self.timer_s = int(self.spinbox3.get())
            self.timer_1['text'] = f"{self.timer_h}:{self.timer_m}:{self.timer_s}"
        else:
            self.stop()

    def count(self):
        if self.running:
            if self.timer_s > 0:
                self.timer_s -= 1
            if self.timer_s == 0:
                if self.timer_h == 0 and self.timer_m == 0:
                    self.stop_button['state'] = 'disabled'
                    running = False
                elif self.timer_m == 0 and self.timer_h > 0:
                    self.timer_h -= 1
                    self.timer_m = 59
                    self.timer_s = 59
                else:
                    self.timer_m -= 1
                    self.timer_s = 60
            self.timer_1['text'] = f"{self.timer_h}:{self.timer_m}:{self.timer_s}"
            screen = self.timer_1.after(1000, self.count)

    def start(self):
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.reset_button['state'] = 'normal'
        self.running = True
        self.count()

    def stop(self):
        self.running = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'
        self.reset_button['state'] = 'normal'

    def reset(self):
        self.running = False
        self.timer_s = 0
        self.timer_m = 0
        self.timer_h = 0
        self.timer_1['text'] = f"{self.timer_h}:{self.timer_m}:{self.timer_s}"
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'
        self.reset_button['state'] = 'disabled'
