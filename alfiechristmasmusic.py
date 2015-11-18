#for i in range (30):
#    print 1

#t = 7

#u = 10

# while t < 10:
#    print ( t )
#    t = t + 1

import math , random , time

def randlist():
    list = []
    list.append(random.randrange(0,2))
    list.append(random.randrange(0,2))
    list.append(random.randrange(0,2))
    list.append(random.randrange(0,2))
    return list

while 1:
    print randlist()
    time.sleep(1)


# print( 'Rounded Up 9.5:', math.ceil( 9.5 ) )
# print( 'Rounded Down 9.5:', math.floor( 9.5 ) )

# num = 4

# print( num , 'Squared:', math.pow( num , 2 ) )
# print( num , 'Square Root:', math.sqrt( num ) )

# nums = random.sample( range( 0, 5 ) , 5 )

# print( 'Your Lucky Lotto Numbers Are:', nums )

while 1:
    alfiesnumber = random.randrange(0,2)
    print"Number is: ", alfiesnumber
    time.sleep ( 1 )


   