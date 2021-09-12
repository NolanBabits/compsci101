# Author: Nolan Babits
# Main program to read in values and convert from miles (mi) to kilometers (km)

import convly

print ( "1 for ly --> km+mi 2 for ly --> tb units" )

choice = float( input())

if choice == 1 :
    print("lightyears")
    ly_str = float( input())
    ly = int(ly_str)
    mi,km = convly.lyconv(ly)
    print ( "km = {} mi = {}".format(mi,km) )
elif choice == 2 :
    print("lightyears")
    ly_str = float( input())
    ly = ly_str
    ins , ft , mi , cm , m , km = convly.tbconv(ly)
    print ( "in = {} , ft = {} , mi = {} , cm = {} , m = {} , km = {} ".format(ins , ft , mi , cm , m , km) )
    
else :
    print("bad imput use 1 or 2")