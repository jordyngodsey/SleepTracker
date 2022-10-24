from tkinter import *

main = Tk()

# Create input box for time user went to sleep
sleep_time = Entry(main, width=50, borderwidth=5)
sleep_time.pack()
sleep_time.insert(0, "Enter time you went to sleep (00:00 XM)")

# Create input box for time user woke up
wake_time = Entry(main, width=50, borderwidth=5)
wake_time.pack()
wake_time.insert(0, "Enter time you woke up (00:00 XM)")

def sleep_calculate(sleep, wake):
    if sleep[-2:] == 'PM':
        if sleep[3:5] == '00':
            hours = (12 - int(sleep[0:2])) + int(wake[0:2])
            minutes = int(sleep[3:5]) + int(wake[3:5])
            total_min = (60 * hours) + minutes
            total = total_min / 60
            return total
        elif sleep[3:5] != '00':
            hours = (11 - int(sleep[0:2])) + int(wake[0:2])
            minutes = (60 - int(sleep[3:5])) + int(wake[3:5])
            total_min = (60 * hours) + minutes
            total = total_min / 60
            return total
    elif sleep[-2:] == 'AM':
        if sleep[3:5] == '00':
            hours = int(wake[0:2]) - int(sleep[0:2])
            minutes = int(sleep[3:5]) + int(wake[3:5])
            total_min = (60 * hours) + minutes
            total = total_min / 60
            return total
        elif sleep[3:5] != '00':
            if sleep[3:5] > wake[3:5]:
                hours = int(wake[0:2]) - int(sleep[0:2]) - 1
                minutes = 60 - abs(int(wake[3:5]) - int(sleep[3:5]))
                total_min = (60 * hours) + minutes
                total = total_min / 60
                return total
            elif sleep[3:5] <= wake[3:5]:
                hours = int(wake[0:2]) - int(sleep[0:2])
                minutes = abs(int(wake[3:5]) - int(sleep[3:5]))
                total_min = (60 * hours) + minutes
                total = total_min / 60
                return total

# Define a function for the button to execute
def button_clicked():
    sleep = sleep_time.get()
    wake = wake_time.get()

    total = sleep_calculate(sleep, wake)
    text = Label(main, text=total)
    text.pack()

button = Button(main, text="Enter", fg="white", bg="black", command=button_clicked)

button.pack()

main.mainloop()

