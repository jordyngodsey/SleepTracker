from tkinter import *

window = Tk()
window.title('Sleep Tracker')

# Create opening window to start Sleep Tracker program
a = Label(window, text = 'Welcome to Sleep Tracker!', font = ('Arial Bold',30)).pack()
b = Label(window, text = "Let's Start Recording",font = ('Arial', 20)).pack()
window.geometry('600x250')

# Create a function to get input and perform calculations
def callback():
    # Input user age
    age = Entry(window, width=20)
    age.pack()
    age.insert(0, 'Enter your age')

    # Input time user went to sleep
    sleep_time = Entry(window, width=35, borderwidth=5)
    sleep_time.pack()
    sleep_time.insert(0, "Enter time you went to sleep (00:00 XM)")

    # Input time user woke up
    wake_time = Entry(window, width=35, borderwidth=5)
    wake_time.pack()
    wake_time.insert(0, "Enter time you woke up (00:00 XM)")

    # Define a function to take the sleep and wake inputs and calculate the
    # total time (in hours) the user slept
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
                if sleep[0:2] == '12':
                    hours = int(wake[0:2])
                    minutes = int(sleep[3:5]) + int(wake[3:5])
                    total_min = (60 * hours) + minutes
                    total = '{0:.2f}'.format(total_min / 60)
                    return total
                elif sleep[0:2] != '12':
                    hours = int(wake[0:2]) - int(sleep[0:2])
                    minutes = int(sleep[3:5]) + int(wake[3:5])
                    total_min = (60 * hours) + minutes
                    total = '{0:.2f}'.format(total_min / 60)
                    return total
            elif sleep[3:5] != '00':
                if sleep[3:5] >= wake[3:5]:
                    if sleep[0:2] == '12':
                        hours = int(wake[0:2]) - 1
                        minutes = 60 - abs(int(wake[3:5]) - int(sleep[3:5]))
                        total_min = (60 * hours) + minutes
                        total = '{0:.2f}'.format(total_min / 60)
                        return total
                    elif sleep[0:2] != '12':
                        hours = int(wake[0:2]) - int(sleep[0:2]) - 1
                        minutes = 60 - abs(int(wake[3:5]) - int(sleep[3:5]))
                        total_min = (60 * hours) + minutes
                        total = '{0:.2f}'.format(total_min / 60)
                        return total
                elif sleep[3:5] < wake[3:5]:
                    if sleep[0:2] == '12':
                        hours = int(wake[0:2])
                        minutes = abs(int(wake[3:5]) - int(sleep[3:5]))
                        total_min = (60 * hours) + minutes
                        total = '{0:.2f}'.format(total_min / 60)
                        return total
                    elif sleep[0:2] != '12':
                        hours = int(wake[0:2]) - int(sleep[0:2])
                        minutes = abs(int(wake[3:5]) - int(sleep[3:5]))
                        total_min = (60 * hours) + minutes
                        total = '{0:.2f}'.format(total_min / 60)
                        return total

    # Define a function for the "Enter" button to execute
    def button_clicked():
        sleep = sleep_time.get()
        wake = wake_time.get()
        ac = age.get()
        Label(window, text=ac).pack()
        c = Label(window, text="Recommended Hours of Sleep Per Day", font=('Arial', 14)).pack()

        # Output recommended hours of sleep based on age
        if int(ac) > 2 and int(ac) < 6:
            c = Label(window, text="Preschool:  3-5 years,  10-13 hours per 24 hours", font=('Arial', 10)).pack()
        elif int(ac) > 5 and int(ac) < 13:
            c = Label(window, text="School Age:  6-12 years,  9-12 hours per 24 hours", font=('Arial', 10)).pack()
        elif int(ac) > 12 and int(ac) < 19:
            c = Label(window, text="Teen:  13-18 years,  8-10 hours per 24 hours", font=('Arial', 10)).pack()
        elif int(ac) > 18:
            c = Label(window, text="Adult:  19-60 years,  7 or more hours per night", font=('Arial', 10)).pack()

        total = sleep_calculate(sleep, wake)
        text = Label(window, text="You slept {} hours.".format(total))
        text.pack()

        # Output if user got enough sleep or not
        if int(ac) <= 5:
            if float(total) <= 10.00:
                output = Label(window, text="You did not get enough sleep.")
                output.pack()
            elif float(total) > 10.00:
                output = Label(window, text="You got enough sleep!")
                output.pack()
        elif (int(ac) >= 6 and int(ac) <= 12):
            if float(total) <= 9.00:
                output = Label(window, text="You did not get enough sleep.")
                output.pack()
            elif float(total) > 9.00:
                output = Label(window, text="You got enough sleep!")
                output.pack()
        elif (int(ac) >= 13 and int(ac) <= 18):
            if float(total) <= 8.00:
                output = Label(window, text="You did not get enough sleep.")
                output.pack()
            elif float(total) > 8.00:
                output = Label(window, text="You got enough sleep!")
                output.pack()
        elif (int(ac) >= 19 and int(ac) <= 60):
            if float(total) <= 7.00:
                output = Label(window, text="You did not get enough sleep.")
                output.pack()
            elif float(total) > 7.00:
                output = Label(window, text="You got enough sleep!")
                output.pack()
    button = Button(window, text="Enter", fg="white", bg="black", command=button_clicked)
    button.pack()

Button(window, text='Start New Log', fg = 'white', bg = 'black', command = callback).pack()

window.mainloop()