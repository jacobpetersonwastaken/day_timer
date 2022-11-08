from tkinter import *
from timer import Timer


HEIGHT = 300
WIDTH = 600
screen = Tk()
canvas = Canvas(master=screen, width=WIDTH, height=HEIGHT)
canvas.grid(padx=0, pady=0, row=0, column=0, rowspan=100, columnspan=8)
screen.minsize(height=HEIGHT, width=WIDTH)

screen.title("Life timer")
main_label = Label(text="Timers", font=("Arial", 24, "bold"))
main_label.grid(row=0, column=0)

timer_s24 = 0
timer_m24 = 0
timer_h24 = 24


def clickExitButton():
    exit()


exit_button = Button(text="Exit", command=clickExitButton)
exit_button.grid(row=0, column=7)


"""Main 24 hour timer"""
main24_hr = Label(screen, text=f"{timer_h24}:{timer_m24}:{timer_s24}", fg="black", font="Verdana 15 bold")
main24_hr.grid(row=1, column=0)

"""Total time"""
total_time = Label(screen, text=f"Total Time", fg="black", font="Verdana 20 bold")
total_time.grid(row=0, column=1)


"""Timer Creation"""
timer1 = Timer(timer_row=3, timer_name="Work")
timer2 = Timer(timer_row=5, timer_name="School")
timer3 = Timer(timer_row=7, timer_name="Entertainment")
timer4 = Timer(timer_row=8, timer_name="Sleep")


screen.mainloop()

