"""
    PROGRAMA REALIZADO POR
        RAUL VILLALTA
        OCUMARE DEL TUY
        MARZO 2020
"""

import re

def getTime(timeString, opt):
    #print("Time --> {}".format(timeString))
    pattern = re.compile(r'(\d{2}):(\d{2}):(\d{2}),(\d{3})')
    sol = pattern.search(timeString)
    if sol:
        hour = sol.group(1)
        minute = sol.group(2)
        second = sol.group(3)
        milisecond = sol.group(4)
        salida = [int(hour), int(minute), int(second), int(milisecond)]
        if opt:
            return salida
        else:
            #return "[" + hour + "," + min + "," + second + "," + milisecond +"]"
            return str(salida)
    return "NO VALUE"
    
def printTime(timeList):
    print("Hour : {}".format(timeList[0]))
    print("Minute : {}".format(timeList[1]))
    print("Second : {}".format(timeList[2]))
    print("Millisecond : {}".format(timeList[3]))
    print("")
    
def addTime(timeOriginal, timeMod):
    _hour = 0
    _min = 0
    _sec = 0
    hour_1 = timeOriginal[0]
    min_1 = timeOriginal[1]
    sec_1 = timeOriginal[2]
    mil_1 = timeOriginal[3]
    
    hour_2 = timeMod[0]
    min_2 = timeMod[1]
    sec_2 = timeMod[2]
    mil_2 = timeMod[3]
    
    mil = mil_1 + mil_2
    if mil > 999:
        _sec = 1
        mil -= 1000
    sec = sec_1 + sec_2
    if sec > 59:
        _min = 1
        sec -= 60
    min = min_1 + min_2
    if min > 59:
        _hour = 1
        min -= 60
    
    hour = hour_1 + hour_2 + _hour
    min = min + _min
    sec = sec + _sec
    hour = insertZeros(hour, 2)
    min = insertZeros(min, 2)
    sec = insertZeros(sec, 2)
    mil = insertZeros(mil, 3)
    return hour + ":" + min + ":" + sec + "," + mil

def removeTime(timeOriginal, timeMod):
    _hour = 0
    _min = 0
    _sec = 0
    hour_1 = timeOriginal[0]
    min_1 = timeOriginal[1]
    sec_1 = timeOriginal[2]
    mil_1 = timeOriginal[3]
    
    hour_2 = timeMod[0]
    min_2 = timeMod[1]
    sec_2 = timeMod[2]
    mil_2 = timeMod[3]
    
    mil = mil_1 - mil_2
    if mil < 0:
        _sec = -1
        mil += 1000
    sec = sec_1 - sec_2
    if sec  < 0:
        _min = -1
        sec += 60
    min = min_1 - min_2
    if min < 0:
        _hour = -1
        min += 60
    hour = hour_1 - hour_2
    if hour < 0:
        hour += 24
    
    sol = [
            hour + _hour,
           min + _min,
           sec + _sec,
           mil
          ]
    mil = str(mil)
    if len(mil) == 1:
        mil = "00" + mil
    if len(mil) == 2:
        mil = "0" + mil
    return str(hour + _hour) + ":" + str(min + _min) + ":" + str(sec + _sec) + ":" + mil

def separateNumber(number):
    entero = int(number)
    decimal = number - entero
    return [entero, decimal]
#TIMETONUM(TIME)
#   TIME --> [HH, MM, SS, mmm]
#   RETURN --> milisegundos
def timeToNum(time):
    s=0
    s += time[0] * 3.6e6
    s += time[1] * 6e4
    s += time[2] * 1e3
    s += time[3]
    return s
#STRINFTONUM(TIEMPO_STRING)
#   TIEMPO_STRING --> HH:MM:SS,mmm
#   RETURN --> MILISEGUNDOS
def stringToNum(tiempo_string):
    tiempo_num = getTime(tiempo_string, True)
    return timeToNum(tiempo_num)

#STRECHTIME(TIME_STRING, FACTOR)
#   tiempo_string --> HH:MM:SS,mmm
#   FACTOR --> number
def strechTime(tiempo_string, factor):
    time = getTime(tiempo_string, True)
    time = timeToNum(time)
    time *= factor
    return formatTime(time)
    
# MODIFYINTERVAL(TIME_A, TIME_B, FACTOR)    
#   TIME_A --> TIEMPO INICIAL   TIME --> [HH, MM, SS, mmm]
#   TIME_B --> TIEMPO FINAL
#   TIME_REF --> TIEMPO AL QUE SE LE SUMARA DELTAT*factor
#   FACTOR --> number
#   RETURN --> [HH, MM, SS, mmm]
def modifyInterval(time_a, time_b, time_ref, factor):
    ti = time_a
    tj = time_b
    tref = time_ref
    dt = timeToNum(tj) - timeToNum(ti)
    dt = dt * factor
    tj = timeToNum(tref) + dt
    sol = formatTime(tj)
    return sol

def formatTime(miliseconds):
    t = separateNumber(miliseconds/3.6e6)
    hh = t[0]
    t = separateNumber(t[1]*60)
    mm = t[0]
    t = separateNumber(t[1]*60)
    ss = t[0]
    t =round(t[1]*1000)
    if t == 1000:
        ss += 1
        t = 0
    mmm = t
    sol = [hh, mm, ss, mmm]
    return sol

# TIMETOSTRING(TIME)
#   TIME --> [HH, MM, SS, mmm]  (LIST)
#   RETURN --> HH:MM:SS,mmm     (STRIG)
def timeToString(time):
    return insertZeros(time[0], 2) + ":" + insertZeros(time[1], 2) + ":" + insertZeros(time[2],2) + "," + insertZeros(time[3],3)

def insertZeros(num, digits):
    s = str(num)
    numZeros = digits - len(s)
    if numZeros == 0:
        return s
    if numZeros == 1:
        return "0" + s
    if numZeros == 2:
        return "00" + s
    
