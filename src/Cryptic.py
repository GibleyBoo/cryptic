import sys
if len(sys.argv) >= 4:
    print("cbb, kms")
elif len(sys.argv) == 3:
    print(str(sys.argv))
elif len(sys.argv) == 2:
    sum = 0
    for arg in sys.argv:
        sum+=int(arg)
    print(sum)
elif len(sys.argv) == 1:
    print("So you're saying "+str(sys.argv)+"?")
elif len(sys.argv) == 0:
    print("The program doesn't know what to do! Closing...")