#!/usr/bin/env python
#coding: utf-8
import sys,time

j1,j2,j3,j5,j6 = 0,60,0,0,0

while True:
    # $B%m%\%C%H$N3QEY$NFI$_9~$_<~4|$O(B20ms$B!J%"%P%&%H$G$9!K(B
    time.sleep(0.05)

    ch0 = 0
    delta = 0

    #$B%A%c%s%M%k(B0$B$N(BAD$B%3%s%P!<%?$NCM$rFI$_9~$`!J5wN%%;%s%5!K(B
    with open("/run/shm/adconv_values","r") as sensor:
        vs_str = sensor.readline().rstrip().split()
        ch0 = int(vs_str[0])

    #$B5wN%%;%s%5$NCM$,(B300$B0J>e$J$i@5$NJ}8~(B
    #$B$=$&$G$J$1$l$PIi$NJ}8~$K2s$k(B
    delta = 1 if ch0 > 300 else -1

    #$B$b$&8~$-$,9T$-$9$.$F$$$?$i;_$a$F$*$/(B
    if j1 < -90 and delta < 0:  continue 
    if j1 > 90 and delta > 0:   continue 

    j1 += delta

    #$B%"!<%`$N3QEY$r;XDj(B
    s = "%d,%d,%d,%d,%d\n" % (j1,j2,j3,j5,j6)
    with open("/run/shm/angles","w") as arm:
        arm.write(s)
        print >> sys.stderr, s
