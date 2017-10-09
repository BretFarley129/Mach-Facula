def diff(arr):
    if arr[0] > arr[1]:
        num = arr[0] / arr[1]
        arr[0] = arr[0] - (num*arr[1])
        arr[2] += num

    elif arr[0] < arr[1]:
        num = arr[1] / arr[0]
        arr[1] = arr[1] - (num*arr[0])
        arr[2] += num

def machFacula(M, F):
    arr = [M, F, 0]
    gogogo =True
    while gogogo:
        if arr[0] == 1 or arr[1] == 1:
            if arr[0] == 1:
                arr[2] += (arr[1] - 1)
            if arr[1] == 1:
                arr[2] += (arr[0] - 1)
            print "It works!"
            print "Took {} steps\n".format(arr[2])
            return True
        elif arr[0] == 0 or  arr[1] ==0:
            print "wompwompwomp\n"
            return False
        elif arr[0] == arr[1]:
            print "wompwompwomp"
            return False
        else:
            diff(arr)

machFacula(5,12)
machFacula(12,5)
machFacula(5,13)
machFacula(3,2)
machFacula(5,20)
machFacula(782394,892835)