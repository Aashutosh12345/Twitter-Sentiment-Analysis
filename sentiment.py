b,a,h,t=[],[],{},[]
accurate=k=0
key=''
fn=open('AFINN-111.txt')
for line in fn:
    b.append(line.split())
#print(b)
for i in range(0,len(b)):
    if len(b[i])!=2:
        for j in range(0,len(b[i])-1):
            key+=b[i][j]+' '
        h[key]=b[i][-1]
    else:
        h[b[i][0]]=b[i][1]
f=open('clean_ElectionGujrat2017.txt')
for line1 in f:
    a.append(line1.split('|'))
for i in range(0,len(a)):
    t.append(a[i][3].split())
#print(t)
for i in t:
    sum=0
    for j in i:
        try:
            sum+=int(h[j])
        except:
            sum+=0
    #print(sum,'  ',a[k][-1])
    if(sum>0):
        print("Positive | ",i)
    elif(sum==0):
        print("Neutral | ",i)
    else:
        print("Negative | ",i)
    if (k!=0 and sum==int(a[k][-1])):
        accurate+=1
    k+=1            
accuracy=accurate*100.0/(len(a)-1)
print('Accuracy = ',accuracy,'%')
