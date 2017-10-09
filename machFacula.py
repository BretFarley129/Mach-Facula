
''' 
    Mach Facula solution
    -Bret Farley
    -Nicholas Thacker
    -Nicole Ohel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is our solution to the Mach Facula algorthm. I don't really care to explain 
the problem in full, so I'm going to assume that anybody reading this is familiar
with the problem. Looking at the problem we realized a couple things:

    -going from the base (1,1) and working towards the target would be inefficient
    as it would require a breadth-first search and that could potientially require
    a lot of computing power

    -working from the target to the base, the only logical "step back" would be to
    subtract the smaller number from the larger number

    -if at any point either nuber reached 1, the pair would work by default

    -if at any point the 2 numbers were equal to each other the pair would not
    work by default.

Looking at these points, we realized that there are some mathematical properties
that we can compare between the two numbers to further optimize the solution,
we will be posting that to an alternative branch when we get aroud to it.

***We later added code to count the numbers of steps it would take, mainly using
    the diff function***
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The diff() function below is used to find which of the 2 numbers is greater and
set that value equal to itself minus the lesser. To optimize, we find how many 
times the lesser can fit into the greater and decriment the greater by that value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def diff(arr):
    if arr[0] > arr[1]:
        num = arr[0] / arr[1]
        arr[0] = arr[0] - (num*arr[1])
        arr[2] += num

    elif arr[0] < arr[1]:
        num = arr[1] / arr[0]
        arr[1] = arr[1] - (num*arr[0])
        arr[2] += num

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the meta-logic function. We run some checks:
    a)is either number equal to 1?
        -if so, it works
    b)is either number equal to 0?
        -if so, it doesn't work. this can be optimized
    c)are the 2 numbers equal?
        -if so, it doesn't work
    
after these checks, we run the diff function and run back through the loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

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

