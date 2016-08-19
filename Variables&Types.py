mystring = "hello"
myint = 20
myfloat = 10.00

if mystring == "hello":
    print ("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print ("Float: %d" % myfloat)
if isinstance(myint, int) and myint == 20:
    print ("Integer: %d" % myint)
