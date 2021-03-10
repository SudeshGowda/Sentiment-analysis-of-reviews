while(True):
    y = int(input())
    x1 = int(input())
    x2 = int(input())
    if(y*(21*x1**2-22.627417*x1*x2+22*x2**2-110)>-0.001):
        print("True")
    else:
        print("F")