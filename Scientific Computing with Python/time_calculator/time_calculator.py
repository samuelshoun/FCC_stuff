'''
This is original code I wrote in order to pass the challenge project.
'''


def add_time(time, add, day=None):

    hh = int(time.split(':')[0])
    mm = int(time.split()[0].split(':')[1])

    if time.split()[1].upper() == 'AM':
        h24 = hh
    else:
        h24 = hh + 12

    hinc = int(add.split(':')[0])
    minc = int(add.split(':')[1])

    newtime = list()
    newtime.append(h24 + hinc)
    newtime.append(mm + minc)
    newtime

    if newtime[1] > 59:
        newtime[1] = newtime[1] - 60
        newtime[0] = newtime[0] + 1
    newtime

    daysinc = 0

    while newtime[0] > 23:
        newtime[0] = newtime[0] - 24
        daysinc = daysinc + 1

    daysinc

    dayid = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
             'friday': 4, 'saturday': 5, 'sunday': 6}

    daysdict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
                4: 'Friday', 5: 'Saturday', 6: 'Sunday'}



    if newtime[0] > 11:
        newtime[0] -= 12
        ampm = 'PM'
    else:
        ampm = 'AM'

    if newtime[0] == 0:
        newtime[0] = 12

    if day != None:
        dd = dayid.get(day.lower())
        print(dd)
        print(daysinc)
        print(dd + daysinc%7)
        print(daysdict.get((dd + daysinc)%7))
        newdd = ', ' + daysdict.get((dd + daysinc) % 7)
    else:
        newdd = ''


    if len(str(newtime[1])) < 2:
        newtime[1] = '0' + str(newtime[1])

    if daysinc == 1:
        laterstr = ' (next day)'
    elif daysinc > 1:
        laterstr = ' ({} days later)'.format(daysinc)
    else:
        laterstr = ''
    laterstr

    newtimestr = str(newtime[0]) + ':' + str(newtime[1]) + ' ' + ampm + newdd + laterstr
    return newtimestr
