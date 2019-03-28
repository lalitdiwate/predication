
from django import forms

class studentForm(forms.Form):
    fname = forms.CharField(max_length=100)
    mname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    mhcet = forms.FloatField(initial=00)
    diploma = forms.FloatField(initial=00)
    tfws= forms.CharField(max_length=100)
    branch= forms.CharField(max_length=100)
    pwd = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    dfe = forms.CharField(max_length=100)
    cate= forms.CharField(max_length=100)
    year= forms.CharField(max_length=100)

class prefForm(forms.Form):
    fname = forms.CharField(max_length=100)
    mname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    mhcet = forms.FloatField(initial=00)
    diploma = forms.FloatField(initial=00)
    year= forms.CharField(max_length=100)
    cate= forms.CharField(max_length=100)
    branch1= forms.CharField(max_length=100)
    clg1= forms.CharField(max_length=100)
    branch2= forms.CharField(max_length=100)
    clg2= forms.CharField(max_length=100)
    branch3= forms.CharField(max_length=100)
    clg3= forms.CharField(max_length=100)
    branch4= forms.CharField(max_length=100)
    clg4= forms.CharField(max_length=100)
    branch5= forms.CharField(max_length=100)
    clg5= forms.CharField(max_length=100)
    tfws= forms.CharField(max_length=100)
    pwd = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    dfe = forms.CharField(max_length=100)

class storeForm(forms.Form):
    clg_id = forms.IntegerField()
    per_13 = forms.IntegerField()
    per_15 = forms.IntegerField()
    per_16 = forms.IntegerField()
    per_17 = forms.IntegerField()
    per_18 = forms.IntegerField()
    predict = forms.IntegerField()
    branch= forms.CharField(max_length=100)
    cate= forms.CharField(max_length=100)

class clg(forms.Form):
    clg = forms.CharField(max_length=100)