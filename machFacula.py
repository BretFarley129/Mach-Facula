def diff(arr):
    if arr[0] > arr[1]:
        num = arr[0] / arr[1]
        arr[0] = arr[0] - (num*arr[1])

    elif arr[0] < arr[1]:
        num = arr[1] / arr[0]
        arr[1] = arr[1] - (num*arr[0])

def machFacula(M, F):
    arr = [M,F]
    gogogo =True
    while gogogo:
        if arr[0] == 1 or arr[1] == 1:
            print "It works!"
            return True
        elif arr[0] == 0 or  arr[1] ==0:
            print "wompwompwomp"
            return False
        elif arr[0] == arr[1]:
            print "wompwompwomp"
            return False
        else:
            diff(arr)

machFacula(5,12)
machFacula(12,5)
machFacula(5,13)
machFacula(5,20)
machFacula(782394,892835)