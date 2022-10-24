from Tkinter import *
window = Tk()
window.title('Sleep Tracker')

#pack is used to show the object in the window
a = Label(window, text = 'Welcome to Sleep Tracker!', font = ('Arial Bold',40)).pack()
b = Label(window, text = "Let's Start Recording",font = ('Arial', 30)).pack()
window.geometry('600x250')


def callback():
    main = Tk()
    main.title('Sleep Tracker')
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
                total = '{0:.2f}'.format(total_min / 60)
                return total
            elif sleep[3:5] != '00':
                hours = (11 - int(sleep[0:2])) + int(wake[0:2])
                minutes = (60 - int(sleep[3:5])) + int(wake[3:5])
                total_min = (60 * hours) + minutes
                total = '{0:.2f}'.format(total_min / 60)
                return total
        elif sleep[-2:] == 'AM':
            if sleep[3:5] == '00':
                hours = int(wake[0:2]) - int(sleep[0:2])
                minutes = int(sleep[3:5]) + int(wake[3:5])
                total_min = (60 * hours) + minutes
                total = '{0:.2f}'.format(total_min / 60)
                return total
            elif sleep[3:5] != '00':
                if sleep[3:5] > wake[3:5]:
                    hours = int(wake[0:2]) - int(sleep[0:2]) - 1
                    minutes = 60 - abs(int(wake[3:5]) - int(sleep[3:5]))
                    total_min = (60 * hours) + minutes
                    total = '{0:.2f}'.format(total_min / 60)
                    return total
                elif sleep[3:5] <= wake[3:5]:
                    hours = int(wake[0:2]) - int(sleep[0:2])
                    minutes = abs(int(wake[3:5]) - int(sleep[3:5]))
                    total_min = (60 * hours) + minutes
                    total = '{0:.2f}'.format(total_min / 60)
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

def ages():
    age = Entry(window, width = 20)
    age.pack()
    age.insert(0, 'Enter your age')
    def bc():
        ac = age.get()
        Label(window, text = ac).pack()
        Button(window, text='Continue', fg='white', bg='black', command=callback).pack()
    Button(window, text = 'Enter', fg = 'white', bg = 'black', command = bc).pack()

Button(window, text='Start New Log', fg = 'white', bg = 'black', command = ages).pack()

window.mainloop()