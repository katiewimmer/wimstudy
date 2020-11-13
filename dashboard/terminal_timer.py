import time as t
## Countdown function starts here
def stopwatch(sec):
    while sec:
        hourr, sec_to_min = divmod(sec, 3600)
        minn, secc = divmod(sec_to_min, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hourr, minn, secc)
        print(timeformat, end='\r')
        t.sleep(1)
        sec -= 1
    print('Times Up!\n')
## calling stopwatch function
stopwatch(15)
# stopwatch(60) #example of a minute
# stopwatch(3600) #example of an hour