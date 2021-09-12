# Author: Nolan Babits
# Main program to read in values and convert from lightyears (li) to miles (mi) and kilometers (km)

# lyconv converts from lightyears as an integer or float to miles.  
def lyconv ( ly ):
    conv_mi = 5878625352016794
    conv_km = 9460730472580800
    mi = ly * conv_mi
    km = ly * conv_km
    return (mi , km)
def tbconv ( ly ):
    conv_in = 16995200          #ly --> tb in
    conv_ft = conv_in/12        #ly --> tb ft
    conv_mi = conv_ft/5280      #ly --> tb mi
    conv_cm = 47484700          #ly --> tb cm
    conv_m = conv_cm/100        #ly --> tb m
    conv_km = conv_m/1000       #ly --> tb km
    ins = ly * conv_in
    ft = ly * conv_ft
    mi = ly * conv_mi
    cm = ly * conv_cm
    m = ly * conv_m
    km = ly * conv_km
    return( ins , ft , mi , cm , m , km )
    
# Automated Test mi
if __name__ == "__main__":
    n_err = 0
    x = lyconv ( 3 )
    if x !=  (17635876056050382, 28382191417742400):
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
                format (  (17635876056050382, 28382191417742400), x ) )
    x = lyconv ( 0 )
    if x != (0, 0):
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
                format ( 0, x ) )
                
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )


