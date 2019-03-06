enc = {}

def encodeTable(s):
    l = len(s)
    count = 1
    i=0
    while i<l:
        #print(i)
        if s[i] not in enc:
            #print(" S [i] :",s[i])
            enc[s[i]] = count
            count += 1
        else:
            s1=s[i]
            i += 1
            while i < l:
                s1 = s1 + s[i]
                #print("S1 ",s1)
                if s1 not in enc:
                    enc[s1] = count
                    count+=1
                    break
                i+=1

        i+=1
    print("Encoded Table : ")
    print(enc)
    print("Length of Encoded Table : ", len(enc))

def  encode(s):
    print("\nMessage Encoding...")
    n=len(s)
    i=0
    t=""
    k=[]
    l=[]
    e=""
    while i<n:
        t+=s[i]

        if t not in l:
            l.append(t)
            t=""

            l.append(t)
        i+=1

    l.append(t)

    for l in l:
        if l != '':
            k.append(l)

    #print(k)
    p=[]
    for i in k:

        n=len(i)
        if n==1:
            e += str(enc[i])
        else:
            i = i[::-1]
            k=""
            k=i[0]
            p=""
            p=i[1::]
            #print(i, k,p)
            p = p[::-1]
            e+=(str(enc[p])+k)

    print("Encoded Code : ", e)
    print("Length of Encoded String : ", len(e))
    return e

def decode(enc,s):
    print("\nMessage Decoding...")
    n=len(s)
    e=''
    for i in s:
        if i.isalpha():
            e+=i
        else:
            for x,y in enc.items():
                if y==int(i):
                    e+=x
                    break

    print("Decoded String : ",e)




s =input()
print("\nInput String : ",s)
print("Length of input String : ",len(s),"\n")

encodeTable(s)
encodedString = encode(s)
decode(enc,encodedString)
