import src.cayenneLPP as cayenneLPP
import src.postData as postData

#--------------------------
# TTS settings
#--------------------------
fPort = 1                           # FPort: 1-223
confirmedDownlink = False           # Confirmed downlink: True / False
priority = "HIGHEST"                # Priority: LOWEST / LOW / BELOW_NORMAL / NORMAL / ABOVE_NORMAL / HIGH / HIGHEST
schedule = "replace"                # Insert mode: push / replace



#--------------------------
# End device settings (API key, Application name, End device name) are in the config.py file
#--------------------------



#--------------------------
# Downlinks - Add data in format: lpp.append([channelNumber, "sensorType", value])
#--------------------------
lpp = []



#--------------------------
# Settings password
#--------------------------
lpp.append([100, "addPower", 1234])                     # 0-9999



#--------------------------
# Common settings
#--------------------------

# Send data every [s]
lpp.append([100, "addSmallTime", 60])                   # 60-3600

# Number of measured samples
lpp.append([100, "addPresence", 1])                     # 1-10

# Power grid [V]
lpp.append([103, "addDigitalInput", 0])                 # 0 = 230, 1 = 400


# Working mode
lpp.append([101, "addDigitalInput", 0])                 # 0 = OFF, 1 = ON, 2 = Light intensity, 3 = Time , 4 = Light intensity in Time, 5 = Sunset / sunrise switching times

# Timezone
lpp.append([102, "addDigitalInput", 0])                 # 0 - Central European Time, 1 - United Kingdom, 2 - UTC, 3 - US Eastern Time Zone, 4 - US Central Time Zone, 5 - US Mountain Time Zone, 6 - US Arizona, 7 - US Pacific Time Zone, 8 - Australia Eastern Time Zone

# Reset and load
lpp.append([100, "addDigitalInput", 1])                 # 1 = Saved, # 2 = Defaul


# Send only selected
#--------------------------
sendOnlySelected1 = [0,0,0,0,0,0,0,0]
sendOnlySelected2 = [0,0,0,0,0,0,0,0]

# 1/2 Send only selected:
sendOnlySelected1[7] = 1     # Relay state
sendOnlySelected1[6] = 1     # Number of changes
sendOnlySelected1[5] = 1     # Light intensity
sendOnlySelected1[4] = 1     # Battery voltage
sendOnlySelected1[3] = 1     # Battery percentage
sendOnlySelected1[2] = 1     # Battery temperature
sendOnlySelected1[1] = 1     # RTC temperature
sendOnlySelected1[0] = 1     # Power line voltage

# 2/2 Send only selected:
sendOnlySelected2[7] = 1     # Power line frequency
sendOnlySelected2[6] = 1     # Active energy
sendOnlySelected2[5] = 1     # Current
sendOnlySelected2[4] = 1     # Active power
sendOnlySelected2[3] = 1     # Power factor
sendOnlySelected2[2] = 1     # Sunrise
sendOnlySelected2[1] = 1     # Sunset
sendOnlySelected2[1] = 1     # 

resSoS1 = int("".join(str(x) for x in sendOnlySelected1), 2)        # Converting binary list to integer
resSoS2 = int("".join(str(x) for x in sendOnlySelected2), 2)        # Converting binary list to integer

lpp.append([1, "addDigitalOutput", resSoS1])
lpp.append([2, "addDigitalOutput", resSoS2])



#--------------------------
# Light intensity settings
#--------------------------

# Threshold [lux]
lpp.append([101, "addLuminosity", 0])       # 0-65535

# Safe zone  [lux]
lpp.append([102, "addLuminosity", 0])       # 0-65535



#--------------------------
# Switching times settings
#--------------------------

# Time entry in the format ( H * 3600 ) + ( M * 60 ) + S
# H - hours, M - minutes, S - seconds

# On time1:
time101 = (0*3600)+(0*60)+0

# On time2:
time103 = (0*3600)+(0*60)+0

# On time3:
time105 = (0*3600)+(0*60)+0


# Off time1:
time102 = (0*3600)+(0*60)+0

# Off time2:
time104 = (0*3600)+(0*60)+0

# Off time3:
time106 = (0*3600)+(0*60)+0

lpp.append([101, "addSmallTime", time101])  # On time1:  Set time: 0-86399 seconds;    Time not set: 100000
lpp.append([103, "addSmallTime", time103])  # On time2:  Set time: 0-86399 seconds;    Time not set: 100000
lpp.append([105, "addSmallTime", time105])  # On time3:  Set time: 0-86399 seconds;    Time not set: 100000

lpp.append([102, "addSmallTime", time102])  # Off time1: Set time: 0-86399 seconds;    Time not set: 100000
lpp.append([104, "addSmallTime", time104])  # Off time2: Set time: 0-86399 seconds;    Time not set: 100000
lpp.append([106, "addSmallTime", time106])  # Off time3: Set time: 0-86399 seconds;    Time not set: 100000



#--------------------------
# Sunset / sunrise settings
#--------------------------
lpp.append([101, "addGPS", 49.820923, 18.262524, 0.0])    # Latitude, Longitude, Altitude



#--------------------------
# Encode and send downlink
#--------------------------
payload = cayenneLPP.encodeCayenneLPP(lpp)
postData.sendData(payload, fPort, confirmedDownlink, priority, schedule)