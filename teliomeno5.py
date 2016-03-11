year = input ("Dwse Xrono : ")
month = input ("Dwse Mina : ")
day = input ("Dwse Mera : 21")
cc = year/100
yy = year - ((year/100)*100)
c = (cc/4) - 2*cc-1
y = 5*yy/4
m = 26*(month+1)/10
d = day
dayofweek = (c+y+m+d)%7
if (dayofweek == 0):
    print "Kiriaki"
elif (dayofweek == 1):
    print "Deftera"
elif (dayofweek == 2):
    print "Triti"
elif (dayofweek == 3):
    print "Tetarti"
elif (dayofweek == 4):
    print "Pempti"
elif (dayofweek == 5):
    print "Paraskevi"
elif (dayofweek == 6):
    print "Savvato"
else:
    print "Error"



