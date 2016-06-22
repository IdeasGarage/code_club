import random
while True:
    dhd == 1
    score = 0
    times_won = 0
    while dhd == 1:
        gfg =input("number")
        genednum = round (random.random() * 10)
        if gfg == genednum:
            if times_won < 6:
                print "yes welldone"
                score = score + 1
                times_won = times_won + 1
                print "score = %s" % score
            else:
                print "yes"
                score = score + 1
                print "score = %s" % score
        else:
            if gfg == "pause_game":
                tdt = 1
                while tdt == 1:
                    pyp =input("paused")
                    if pyp == "resume_game":
                        tdt = 0
                    else:
                        if pyp == "score":
                            print "score = %s" %score
                        else:
                            if pyp == "restart":
            else:
                print "no it was %s" % genednum
