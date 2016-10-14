import copy
import time
N=15
def area(l):
    minx=7
    maxx=7
    miny=7
    maxy=7
    for i in range(N):
        for j in range(N):
            if(l[i][j]!=0):
                if(j>maxy):
                    maxy=j
                if(j<miny):
                    miny=j
                if(i>maxx):
                    maxx=i
                if(i<minx):
                    minx=i
    #print( [max(0,minx-2),min(N,maxx+2),max(0,miny-2),min(N,maxy+2)])
    return [max(0,minx-2),min(N,maxx+2),max(0,miny-2),min(N,maxy+2)]
def fourinrow(l):
    ans = [0,1,1,1,1,0]
    length=len(l)
    num=0
    if(length>=6):
        for i in range(length-5):
            if(ans==l[i:i+6:1]):
                num+=1
    return num
def fourinrowx(l):
    ansa = [-1,1,1,1,1,0]
    ansb = [0,1,1,1,1,-1]
    length=len(l)
    num=0
    if(length>=6):
        for i in range(length-5):
            if(ansa==l[i:i+6:1] or ansb==l[i:i+6:1]):
                num+=1
    return num
def threeinrow(l):
    ansa = [0,1,1,1,0,0]
    ansb = [0,0,1,1,1,0]
    length=len(l)
    num=0
    if(length>=6):
        i=0
        while(length-5>i):
            if(ansa==l[i:i+6:1] or ansb==l[i:i+6:1]):
                num+=1
                i+=5
            i+=1
    return num
def twoinrow(l):
    ans = [0,0,1,1,0,0]
    length=len(l)
    num=0
    if(length>=6):
        i=0
        for i in range(length-5):
            if(ans==l[i:i+6:1]):
                num+=1
    return num
def analyze(l):
    # 4 in row 011110
    # 4 in rowx 01111-1 or -111110
    # 3 in row 011100 or 001110
    # 2 in row 011000 or 001100 or 000110
    _4inrow=0
    _4inrowx=0
    _3inrow=0
    _2inrow=0
    for i in l:
        _4inrow+=fourinrow(i)
        _4inrowx+=fourinrowx(i)
        _3inrow+=threeinrow(i)
        _2inrow+=twoinrow(i)

    tate=list(map(list, zip(*l)))
    for i in tate:
        _4inrow+=fourinrow(i)
        _4inrowx+=fourinrowx(i)
        _3inrow+=threeinrow(i)
        _2inrow+=twoinrow(i)
    for x in range(-1*N,2*N+1):
        nanameup=[]
        nanamedown=[]
        for i in range(N):
            for j in range(N):
                if((x)==(i+j)):
                    nanameup.append(l[i][j])
                if((x)==(i-j)):
                    nanamedown.append(l[i][j])
        #print( nanamedown)
        _4inrow+=fourinrow(nanameup)
        _4inrowx+=fourinrowx(nanameup)
        _3inrow+=threeinrow(nanameup)
        _2inrow+=twoinrow(nanameup)
        _4inrow+=fourinrow(nanamedown)
        _4inrowx+=fourinrowx(nanamedown)
        _3inrow+=threeinrow(nanamedown)
        _2inrow+=twoinrow(nanamedown)
    #if(sum([_4inrow,_4inrowx,_3inrow])!=0):
    #    print( [_4inrow,_4inrowx,_3inrow,_2inrow])
    return [_4inrow,_4inrowx,_3inrow,_2inrow]
def five(l):
    black=0
    white=0
    for i in l:
        if(i==1):
            black+=1
            white=0
        elif(i==-1):
            white+=1
            black=0
        elif(i==0):
            black=0
            white=0
        if(black>=5 or white >=5):
            return True
    return False

def check(l,x,y):
    nanameup=[]
    nanamedown=[]
    yoko=l[x]
    tate=list(map(list, zip(*l)))[y]
    for i in range(len(l)):
        for j in range(len(l[0])):
            if((x+y)==(i+j)):
                nanameup.append(l[i][j])
            if((x-y)==(i-j)):
                nanamedown.append(l[i][j])
    if(five(nanameup) or five(nanamedown) or five(tate) or five(yoko)):
        return True
    return False


def neg(l):
    inv=[[0 for i in range(len(l))]for i in range(len(l[0]))]
    for i in range(len(l)):
        for j in range(len(l[0])):
            inv[i][j]=-1*l[i][j]
    return inv
def yota(l):
    sttime = time.clock()
    hand=1
    for i in l:
        for j in i:
            if(j!=0):
                hand+=1
    #print( hand)
    #print( hand)
    #If you could win
    for i in range(N):
        for j in range(N):
            if(l[i][j]==0 and hand >=8):
                l_copy = copy.deepcopy(l)
                l_copy[i][j]=1
                if(check(l_copy,i,j)):
                    return [i,j]
    #If you would lose
    for i in range(N):
        for j in range(N):
            if(l[i][j]==0 and hand >=8):
                l_copy = copy.deepcopy(l)
                l_copy[i][j]=-1
                if(check(l_copy,i,j)):
                    return [i,j]
    score=[[0 for i in range(N)]for j in range(N)]
    analyzed=[[[0 for i in range(4)]for j in range(N)]for k in range(N)]
    analyzedinv=[[[0 for i in range(4)]for j in range(N)]for k in range(N)]
    #raw_analyzed=analyze(l)
    entime = time.clock()
    #print( "0="+str(entime - sttime))
    sx,ex,sy,ey=area(l)
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=6):
                l_copy = copy.deepcopy(l)
                l_copy[i][j]=1
                analyzed[i][j]=analyze(l_copy)
                l_copy[i][j]=-1
                analyzedinv[i][j]=analyze(neg(l_copy))
    entime = time.clock()
    #print( "1="+str(entime - sttime))
    #If you make 011110
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=6):
                #print( analyzed[i][j][0])
                if(analyzed[i][j][0]>0):
                    print( "011110 was activated")
                    return [i,j]
    #If opssite cold make 0-1-1-1-10
    for i in range(N):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=6):
                if(analyzedinv[i][j][0]>0):
                    print( "0-1-1-1-10 was activated")
                    return [i,j]
    # 4b2
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=14):
                if(analyzed[i][j][1]>1):
                    print( "# 4b2 was activated")
                    return [i,j]
    # 4w2
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=14):
                if(analyzedinv[i][j][1]>1):
                    print( "# 4w2 was activated")
                    return [i,j]
    # 4b 3b
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=12):
                if(analyzed[i][j][1]>0 and analyzed[i][j][2]>0):
                    print("# 4b3b was activated")
                    return [i,j]
    # 4w 3w
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=12):
                if(analyzedinv[i][j][1]>0 and analyzedinv[i][j][2]>0):
                    print("# 4w3w was activated")
                    return [i,j]
    # 3b 3b
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=10):
                if(analyzed[i][j][2]>1):
                    print("# 23b was activated")
                    return [i,j]
    # 3w 3w
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0 and hand >=10):
                if(analyzedinv[i][j][2]>1):
                    print("# 23w was activated")
                    return [i,j]
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(l[i][j]==0):
                score[i][j]+=int(analyzed[i][j][1])*100000
                score[i][j]+=int(analyzedinv[i][j][1])*100000
                score[i][j]+=int(analyzed[i][j][2])*100000
                score[i][j]+=int(analyzedinv[i][j][2])*1000
                score[i][j]+=int(analyzed[i][j][3])*1000
                score[i][j]+=int(analyzedinv[i][j][3])*100    
                score[i][j]-=abs(i-len(l)/2)+abs(j-len(l)/2)
    max_score=-100000000000000
    #print( "hi")
    ret=[-1,-1]
    for i in range(sx,ex):
        for j in range(sy,ey):
            if(score[i][j]>=max_score and l[i][j]==0):
                max_score=score[i][j]
                ret=[i,j]
    #print( hand+1,max_score)
    entime = time.clock()
    #print( "2="+str(entime - sttime))
    print( "yota placed the stone on "+str(ret)+"it's his "+str(hand)+ "hand")
    return ret