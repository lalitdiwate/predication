
from django.shortcuts import render


from sklearn.linear_model import LinearRegression  
import numpy as np
# import pandas as pd
from django.http import HttpResponse
from tablib import Dataset
from .models import clg_list,sipna_direct_cutt_offs,tfws_clg_list,predict_table,first_predict_table
import array as ar
# import matplotlib.pyplot as plt
import pickle
from .forms import studentForm,storeForm,clg,prefForm
 


def index(request):
    name = clg_list.objects.all()

    return render(request, "pall.html", {"name":name})


def form(request):
    # name = clg_list.objects.all()
    branch=predict_table.objects.order_by().values('branch').distinct()
    cate=predict_table.objects.order_by().values('cate').distinct()
    clg=clg_list.objects.all()
    return render(request, "preform.html", {"branch":branch,"cate":cate,"clg":clg})

def collage(request):
    # name = clg_list.objects.all()
    collage1 = clg(request.POST)
    if(collage1.is_valid()):
        search = collage1.cleaned_data['clg']
    search = collage1.cleaned_data['clg']

    result = clg_list.objects.filter(name__icontains = search)
    return render(request, "collage.html", {"result":result})
    

def tfws_list(request):
    name1=predict_table.objects.filter(cate="TFWS")
    name2=first_predict_table.objects.filter(cate="TFWS")
    clg=clg_list.objects.all()
    # clg=clg_list.objects.all()
    # data=name1.name
    return render(request, "tfws_list.html", {"name":name1,"name1":name2,"clg_name":clg})

def tfws_score(request,num):
    branch=first_predict_table.objects.filter(clg_id=num,cate="TFWS").values('branch').distinct()
    cate=first_predict_table.objects.filter(clg_id=num,cate="TFWS").values('cate').distinct()

    return render(request, "predict.html", {'branch':branch,'cate':cate})

def score(request,num):
    # data=pd.read_csv(r"C:\Users\Jitesh\Desktop\Cut of list\book6.csv",delim_whitespace=True)
    # data1=pd.DataFrame(data)
    X_train=[]
    y_train=[]
    dt=sipna_direct_cutt_offs.objects.all()
    for cutt in dt:
        X_train.append([cutt.seat_type])
        y_train.append([cutt.GOPEN])


    

    regressor = LinearRegression()  
    regressor.fit(X_train, y_train) 
    X_test=[[2019]] 
    predict1=regressor.predict(X_test)
    branch=predict_table.objects.filter(clg_id=num).values('branch').distinct()
    cate=predict_table.objects.filter(clg_id=num).values('cate').distinct()

    return render(request, "predict.html", {'branch':branch,'cate':cate})


def find_predict(request,num):
    # data=pd.read_csv(r"C:\Users\Jitesh\Desktop\Cut of list\book6.csv",delim_whitespace=True)
    # data1=pd.DataFrame(data)
    # clg_name=num
    # X_train=[]
    # y_train=[]
    # dt=sipna_direct_cutt_offs.objects.all()
    # for cutt in dt:
    #     if((float(cutt.seat_type) > 2) & (float(cutt.seat_type) < 3)):
    #         X_train.append([cutt.seat_type])
    #         y_train.append([cutt.GOPEN])


    # data={'cutt':[y_train],'seat':[X_train]}
    # data1=pd.DataFrame(data)
    # cutt1=data1.loc[data1['seat'] == 1.2015]
    # cutt1=data1.loc[(data1.seat == 5.2016) & (data1.seat == 1.2015)]
    # cutt1=data1.loc[(data1['seat'].isin(1,2)) & (data1['seat'] <= 2.0)]
    StudentForm1 = studentForm(request.POST)
    if(StudentForm1.is_valid()):
        branch = StudentForm1.cleaned_data['branch']
        name = StudentForm1.cleaned_data['fname']
    branch = StudentForm1.cleaned_data['branch']
    name = StudentForm1.cleaned_data['fname']
    cate1=StudentForm1.cleaned_data['cate']
    year=StudentForm1.cleaned_data['year']
    gender=StudentForm1.cleaned_data['gender']
    tfws=StudentForm1.cleaned_data['tfws']
    pwd=StudentForm1.cleaned_data['pwd']
    dfe=StudentForm1.cleaned_data['dfe']
    # regressor = LinearRegression()  
    # regressor.fit(X_train, y_train) 
    # y_test=[[2.2019]] 
    # predict1=regressor.predict(y_test)
    # try:
    if(gender == "male"):
        cate="G"+cate1
    if(gender == "female"):
        cate="L"+cate1
    if(tfws == "yes"):
        cate="TFWS"
    if(dfe == "yes"):
        cate="DEF"
    if(pwd == "yes"):
        cate="PWD"
    if(1==1):
        if(year == "second_year"):
            diploma = StudentForm1.cleaned_data['diploma']
            try:
                predict=predict_table.objects.get(clg_id=num,branch=branch,cate=cate)
                predict1=predict.cuttoff
                predict2=((diploma-20)/predict1)*100
                data=clg_list.objects.get(id=num)
                clg_name=data.name
                if(predict2>100):
                    predict2=100
                return render(request, "resp.html", {"name":name,"branch":branch,"predict1":predict2,"clg_name":clg_name})
            except:
                return render(request, "resp.html", {"name":name,"branch":branch,"msg":"sorry no data "})

                
        if(year == "first_year"):
            mhcet = StudentForm1.cleaned_data['mhcet']
            try:
                predict=first_predict_table.objects.get(clg_id=num,branch=branch,cate=cate)
                predict1=predict.cuttoff
                predict2=((mhcet-20)/predict1)*100
                data=clg_list.objects.get(id=num)
                clg_name=data.name
                if(predict2>100):
                    predict2=100           
                return render(request, "resp.html", {"name":name,"branch":branch,"predict1":predict2,"clg_name":clg_name})
            except:
                return render(request, "resp.html", {"name":name,"branch":branch,"msg":"sorry no data "})


def simple_upload(request):
    if request.method == 'POST':
        person_resource = clg_listResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_clg.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')


def simple_upload(request):
    if request.method == 'POST':
        person_resource = cuttoffResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_clg.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html') 


def  storeform(request):
    return render(request,'store.html',{})


def  store(request):
    storeForm1 = storeForm(request.POST)
    if(storeForm1.is_valid()):
        clg_id = storeForm1.cleaned_data['clg_id']
        branch = storeForm1['branch']
        cate = storeForm1['cate']
        # per_13 = storeForm1['per_13']
        # per_15 = storeForm1['per_15']
        per_16 = storeForm1['per_16']
        per_17 = storeForm1['per_17']
        per_18 = storeForm1['per_18']
    clg_id = storeForm1.cleaned_data['clg_id']
    branch = storeForm1.cleaned_data['branch']
    cate = storeForm1.cleaned_data['cate']
    # per_13 = storeForm1.cleaned_data['per_13']
    # per_15 = storeForm1.cleaned_data['per_15']
    per_16 = storeForm1.cleaned_data['per_16']
    per_17 = storeForm1.cleaned_data['per_17']
    per_18 = storeForm1.cleaned_data['per_18']
    X_train=[[2016],[2017],[2018]]
    # X_train1=[]
    # X_train.reshape(-1, 1)
    y_train=[per_16,per_17,per_18]
    # y_train1=[]
    # y_train.reshape(-1, 1)
    # for dt in X_train:
    #      X_train1.append(dt)
    # for dt in y_train:
    #      y_train1.append(dt)


    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    y_test=[[2019]]
    predict1=regressor.predict(y_test)
    # predict2=((diploma-5)/predict1)*100 
    data=first_predict_table(clg_id=clg_id,branch=branch,cate=cate,per_16=per_16,per_17=per_17,per_18=per_18,cuttoff=predict1)
    data.save()
    return HttpResponse(predict1)
    # return render(request,'store.html',{"msg":per_17})

def pref_score(request):
    prefForm1= prefForm(request.POST)
    if(prefForm1.is_valid()):
        name = prefForm1.cleaned_data['fname']
    name = prefForm1.cleaned_data['fname']
    cate1=prefForm1.cleaned_data['cate']
    year=prefForm1.cleaned_data['year']
    clg1=prefForm1.cleaned_data['clg1']
    branch1=prefForm1.cleaned_data['branch1']
    clg2=prefForm1.cleaned_data['clg2']
    branch2=prefForm1.cleaned_data['branch2']
    clg3=prefForm1.cleaned_data['clg3']
    branch3=prefForm1.cleaned_data['branch3']
    clg4=prefForm1.cleaned_data['clg4']
    branch4=prefForm1.cleaned_data['branch4']
    clg5=prefForm1.cleaned_data['clg5']
    branch5=prefForm1.cleaned_data['branch5']
    gender=prefForm1.cleaned_data['gender']
    tfws=prefForm1.cleaned_data['tfws']
    pwd=prefForm1.cleaned_data['pwd']
    dfe=prefForm1.cleaned_data['dfe']
    if(gender == "male"):
        cate="G"+cate1
    else:
        cate="L"+cate1
    if(tfws == "yes"):
        cate="TFWS"
    if(dfe == "yes"):
        cate="DEF"
    if(pwd == "yes"):
        cate="PWD"
    if(year == "second_year"):
        diploma = prefForm1.cleaned_data['diploma']
        data=clg_list.objects.get(id=clg1)
        clg_name1=data.name
        try:
            p1=predict_table.objects.get(clg_id=clg1,branch=branch1,cate=cate)
            pr1=p1.cuttoff
            pre1=((diploma-20)/pr1)*100
            if(pre1>100):
                pre1=100
        except:
            pre1="no entry for these category"
        data=clg_list.objects.get(id=clg2)
        clg_name2=data.name
        try:
            p2=predict_table.objects.get(clg_id=clg2,branch=branch2,cate=cate)
            pr2=p2.cuttoff
            pre2=((diploma-20)/pr2)*100
            if(pre2>100):
                pre2=100
        except:
            pre2="no entry for these category"
        data=clg_list.objects.get(id=clg3)
        clg_name3=data.name
        try:
            p3=predict_table.objects.get(clg_id=clg3,branch=branch3,cate=cate)
            pr3=p3.cuttoff
            pre3=((diploma-20)/pr3)*100
            if(pre3>100):
                pre3=100
        except:
            pre3="no entry for these category"
        data=clg_list.objects.get(id=clg4)
        clg_name4=data.name
        try:
            p4=predict_table.objects.get(clg_id=clg4,branch=branch4,cate=cate)
            pr4=p4.cuttoff
            pre4=((diploma-20)/pr4)*100
            if(pre4>100):
                pre4=100
        except:
            pre4="no entry for these category"
        data=clg_list.objects.get(id=clg5)
        clg_name5=data.name
        try:
            p5=predict_table.objects.get(clg_id=clg5,branch=branch5,cate=cate)
            pr5=p5.cuttoff
            pre5=((diploma-20)/pr5)*100
            if(pre5>100):
                pre5=100
        except:
            pre5="no entry for these category"
        data = [pre1,pre2,pre3,pre4,54]
        loaded_model = pickle.load(open("LogisticRegression.pkl", 'rb'))
        result = []
        for i in data:
            result.append(loaded_model.predict([[i]]))
        res = []
        for i in result:
            if i == [0]:
                res.append("Sure!!!")
            elif i == [1]:
                res.append("May BE!!")
            elif i == [3]:
                res.append("Nup!!")
        return render(request,"prefresp.html",{"name":name,"year":year,"cate":cate,"branch1":branch1,"predict1":pre1,"clg_name1":clg_name1,"clg_id1":clg1,"branch2":branch2,"predict2":pre2,"clg_name2":clg_name2,"clg_id2":clg2,"branch3":branch3,"predict3":pre3,"clg_name3":clg_name3,"clg_id3":clg3,"branch4":branch4,"predict4":pre4,"clg_name4":clg_name4,"clg_id4":clg4,"branch5":branch5,"predict5":pre5,"clg_name5":clg_name5,"clg_id5":clg5,"result":res,"result1":result})     
    if(year == "first_year"):
        mhcet = prefForm1.cleaned_data['mhcet']
        data=clg_list.objects.get(id=clg1)
        clg_name1=data.name
        try:
            p1=first_predict_table.objects.get(clg_id=clg1,branch=branch1,cate=cate)
            pr1=p1.cuttoff
            pre1=((mhcet-20)/pr1)*100
            if(pre1>100):
                pre1=100
        except:
            pre1="no entry for these category"
        data=clg_list.objects.get(id=clg2)
        clg_name2=data.name
        try:
            p2=first_predict_table.objects.get(clg_id=clg2,branch=branch2,cate=cate)
            pr2=p2.cuttoff
            pre2=((mhcet-20)/pr2)*100
            if(pre2>100):
           
                pre2=100
        except:
            pre2="no entry for these category"
        data=clg_list.objects.get(id=clg3)
        clg_name3=data.name
        try:
            p3=first_predict_table.objects.get(clg_id=clg3,branch=branch3,cate=cate)
            pr3=p3.cuttoff
            pre3=clg3
            if(pre3>100):
           
                pre3=100
        except:
            pre3="no entry for these category"
        data=clg_list.objects.get(id=clg4)
        clg_name4=data.name
        try:
            p4=first_predict_table.objects.get(clg_id=clg4,branch=branch4,cate=cate)
            pr4=p4.cuttoff
            pre4=((mhcet-20)/pr4)*100
            if(pre4>100):
            
                pre4=100
        except:
            pre4="no entry for these category"
        data=clg_list.objects.get(id=clg5)
        clg_name5=data.name
        try:
            p5=first_predict_table.objects.get(clg_id=clg5,branch=branch5,cate=cate)
            pr5=p5.cuttoff
            pre5=((mhcet-20)/pr5)*100
            if(pre5>100):
            
                pre5=100
        except:
            pre5="no entry for these category"           
        my_score = (pre1,pre2,pre3,pre4,pre5)
               
        return render(request,"prefresp.html",{"name":name,"year":year,"cate":cate,"branch1":branch1,"predict1":pre1,"clg_name1":clg_name1,"clg_id1":clg1,"branch2":branch2,"predict2":pre2,"clg_name2":clg_name2,"clg_id2":clg2,"branch3":branch3,"predict3":pre3,"clg_name3":clg_name3,"clg_id3":clg3,"branch4":branch4,"predict4":pre4,"clg_name4":clg_name4,"clg_id4":clg4,"branch5":branch5,"predict5":pre5,"clg_name5":clg_name5,"clg_id5":clg5,})
        

def info(request):
    return render(request,"inform.html",{})

def  user(request):
    return render(request,'user_response.html',{})


def  user_response(request):
    return render(request,'user_response.html',{})

def  show_graph(request,num,cat,branch,year,num1,num2,num3,num4,num5):
    if(year == "first_year"):
        result = first_predict_table.objects.get(clg_id=num,branch=branch,cate=cat)
        ok = "okkk1"


    if(year == "second_year"):
        result = predict_table.objects.get(clg_id=num,branch=branch,cate=cat)
        ok = "okkk2"
            
    return render(request,'graph.html',{"result":result,"predict1":num1,"predict2":num2,"predict3":num3,"predict4":num4,"predict5":num5})



def getpic(request):
    loaded_model = pickle.load(open("LogisticRegression.pkl", 'rb'))
    result = loaded_model.predict([[54]])
    return render(request,'getpic.html',{"result":result})