def ten(tn):
    if(tn=="10"):
        return "Ten"
    elif(tn=="11"):
        return "Eleven"
    elif(tn=="12"):
        return "Twelve"
    elif(int(tn[1])>2):
        return num(tn[1])+"teen"

def num(d):
    
    if(d=="2"):
        return "Twen"
    elif(d=="3"):
        return "Thir"
    elif(d=="4"):
        return "Four"
    elif(d=="5"):
        return "Fif"
    elif(d=="6"):
        return "Six"
    elif(d=="7"):
        return "Seven"
    elif(d=="8"):
        return "Eight"
    elif(d=="9"):
        return "Nine"

    
def nums(ds):

    if(ds=="1"):
        return "one"
    elif(ds=="2"):
        return "two"
    elif(ds=="3"):
        return "three"
    elif(ds=="4"):
        return "four"
    elif(ds=="5"):
        return "five"
    elif(ds=="6"):
        return "six"
    elif(ds=="7"):
        return "seven"
    elif(ds=="8"):
        return "eight"
    elif(ds=="9"):
        return "nine"
    else:
        return ""

def zz(dd):
    if(dd[0]=="1"):
        return "ten"
    elif dd[0]!="0":
        return num(dd[0])+"ty"
    else:
        return ""
    
def cal(dg):
    if len(dg)==1:
        return nums(dg)
    
    elif dg[1]=="0":
        return zz(dg)
    elif(dg[0]=="1"):
        return ten(dg)
    else:
        return num(dg[0])+"ty "+nums(dg[1])

def unit(n):
    if len(n) >0 and len(n)<8:
        ln=len(n)

        if ln==1 or ln==2:
           return cal(n)
        
        elif ln==3:
            if cal(n[0])!="":
                return cal(n[0])+" Hundred "+cal(n[1:])
            else:
                return cal(n[1:])

        elif ln==4:
            if cal(n[0])!="":
                return cal(n[0])+" Thousand "+unit(n[1:])
            else:
                return unit(n[1:])
                
        
        elif ln==5:
            if cal(n[:2])!="":
                return cal(n[:2])+" Thousand "+unit(n[2:])
            else:
                return unit(n[2:])

        elif ln==6:
            if cal(n[0])!="":
                return cal(n[0])+" Lakh "+unit(n[1:])
            else:
                return unit(n[1:])
        
        elif ln==7:
            if cal(n[:2])!="":
                return cal(n[0:2])+" Lakh "+unit(n[2:])
            else:
                return unit(n[2:])

def conv(n):
    ln=len(n)
    if ln>0 and ln<8:
        return(unit(n))
    
    elif ln >7:
        rem= len(n)-7
        if unit(n[:rem])!="":
            return unit(n[:rem])+" Crore "+unit(n[rem:])
        else:
            return unit(n[rem:])



n=input("Enter a amount to convert into word : ")
if len(n)<15 and len(n)>0:
    res = conv(n)
    if res=="":
        res = "Zero Rupee"
    else:
        res+=" Rupees"
else:
    res="Input length will be 1 to 14"
    
print(res)
