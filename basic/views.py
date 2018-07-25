# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, Editform
from .models import PersonalDetails, OtherDetails
from .ocr import resizeImage, ocrExtraction, frontSections, backSections
import requests 
import time
from PIL import Image
from collections import OrderedDict

page1list1 = ['FULL NAME', 'APPLYING FOR', 'D.O.B', 'GENDER', 'AADHAR NUMBER', 'BLOOD GROUP', 'RELIGION', 'CATEGORY', 'NATIONALITY', 'ADDRESS', 'CITY', 'STATE', 'PIN CODE', 'COUNTRY', 'SINGLE CHILD?', 'FIRST CHILD?', 'SINGLE PARENT?', 'NO PARENT?']
page2list1 = ['FULL NAME', 'AGE (IN YEARS)', 'EDUCATION', 'OCCUPATION', 'DESIGNATION', 'ANNUAL INCOME', 'OFFICE ADDRESS', 'OFFICE NUMBER', 'MOBILE NUMBER', 'EMAIL']
page2list2 = ['FULL NAME', 'CONTACT NUMBER', 'RELATIONSHIP']
personal_data_list = ['full_nam', 'apply_for', 'dob', 'gender', 'aadhar', 'bg', 'rel', 'cat', 'nat', 'addr', 'city', 'state', 'code', 'country', 'sc', 'fc', 'sp', 'np', 'full_nam1', 'age1', 'edu1', 'occ1', 'des1', 'inc1', 'addr1', 'offnum1', 'mob1', 'email1', 'full_nam2', 'age2', 'edu2', 'occ2', 'des2', 'inc2', 'addr2', 'offnum2', 'mob2', 'email2']
# pdlist = personal_data_list[:18]
# odlist = personal_data_list[18:]

# g = {'ur1': '', 'ur2': '', 'form_id' : ''}
# Create your views here.
def hello(request):
    return render(request, r'basic/home.html')

# def hello2(request):
#     postDataList = []
#     for i in personal_data_list:
#         postDataList.append(dictx[i])
        
#     postDataList = [str(x) for x in postDataList]
#     page1data1 = postDataList[:18]
#     dict1 = OrderedDict(zip(page1list1, page1data1))
#     page2data1 = postDataList[18:28]
#     dict2 = OrderedDict(zip(page2list1, page2data1))
#     page2data2 = postDataList[28:]
#     dict3 = OrderedDict(zip(page2list1, page2data2))
#     print(form_id)
#     #print(listx)
#     # datadict1 = OrderedDict(zip(page1list1, page1data))
#     # datadict2 = OrderedDict(zip(page2list1, page2data1))
#     # datadict3 = OrderedDict(zip(page2list1, page2data2))

#     context = {'dict1':dict1, 'dict2':dict2, 'dict3':dict3}

#     # return HttpResponse('Done')
#     return render(request, r'basic/hello.html', context)

def pageForm(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            # global ur1
            # global ur2
            request.session['your_first_page'] = request.POST['your_first_page']
            request.session['your_second_page'] = request.POST['your_second_page']

            # ur1 = form.cleaned_data['your_first_page']
            # ur2 = form.cleaned_data['your_second_page']
            #print(ur1 + "\n" + ur2)
            return HttpResponseRedirect('/basic/edit')
    else:
        form = NameForm()
        return render(request, r'basic/imageForm.html', {'form': form})

def editable(request):
    if request.method == "POST":
        form = Editform(request.POST)
        # print(form.values())
        if form.is_valid():
            # global form_id
            # form_id = form.cleaned_data['form_id']
            # global dictx
            # dictx = form.cleaned_data
            # print(dictx)
            # global form_id
            formid = form.cleaned_data['form_id']
            pd = PersonalDetails()
            od = OtherDetails()
            pd.form_id = formid
            pd.full_nam = form.cleaned_data['full_nam']
            pd.apply_for = form.cleaned_data['apply_for']
            pd.dob = form.cleaned_data['dob']
            pd.gender = form.cleaned_data['gender']
            pd.aadhar = form.cleaned_data['aadhar']
            pd.bg = form.cleaned_data['bg']
            pd.rel = form.cleaned_data['rel']
            pd.cat = form.cleaned_data['cat']
            pd.nat = form.cleaned_data['nat']
            pd.addr = form.cleaned_data['addr']
            pd.city = form.cleaned_data['city']
            pd.state = form.cleaned_data['state']
            pd.code = form.cleaned_data['code']
            pd.country = form.cleaned_data['country']
            pd.sc = form.cleaned_data['sc']
            pd.fc = form.cleaned_data['fc']
            pd.sp = form.cleaned_data['sp']
            pd.np = form.cleaned_data['np']
            pd.save()

            od.form_id = formid
            od.full_nam1 = form.cleaned_data['full_nam1']
            od.age1 = form.cleaned_data['age1']
            od.edu1 = form.cleaned_data['edu1']
            od.occ1 = form.cleaned_data['occ1']
            od.des1 = form.cleaned_data['des1']
            od.inc1 = form.cleaned_data['inc1']
            od.addr1 = form.cleaned_data['addr1']
            od.offnum1 = form.cleaned_data['offnum1']
            od.mob1 = form.cleaned_data['mob1']
            od.email1 = form.cleaned_data['email1']
            od.full_nam2 = form.cleaned_data['full_nam2']
            od.age2 = form.cleaned_data['age2']
            od.edu2 = form.cleaned_data['edu2']
            od.occ2 = form.cleaned_data['occ2']
            od.des2 = form.cleaned_data['des2']
            od.inc2 = form.cleaned_data['inc2']
            od.addr2 = form.cleaned_data['addr2']
            od.offnum2 = form.cleaned_data['offnum2']
            od.mob2 = form.cleaned_data['mob2']
            od.email2 = form.cleaned_data['email2']
            od.personalDetails = pd

            od.save()
            # formx = OtherDetails.objects.get(form_id = formid)
            # pd.form_id = formid
            # pd.save()
            # print(pd)
            # print(od)

            return HttpResponseRedirect('/basic/view')

    else:
        # global ur1
        # global ur2
        urx = request.session.get('your_first_page')
        ury = request.session.get('your_second_page')
        print(urx)
        print(ury)
        loca = 'C:/ezyschooling/backend/images/cropped.jpg'
        locb = 'C:/ezyschooling/backend/images/cropped2.jpg'
        resizeImage(urx, loca)
        resizeImage(ury, locb)
        frontList = frontSections(loca)
        backList = backSections(locb)

        dataList1 = []
        dataList2 = []

        if (len(frontList) != 0): 
            for f in frontList:
                pol = ocrExtraction(f)
                dataList1.append(pol)

        if (len(backList) != 0): 
            for b in backList:
                pol2 = ocrExtraction(b)
                dataList2.append(pol2)

        p1s1 = dataList1[0]
        p1s2 = dataList1[1]
        p1s3 = dataList1[2]
        p1s4 = dataList1[3]

        p2s1 = dataList2[0]
        p2s2 = dataList2[1]
        p2s3 = dataList2[2]
        p2s4 = dataList2[3]
        p2s5 = dataList2[4]
        p2s6 = dataList2[5]
        # p2s7 = dataList2[6]

        full_nam = str(p1s1[0])
        apply_for = str(p1s1[1])
        dob = str(p1s1[2].replace(' ', ''))
        gender = str(p1s1[3])
        aadhar = str(p1s1[4].replace(' ', ''))
        bg = str(p1s1[5].replace(' ', ''))
        rel = str(p1s1[6])

        cat = str(p1s2[0])

        nat = str(p1s3[0])
        addr = str(p1s3[1] + ', ' + p1s3[2])
        city = str(p1s3[3])
        state = str(p1s3[4])
        code = str(p1s3[5].replace(' ', ''))
        country = str(p1s3[6])

        sc = str(p1s4[0])
        fc = str(p1s4[1])
        sp = str(p1s4[2])
        np = str(p1s4[3])

        full_nam1 = str(p2s1[0])
        age1 = str(p2s1[1].replace(' ', ''))
        edu1 = str(p2s1[2])
        occ1 = str(p2s1[3])
        des1 = str(p2s1[4])

        inc1 = str(p2s2[0] + ' LACS')

        email1 = p2s3[-1]
        mob1 = p2s3[-2]
        offnum1 = p2s3[-3]
        p2s3.remove(email1)
        p2s3.remove(mob1)
        p2s3.remove(offnum1)
        addr1 = ', '.join(p2s3)
        email1 = email1.replace(' ', '')
        offnum1 = offnum1.replace(' ', '')
        mob1 = mob1.replace(' ', '')

            # for i in p2s3:
            #     if i not in [email1, mob1, offnum1]:
            #         addr1.append(i) 

            # addr1 = ', '.join(addr1)

        full_nam2 = str(p2s4[0])
        age2 = str(p2s4[1].replace(' ', ''))
        edu2 = str(p2s4[2])
        occ2 = str(p2s4[3])
        des2 = str(p2s4[4])

        inc2 = str(p2s5[0] + ' LACS')

        email2 = p2s6[-1]
        mob2 = p2s6[-2]
        offnum2 = p2s6[-3]
        p2s6.remove(email2)
        p2s6.remove(mob2)
        p2s6.remove(offnum2)
        addr2 = ', '.join(p2s6)
        email2 = email2.replace(' ', '')
        offnum2 = offnum2.replace(' ', '')
        mob2 = mob2.replace(' ', '')
        # full_nam3 = p2s7[0]
        # mob3 = p2s7[1]
        # reln = p2s7[2]

        personal_data_list = ['full_nam', 'apply_for', 'dob', 'gender', 'aadhar', 'bg', 'rel', 'cat', 'nat', 'addr', 'city', 'state', 'code', 'country', 'sc', 'fc', 'sp', 'np', 'full_nam1', 'age1', 'edu1', 'occ1', 'des1', 'inc1', 'addr1', 'offnum1', 'mob1', 'email1', 'full_nam2', 'age2', 'edu2', 'occ2', 'des2', 'inc2', 'addr2', 'offnum2', 'mob2', 'email2']
        # global personal_data_list2
        personal_data_list2 = [full_nam, apply_for, dob, gender, aadhar, bg, rel, cat, nat, addr, city, state, code, country, sc, fc, sp, np, full_nam1, age1, edu1, occ1, des1, inc1, addr1, offnum1, mob1, email1, full_nam2, age2, edu2, occ2, des2, inc2, addr2, offnum2, mob2, email2]

        # print("hello")
        personal_dict = OrderedDict(zip(personal_data_list, personal_data_list2))
        form = Editform(initial = personal_dict)
        return render(request, r'basic/outputForm.html', {'form21': form, 'dic' : personal_dict})
    

def viewx(request):
    # applicant = PersonalDetails.objects.all()
    parents = OtherDetails.objects.all()
    return render(request, r'basic/view.html',{'par': parents})

def userprofile(request, form_id):
    id = OtherDetails.objects.get(form_id = form_id)
    dblist1 = [id.personalDetails.full_nam, id.personalDetails.apply_for, id.personalDetails.dob, id.personalDetails.gender, id.personalDetails.aadhar, id.personalDetails.bg, id.personalDetails.rel, id.personalDetails.cat, id.personalDetails.nat, id.personalDetails.addr, id.personalDetails.city, id.personalDetails.state, id.personalDetails.code, id.personalDetails.country, id.personalDetails.sc, id.personalDetails.fc, id.personalDetails.sp, id.personalDetails.np]
    dblist2 = [id.full_nam1, id.age1, id.edu1, id.occ1, id.des1, id.inc1, id.addr1, id.offnum1, id.mob1, id.email1]
    dblist3 = [id.full_nam2, id.age2, id.edu2, id.occ2, id.des2, id.inc2, id.addr2, id.offnum2, id.mob2, id.email2]
    d1 = OrderedDict(zip(page1list1, dblist1))
    d2 = OrderedDict(zip(page2list1, dblist2))
    d3 = OrderedDict(zip(page2list1, dblist3))
    context = {'i':id, 'dic1' : d1, 'dic2' : d2, 'dic3' : d3}
    # persDict = {'FULL NAME':id.personalDetails.full_nam, }
    # print(id.values_list())
    return render(request, r'basic/user.html', context)

def editUser(request, form_id):
    id = OtherDetails.objects.get(form_id = form_id)
    print(id.form_id)
    return HttpResponse('hi')
    # return render(request, r'basic/outputForm2.html', {'i': id})

