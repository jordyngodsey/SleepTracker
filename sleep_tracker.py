sleep = '10:30 PM'
wake = '8:00 AM'

if sleep[-1:-3] == 'PM':
    new_sleep = int(sleep[0:2])+12
    print(new_sleep)