n = 0
for c1 in 'АЕКНТЦ':
    for c2 in 'АЕКНТЦ':
        for c3 in 'АЕКНТЦ':
            for c4 in 'АЕКНТЦ':
                for c5 in 'АЕКНТЦ':
                    w = c1+c2+c3+c4+c5
                    n+=1
                    if c1 != 'А' and c1 != 'Е' and c1 != 'К' and w.count('Т') >= 1 and n%2==0:
                        print(w, n)
                        exit(0)