from alpha import List
from time import sleep

def prime(x):
    
    for c in range(1, x+1):
        if c == 1 or c == x:
            pass
        else:
            r = x%c

            if r == 0:
                return False
    return True


def p_q():
    while True:
        while True:
            try:
                print('\nOnly prime numbers.')
                p = int(input('\nP: '))
                q = int(input('Q: '))

            except:
                print('\n\033[0;31mEnter whole numbers.\033[m')

            else:
                break
            
        
        if p > 2 and q > 2:
            if p*q > 219:
                if prime(p) and prime(q):
                    break
                else:
                    print('\n\033[0;31mYour numbers are not prime numbers.\033[m')
            else:
                print('\n\033[0;31mEnter larger numbers so that their multiplication product is greater than 194.\033[m')
                
        else:
            print('\n\033[0;31mOne or two of its values ​​(p, q) are too small.\033[m')

    return [p, q] 


def ETphi(x):
    print()
    y = 0
    m = []
    ca = []
    for c in range(1, x+1):
        if x%c == 0:
            m.append(c)
    
    for c in range(1, x):
        ca = []
        for a in range(1, c+1):
            if a != 1:
                if c%a == 0:
                    ca.append(a)
        #print(ca)
        t = False        
        for b in range(0, len(ca)):
            if ca[b] in m:
                t = True
        if not t:
            y += 1

    return y,m    


def NED(pq):
    print('\n\033[0;33mCalculating the value of "n"...')
    n = pq[0]*pq[1]
    sleep(1)
    print('\nCalculating the value of "l"...')
    l = ETphi(n)[0]
    sleep(1)
    print('\nCalculating multiples of "n"...')
    mult_n = ETphi(n)[1]
    sleep(1)
    print('\nCalculating multiples of "l"...\033[m')
    mult_l = ETphi(l)[1]
    sleep(1)
    while True:
        while True:
            try:
                e = int(input(f'\nChoose an whole number greater than 1 and less than \033[0;33m{l}\033[m that is coprime with \033[0;33m{l}\033[m and \033[0;33m{n}\033[m.\n\ne: '))
            
            except:
                print('\n\033[0;31mEnter whole number.\033[m')

            else:
                break

        if 1 < e < n:
            for c in mult_n:
                if e != c:
                    c1 = True
                else:
                    c1 = False
                    break

            for c in mult_l:
                if e != c:
                    c2 = True
                else:
                    c2 = False
                    break

            if c1 and c2:
                break
            
            else:
                print('\n\033[0;31mTry another number.\033[m')
        else:
            print('\n\033[0;31mTry another number.\033[m')

    d = 1
    print('\n\033[0;33mCalculating the value of "d"...\033[m')
    sleep(5)
    while True:
        if d*e%l == 1:
            print(f'\033[0;32m{d} ✓\033[m')
            break

        else:
            print(f'\033[0;31m{d} X')
            d += 1
            

    return [n, e, d]


def encrypt(arq, n, e):
    print('\n\033[0;32mEncrypting...\033[m')
    msg = []
    fileR = open(arq, 'r')
    filelist = fileR.readlines()
    #print(filelist)
    for line in filelist:
        m = []
        for l in line:
            for c in range(0, len(List)):
                if l in List[c]:
                    m.append(c)
        msg.append(m)

    fileR.close()
    fileW = open(arq, 'w')

    for m in range(0, len(msg)):
        for a in msg[m]:
            fileW.write(str(a**e % n)+' ')
        if m < len(msg)-1:
            fileW.write('\n')
        else:
            break

    fileW.close()
    print(f'\n{msg}')


def decrypt(arq, n, d):
    print('\n\033[0;32mDecrypting...\033[m')
    msg = []
    fileR = open(arq, 'r')
    filelist =  fileR.readlines()
    
    for line in filelist:
        m = line.split(' ')
        m.append(m)
        msg.append(m)

    fileR.close()
    fileW = open(arq, 'w')
    print(f'\n{msg}')
    for m in range(0, len(msg)):
        for a in msg[m]:
            if a != '\n' and a != '' and type(a) != list:
                ai = int(a)
                alpha_l = (ai**d % n)
                fileW.write(f"{List[alpha_l]}")

        if m < len(msg)-1:
            fileW.write('\n')
        else:
            break

    fileW.close()

    

print('\n\033[0;33mRSA ALGORITHM')
print('-_-'*10,'\033[m')

pq = p_q()
keys = NED(pq)

sleep(3)

encrypt('message.txt', keys[0], keys[1])

sleep(10)

decrypt('message.txt', keys[0], keys[2])
