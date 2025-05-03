def add_time(start, duration, sday=''):

    # create variables
    stime, smeridiem = start.split()
    shour, sminute = stime.split(':')
    shour = int(shour)
    sminute = int(sminute)
    ahour, aminute = duration.split(':');
    ahour = int(ahour)
    aminute = int(aminute)
    week = ['sunday', 'monday' ,'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # convert to military time
    if smeridiem == 'PM' and shour != 12:
        shour += 12
    elif smeridiem == 'AM' and shour == 12:
        shour = 0
    else:
        pass
    
    # add time
    thour = shour + ahour
    tminute = sminute + aminute
    daycount = 0

    while tminute >= 60:
        #print(tminute)
        thour += 1
        tminute -= 60
    
    if tminute < 10:
        tminute = f'0{tminute}'

    while thour >= 24:
        daycount += 1
        thour -= 24

    if thour == 12:
        fmeridiem = 'PM'
    elif thour > 12:
        fmeridiem = 'PM'
        thour -= 12
    elif thour == 0:
        thour = 12
        fmeridiem = 'AM'
    else:
        fmeridiem = 'AM'

    if daycount == 1:
        dayspassed = f' (next day)'
    elif daycount > 1:
        dayspassed = f' ({daycount} days later)'
    else:
        dayspassed = ''

    if sday != '':
        sday = sday.lower()
        sindex = week.index(sday.lower())
        nindex = sindex

        while daycount > 0:
            nindex += 1
            daycount -= 1
            if nindex == 7:
                nindex = 0
            else:
                pass

        fday = f', {week[nindex].capitalize()}'
            
    else:
        sday = ''
        fday = ''

    new_time = f'{thour}:{tminute} {fmeridiem}{fday}{dayspassed}'

    # test
    #print(new_time)
    
  return new_time
