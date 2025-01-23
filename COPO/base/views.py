from django.shortcuts import render
from django.core.files import File
from django.contrib.auth.decorators import login_required
from .form import ExcelForm
from .ExcelCal import *
from .models import Attainment,CourseOutcome,CalculateExcel
import os
from django.contrib.auth.models import User

@login_required(login_url='user-login')
def index(request):
    print(request.method)
    if request.method == 'POST':
        print(request.user)
        form_t = ExcelForm(request.POST,request.FILES,initial={'userId':request.user})
        co = request.POST['courseOutCome']
        at = request.POST['attainment']
        type1 = request.POST['type']
        
        
        print(co,at)
        
        CO = CourseOutcome.objects.filter(name = co)
        AT = Attainment.objects.filter(name = at)
        
        CourseOutcomeT = []
        
        for c in CO:
            CourseOutcomeT.append(c.per1)
            CourseOutcomeT.append(c.per2)
            CourseOutcomeT.append(c.per3)
            CourseOutcomeT.append(c.per4)
        
        AttainmentT = []
        
        for a in AT:
            AttainmentT.append(a.IA_1)
            AttainmentT.append(a.IA_2)
            AttainmentT.append(a.Assignment)
            AttainmentT.append(a.ESE)
            
        
        print(AttainmentT,CourseOutcomeT)
        if form_t.is_valid():
            in_file = request.FILES['file']
            out_file, name = cal(in_file,CourseOutcomeT,AttainmentT,type1)
            print(name)
            obj = form_t.save(commit=False)
            obj.userId = request.user
            obj.save()
            print(obj.file.path)
            os.remove(obj.file.path)
            os.rename(name,obj.file.path)

            context = {
                "excel_data" : out_file
            }
            return render(request,'dashboard/index.html',context)
        else:
            print(form.errors)
        return render(request,'dashboard/index.html')
    else:
        form = ExcelForm
        context = {
            'form' : form
        }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='user-login')
def storage(request):
    userId = request.user
    print(userId)
    #items = CalculateExcel.objects.all()
    items = CalculateExcel.objects.filter(userId=userId)
    context = {
        'items' : items
    }
    return render(request,'dashboard/storage.html',context)

import struct
import json
@login_required(login_url='user-login')
def View(request,pk):
    useID = request.user
    items = CalculateExcel.objects.get(id=pk)
    name = items.file.path
    B = BytesIO()
    with open(os.path.abspath(name),'rb') as fh:
        B=BytesIO(fh.read())
    #wb = load_workbook(name,data_only=True)
    #wb.save(B)
    int_list = struct.unpack(f"{len(B.getvalue())}B",B.getvalue())
    json_string = json.dumps(int_list)
    context = {
        "excel_data":json_string
    }
    
    return render(request,'dashboard/view.html',context)