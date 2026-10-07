n = 0
for c1 in "АЕЛПРЬ":
    for c2 in "АЕЛПРЬ":
        for c3 in "АЕЛПРЬ":
            for c4 in "АЕЛПРЬ":
                for c5 in "АЕЛПРЬ":
                    for c6 in "АЕЛПРЬ":
                        w = c1+c2+c3+c4+c5+c6
                        n+=1
                        if c1 != "А" and c1 != "Л" and w.count('П') >= 2 and n%2==1:
                            print(n, w)
                            exit(0)