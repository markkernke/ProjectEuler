units = [0,3,3,5,4,4,3,5,5,4]
teens = [len('ten'),len('eleven'),len('twelve'),len('thirteen'),len('fourteen'),len('fifteen'),len('sixteen'),len('seventeen'),len('eighteen'),len('nineteen')]
tens = [0,0,len('twenty'),len('thirty'),len('forty'),len('fifty'),len('sixty'),len('seventy'),len('eighty'),len('ninety')]

output = 0

for i in xrange(1,1000):
    if i < 10:
        output += units[i]
    elif i<20:
        output += teens[ int(str(i)[1]) ]
    elif i<100:
        output += tens[ int(str(i)[0]) ]
        output += units[ int(str(i)[1]) ]
    elif i%100==0:
        output += units[ int(str(i)[0]) ] + len('hundred')
    else:
        output += units[ int(str(i)[0]) ] + len('hundredand')
        if i%100 < 10:
            output += units[i%100]
        elif i%100<20:
            output += teens[ int(str(i%100)[1]) ]
        else:
            output += tens[ int(str(i%100)[0]) ]
            output += units[ int(str(i%100)[1]) ]

output += len('onethousand')

print output
