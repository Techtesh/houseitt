from django.shortcuts import render
from django.http import HttpResponse
from . import dbmanager
# Create your views here.

def home(request):
    return render(request,"homepage2.html")
global nxt
nxt=1
val_share=""
val_curfew=""


def add(request):
    addr=request.POST["addr"]
    Type=request.POST["type"]
    students=request.POST["students"]
    times=request.POST["times"]
    rent=request.POST["rent"]
    nego1=request.POST["nego1"]
    deposit=request.POST["deposit"]
    nego2=request.POST["nego2"]
    
    data=[addr,Type,rent,nego1,deposit,nego2,students,times]
    
    res=addr+Type+students+times+rent+nego1+deposit+nego2
    dbmanager.updateDB("calc_primaryform", data)
    
    #columns=['id', 'name', 'address', 'type_of_lease', 'rent', 'nego1', 'deposit', 'nego2', 'type_of_students', 'restrictions']
    columns=dbmanager.column("calc_subform_amenities")
    columns=columns[:-1]
    val_shares=Type
    val_curfew=times 
    #lobal nxt
    nxt=len(columns)
    final=[]
    for index,val in enumerate(columns):
        label="try"+str(index)
        #print(val,type(val))
        try:
            val.index("is")
            final.append((val[2:],0,label))
            #final.append(0)
        except:
            pass
        try:
            val.index("no")
            final.append((val[2:],1,label))
            #final.append(1)
        except:
            pass
    
    #for val in final:
        #print(val)
    
    #nxt=len(final)
    print("form1",len(final),nxt)
            #print(val,"error")
    return render(request,"result2.html",{"valve":final})
    #num1=http




def sub(request):
    outs=[]
    columns=dbmanager.column("calc_subform_amenities")
    columns=columns[:-1]
    nxt=len(columns)
    print("now in subform amenities@@@@@@@@@@@@@@@@@@@@@")
    
    for x in columns:
        print(x)
    
    labels=[]
    print(nxt)
    
    
    for x in range(0,nxt):
        label="try"+str(x)
        
        labels.append(label)
        #print(label,labels)

        print(label)
        labels.append(label)
        temp=request.GET.get(label)
        print(temp)
        outs.append(temp)
    
    
    print(outs)
    
    dbmanager.updateDB("calc_subform_amenities", outs)
    """
    send to database
    """
    columns=dbmanager.column("calc_subform_restrictions")
    
    final=[]
    
    for index,x in enumerate(columns):
        s="try"+str(index)        
        final.append((x,s))
    final=final[:-1]
    print("@@@@@@@@@@@@@@@@@@@@@@",columns)
    print(final)
    return render(request,"result3.html",{"valve":final})



def mul(request):
    outs=[]
    columns=dbmanager.column("calc_subform_restrictions")
    columns=columns[:-1]
    nxt=len(columns)
    print(nxt)
    print("now in subform restrictions@@@@@@@@@@@@@@@@@@@@@")
    
    for x in columns:
        print(x)
    
    labels=[]
     
    for x in range(0,nxt):
        label="try"+str(x)
        
        labels.append(label)
        #print(label,labels)

        print(label)
        labels.append(label)
        temp=request.GET.get(label)
        print(temp)
        outs.append(temp)
    
    
    print(outs)
    
    dbmanager.updateDB("calc_subform_restrictions", outs)
    """
    send to sharing or thankyou 
    """

    return render(request,"result.html")
    

"""
def mul(request):
    outs=[]
    columns=dbmanager.column("calc_subform_restrictions")
    columns=columns[:-1]
    print(columns)
    nxt=len(columns)
   
    for x in columns:
        print(x)
    labels=[]
    print(nxt)
    for x in range(0,nxt):
        label="try"+str(x)
        
        labels.append(label)
        #print(label,labels)

        print(label)
        
        temp=request.GET.get(label)
        #print(temp)
        outs.append(temp)
    print(columns)
    print(outs)
    
    #send to database
    
    columns=dbmanager.column("calc_subform_curfew")
    final=[]
    for x,y in zip(columns,labels):
        
        final.append((x,y))
        
    return render(request,"result.html")
"""  

    