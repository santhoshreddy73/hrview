
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from .models import *
from datetime import datetime
from num2words import num2words
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings 

from letter_generators.appointment_letter import apt_generator
from letter_generators.termination_letter import termination_letter_generator
from letter_generators.letter_of_intent import intent_letter_generator
from letter_generators.increment_letters import hike_generator
from letter_generators.service_agreement import service_agreement_generator
from letter_generators.issue_internhsip_certificate import issue_internship_certificate
from letter_generators.offer_letter_creator import Offer_letter_generator

from django.core.mail import send_mail
import datetime as DT
from django.core.mail import EmailMessage
# self-written app/code for converting integers to the Indian_reading format
 
apt_creation_controller=1
Id=0

def num2Indian_num_sys(number):
    num=str(number)
    l=len(num)
    res=[]
    x=list(num)
    if l%2==0 and l>=4:
        for i in range(len(x)):
            if i!=len(x)-3:
                if i%2!=0 and i!=0:
                    res.append(x[i])
                elif i==0:
                    res.append(str(x[i]+','))
                else:
                    res.append(x[i]+',')
            else:
                res.append(str(x[i]+x[i+1]+x[i+2]))
                break
        result=''.join(res)

    elif l%2!=0 and l>3:
        for i in range(len(x)):
            if i!=len(x)-3:
                if i%2==0:
                    res.append(x[i])
                else:
                    res.append(x[i]+',')
            else:
                res.append(str(x[i]+x[i+1]+x[i+2]))
                break
        result=''.join(res)

    else:
        result=num
    return result

def read_num_in_Indian_format(number):
    x=num2Indian_num_sys(int(number))
    y=x.split(',')
    res=[]
    j=0
    result=''
    for i in y:
        res.append([int(i),len(y)-j])
        j+=1

    for i in res:
        if i[1]==4:
            if i[0]!=0:result+=num2words(i[0])+' crore  '
        elif i[1]==3:
            if i[0]!=0:result+=num2words(i[0])+' lakh  '
        elif i[1]==2:
            if i[0]!=0:result+=num2words(i[0])+' thousand '
        elif i[1]==1:
            if i[0]!=0:result+=num2words(i[0])
    return result


# Create your views here.
def home_login(request):
    if request.method=='POST':

        id=request.POST['id']
        pswrd=request.POST['password']
        if id.endswith('@fourninecloud.com'):

            try:
                usrname=User.objects.get(email=id).username
                #print(usrname)
                uSer=authenticate(request,username=usrname,password=pswrd)
                login(request,uSer)
                record=records.objects.create(user=uSer.username,record='user logged in at ',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                record.save()
                return redirect('main')
            except:
                messages.error(request,'details not found maybe incorrect details')
                return render(request,'app/desinged_login_page.html')
        elif id.endswith('.com'):
            messages.error(request,'only@fourninecloud.com emails allowed here')
            return render(request,'app/desinged_login_page.html')

        else:
            try:
                uSer=authenticate(request,username=id,password=pswrd)
                login(request,uSer)
                record=records.objects.create(user=uSer.username,record='user logged in at ',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                record.save()
                return redirect('main')
            except:
                messages.error(request,'details not found')
                return render(request,'app/desinged_login_page.html')
    else:
        return render(request,'app/desinged_login_page.html')
def logout_user(request):
    record=records.objects.create(user=request.user.username,record='loggged out at ',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    record.save()
    logout(request)
    messages.success(request,'succesfully logged out')

    return redirect('/')

@login_required(login_url='main')
def home(request):
    intrns=Interns.objects.all().order_by('name')
    employs=employees.objects.all().order_by('name')
    if request.method=='POST':
        srch=request.POST['search']
        intrns=Interns.objects.all().filter(name__icontains=srch).order_by('name')
        employs=employees.objects.filter(name__icontains=srch).order_by('name')
    if employs.count==0 :
        messages.info(request,'HR View app welcomes,try creating some letters')
    if intrns.count==0:
        messages.info(request,'no intern available right now')
    recrds=records.objects.all().order_by('date').reverse()
    #print(request.user.username)
    return  render(request,'app/home.html',{'employees':employs,'records':recrds,'interns':intrns})


@login_required(login_url='main')
def download_apt_letter_for_existing_user(request,pk):
    dt=datetime.today()
    emp=employees.objects.get(id=pk)
    paTh="media/appointment_letters/"+str(emp.id)+"_appointment.pdf"
    if request.method=='POST':
        header=request.POST['header']
        naMe=request.POST['fullname']
        roLe=request.POST['role']
        date=request.POST['date']
        ctc=request.POST['ctc']
        jOin_date=request.POST['join_date']
        
        notice_Period=request.POST['notice_period']
        reprts_to=request.POST['reports_to']
        if date!='':
            x=list(map(int,date.split('-')))
            y=datetime(x[0],x[1],x[2])
            z=y.strftime('%b %d,%Y')
            ref=datetime.now().strftime('%Y/%d/%m/%H%M')
        else:
            y=''
            z=''
            ref=''
        try:
            f=read_num_in_Indian_format(ctc)
        except:
            f=0
        cTc=num2Indian_num_sys(ctc)
        apt_generator(
            header=header,
            date=z,
            name=naMe,
            role=roLe,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            ctc_in_words=f,
            annual_ctc=cTc,
            notice_period=notice_Period,
            reports_to=reprts_to,
            path=paTh,
            join_date=jOin_date
        )

        y=datetime.today()
        emp.name=naMe
        emp.role=roLe
        emp.join_date=jOin_date
        emp.annual_package=ctc
        
        emp.appointmentletter_issued_on=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        emp.notice_period=notice_Period
        emp.save()
        try:
            apt=Appointment_Letters.objects.get(employee=emp)
        except:
            apt=Appointment_Letters.objects.create(employee=emp,path=paTh)
            apt.save()
        record=records.objects.create(user=request.user.username,record='downloaded appointment letter for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        record.save()
        download_record=download_records.objects.create(user=request.user.username,downloads='downloaded appointment letter for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        download_record.save()
        try:
            #store file
            pass
        except:
            #store_file
            pass
        return render(request,'app/download_employee_appinmntletter.html',{'emplye':emp,'download_link':paTh,'dt':dt})
    else:
        return render(request,'app/download_employee_appinmntletter.html',{'emplye':emp,'download_link':paTh,'dt':dt})
        


@login_required(login_url='main')
#employees hike details operation function
def employee_hike(request,pk):
    emploYee=employees.objects.get(id=pk)
    hikes=Employees_hike.objects.filter(employee=emploYee).order_by('-id')
    return render(request,'app/employees_hike_details.html',{'employee':emploYee,'hikes':hikes})


@login_required(login_url='main')
def termination_letter(request,pk):
    employee=employees.objects.get(id=pk)
    paTH='media/termination_letters/'+str(employee.id)+'trm_ltr.pdf'
    if request.method=='POST':
        naMe=request.POST['fullname']
        header=request.POST['header']
        roLe=request.POST['role']
        date=request.POST['date']
        join_Date=request.POST.get('join_date')
        trm_date=request.POST['trm_date']
        #doc=MailMerge('media/doc_service.docx')
        x=list(map(int,date.split('-')))
        y=datetime(x[0],x[1],x[2])
        z=y.strftime('%b %d,%Y')
        termination_letter_generator(
                header=header,
                date=str(z),
                role=roLe,
                name=naMe,
                ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
                join_date=join_Date,
                termination_date=str(trm_date),
                path=paTH
        )
        date=datetime.now()
        #print(employee.termination_letter_issued)
        try:
            employee.termination_letter_issued=date.strftime('%Y-%m-%d %H:%M:%S')
            employee.save()
            try:
                trm=Termination_Letters.objects.get(employee=employee)
            except:
                #print('tst123')
                trm=Termination_Letters.objects.create(employee=employee,path=paTH)
                #print('3')
                trm.save()
            record=records.objects.create(user=request.user.username,record='issued termination  letter for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            download_record=download_records.objects.create(user=request.user.username,downloads='issued termination  letter for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            messages.info(request,'succesfully updated and downloaded the doc ')
        except:
            messages.info(request,'error updating the file')
        #return redirect('/preview_termination_ltr/'+str(pk))
        return render(request,'app/termination_doc.html',{'employee':employee,'date':datetime.today(),'doWnload_link':paTH})

    else:
        return render(request,'app/termination_doc.html',{'employee':employee,'date':datetime.today(),'doWnload_link':paTH})


@login_required(login_url='main')
def hike_issue(request,pk):
    emploYee=employees.objects.get(id=pk)
    if request.method=='POST':

        hik=Hike_letters.objects.create(employee=emploYee)
        t=hik.id
        paTh='media/increment_letters/'+str(t)+'_increment.pdf'
        #print(emploYee.annual_package)
        header=request.POST['header']
        worth=request.POST['hike_worth']
        date=request.POST['date']
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        start_date=list(map(int,start_date.split('-')))
        end_date=list(map(int,end_date.split('-')))
        sTart_date=datetime(start_date[0],start_date[1],1).strftime('%b %Y')
        eNd_date=datetime(end_date[0],end_date[1],1).strftime('%b %Y')
        start_date=datetime(start_date[0],start_date[1],1).strftime('%Y-%m-01')
        end_date=datetime(end_date[0],end_date[1],1).strftime('%Y-%m-01')

        #print(start_date)
        x=map(int,date.split('-'))
        x=list(x)
        date=datetime(x[0],x[1],x[2])
        #print('test',date)
        var=date
        #doc=MailMerge('media/increment_doc.docx')
        hike_generator(
            header=header,
            daTe=date.strftime('%b %d,%Y'),
            increment_effective_date=date.strftime('%b %d,%Y'),
            name=emploYee.name,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            increment_in_words=read_num_in_Indian_format(int(worth)),
            duration=sTart_date+'-'+eNd_date,
            path=paTh
        )
        #doc.write(paTh)
        hik.path=paTh
        hik.Created=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hik.save()

        emp_hike=Employees_hike.objects.create(employee=emploYee,hike=worth,hike_duration_start_year=start_date,hike_duration_end_year=end_date)
        emp_hike.hike_letter_issued_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        emp_hike.path=paTh
        emp_hike.save()
        if emploYee.annual_package!=None:
            emploYee.annual_package=int(emploYee.annual_package)+int(worth)
        else:
            emploYee.annual_package=int(worth)
        emploYee.save()

        record=records.objects.create(user=request.user.username,record='issued hike letter for '+emploYee.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        record.save()
        download_record=download_records.objects.create(user=request.user.username,downloads='issued hike letter for '+emploYee.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        download_record.save()
        #print(emploYee.annual_package)
        t=emp_hike.id
        messages.info(request,'hike isssued successfully')
        return redirect('/view_hik/'+str(t))
    return render(request,'app/emloyee_hike_issue.html',{'employee':emploYee})

@login_required(login_url='main')
def main(request):
    #print('url compoinent',request.path)
    if request.method=='POST':
        if request.POST.get('form_id') == 'global_search':
            srch=request.POST['global_search']
            test=srch.split('&&')
            letters_srch=srch.split('^')
            if len(test)>=2:
                
                intrns=Interns.objects.all().filter(Q(name__icontains=test[0])).order_by('name')
                employs=employees.objects.filter(Q(name__icontains=test[0]) and( Q(join_date__icontains=test[1]) | Q(appointmentletter_issued_on__icontains=test[1]) | Q(termination_letter_issued__icontains=test[1]) | Q(letter_of_intent_issued_date__icontains=test[1]) | Q(offer_letter_issued_datetime__icontains=test[1])) ).order_by('name')
                if employs.count==0 and intrns.count==0:
                    messages.info(request,'no data for'+srch)
                    return  render(request,'app/home.html',{'employees':employs,'interns':intrns})
                return  render(request,'app/home.html',{'employees':employs,'interns':intrns})  
            elif len(letters_srch) ==2:  
                test=letters_srch
                if test[1]=='appointment_letter' or test[1]=='apt' or test[1]=='appointment':
                    appoint_letters=Appointment_Letters.objects.filter(employee__name__icontains=test[0])
                    dict={'appoint_letters':appoint_letters}
                    return render(request,'app/letters_bucket.html',dict)

                elif test[1]=='termination' or test[1] == 'trm'or test[1] == 'termination_letter':
                    termination_letters=Termination_Letters.objects.filter(employee__name__icontains=test[0])
                    dict={'termination_letters':termination_letters}
                    return render(request,'app/letters_bucket.html',dict)

                elif test[1]=='service_letters' or test[1] =='srv' or test[1] =='service_agreements' or test[1]=='service' or test[1]=='service agreements':
                    service_letters=Service_letters.objects.filter(employee__name__icontains=test[0])
                    dict={'service_letters':service_letters}
                    return render(request,'app/letters_bucket.html',dict)

                elif test[1]=='intent_letter' or test[1]=='intent_ltr' or test[1]=='int'or  test[1]=='intl'or test[1]=='intent' or test[1]=='letter of intent' or test[1]=='intent letter' :
                    intent_ltrs=Intent_Letters.objects.filter(employee__name__icontains=test[0])
                    dict={'intent_ltrs':intent_ltrs}
                    return render(request,'app/letters_bucket.html',dict)

                elif test[1]=='offer_letter' or test[1]=='off_l' or test[1]=='off'or  test[1]=='offr_l'or test[1]=='offer_l' or test[1]=='offer letter'  :
                    off_ltrs=Offer_Letters.objects.filter(employee__name__icontains=test[0])
                    dict={'offr_ltrs':off_ltrs}
                    return render(request,'app/letters_bucket.html',dict)
                else:
                    appoint_letters=Appointment_Letters.objects.filter(employee__name__icontains=test[0])
                    termination_letters=Termination_Letters.objects.filter(employee__name__icontains=test[0])
                    service_letters=Service_letters.objects.filter(employee__name__icontains=test[0])
                    intent_ltrs=Intent_Letters.objects.filter(employee__name__icontains=test[0])

                    intern_ltrs=Intenship_certificates.objects.filter(intern__name__icontains=test[0])
                    hik_ltrs=Hike_letters.objects.filter(employee__name__icontains=test[0])
                    off_ltrs=Offer_Letters.objects.filter(employee__name__icontains=test[0])
                    dict={'appoint_letters':appoint_letters,'termination_letters':termination_letters,'service_letters':service_letters,'intent_ltrs':intent_ltrs,'intern_ltrs':intern_ltrs,'hik_ltrs':hik_ltrs,'offr_ltrs':off_ltrs}
                   
                    if appoint_letters.count()==0 and termination_letters.count()==0 and intent_ltrs.count()==0  and hik_ltrs.count()==0 and off_ltrs.count()==0 and service_letters.count()==0  :
                        messages.error(request,'no letter available,on search for '+srch)
                        dict={}
                    return render(request,'app/letters_bucket.html',dict)
                
            else:
                intrns=Interns.objects.all().filter(name__icontains=srch).order_by('name')
                employs=employees.objects.filter(name__icontains=srch).order_by('name')
                return  render(request,'app/home.html',{'employees':employs,'interns':intrns})
    return render(request,'app/services_page.html')
#app/services_page.html

@login_required(login_url='main')
def user_activities(request):
    recrds=records.objects.all().order_by('date').reverse()
    return render(request,'app/user_records.html',{'records':recrds})

@login_required(login_url='main')
def user_downloads(request):
    download_recrds=download_records.objects.all().order_by('date').reverse()
    return render(request,'app/user_downloads.html',{'download_records':download_recrds})

@login_required(login_url='main')
def view_issued_letters(request):
    if request.method=='POST':
        
        
        srch=request.POST['search']
        test=srch.split('^')
    
        if len(test)>=2:
            test[1]=test[1].lower()

            if test[1]=='appointment_letter' or test[1]=='apt' or test[1]=='appointment':
                appoint_letters=Appointment_Letters.objects.filter(employee__name__icontains=test[0])
                dict={'appoint_letters':appoint_letters}
                return render(request,'app/letters_bucket.html',dict)

            elif test[1]=='termination' or test[1] == 'trm' or test[1] == 'termination_letter' or test[1] == 'trml' :
                termination_letters=Termination_Letters.objects.filter(employee__name__icontains=test[0])
                dict={'termination_letters':termination_letters}
                return render(request,'app/letters_bucket.html',dict)

            elif test[1]=='service_letters' or test[1] =='srv' or test[1] =='service_agreements' or test[1]=='service' or test[1]=='service agreements':
                service_letters=Service_letters.objects.filter(employee__name__icontains=test[0])
                dict={'service_letters':service_letters}
                return render(request,'app/letters_bucket.html',dict)

            elif test[1]=='intent_letter' or test[1]=='intent_ltr' or test[1]=='int'or  test[1]=='intl'or test[1]=='intent' or test[1]=='letter of intent' or test[1]=='intent letter' :
                intent_ltrs=Intent_Letters.objects.filter(employee__name__icontains=test[0])
                dict={'intent_ltrs':intent_ltrs}
                return render(request,'app/letters_bucket.html',dict)
            
            elif test[1]=='offer_letter' or test[1]=='off_l' or test[1]=='off'or  test[1]=='offr_l'or test[1]=='offer_l' or test[1]=='offer letter' or test[1]=='offl'  :
                off_ltrs=Offer_Letters.objects.filter(employee__name__icontains=test[0])
                dict={'offr_ltrs':off_ltrs}
                return render(request,'app/letters_bucket.html',dict)

            else:
                messages.error(request,'no letter available,on search for '+srch)
                return render(request,'app/letters_bucket.html')
        else:
            appoint_letters=Appointment_Letters.objects.filter(employee__name__icontains=srch).order_by('employee__appointmentletter_issued_on').reverse()
            termination_letters=Termination_Letters.objects.filter(employee__name__icontains=srch)
            service_letters=Service_letters.objects.filter(employee__name__icontains=srch)
            intent_ltrs=Intent_Letters.objects.filter(employee__name__icontains=srch)

            intern_ltrs=Intenship_certificates.objects.filter(intern__name__icontains=srch)
            hik_ltrs=Hike_letters.objects.filter(employee__name__icontains=srch)
            off_ltrs=Offer_Letters.objects.filter(employee__name__icontains=srch)
                #print('test after appointment letter')
                #print(appoint_letters.count())
            if appoint_letters.count() == 0 and termination_letters.count() == 0 and intern_ltrs.count() == 0 and service_letters.count() == 0 and intern_ltrs.count() == 0 and hik_ltrs.count() == 0 and off_ltrs.count() == 0:
                messages.error(request,'no letter available,on search for '+srch)
                return render(request,'app/letters_bucket.html')
            else:
                dict={'appoint_letters':appoint_letters,'termination_letters':termination_letters,'service_letters':service_letters,'intent_ltrs':intent_ltrs,'intern_ltrs':intern_ltrs,'hik_ltrs':hik_ltrs,'offr_ltrs':off_ltrs}
                return render(request,'app/letters_bucket.html',dict)
                
    appoint_letters=Appointment_Letters.objects.all()
    termination_letters=Termination_Letters.objects.all()
    service_letters=Service_letters.objects.all()
    intent_ltrs=Intent_Letters.objects.all()
    intern_ltrs=Intenship_certificates.objects.all()
    hik_ltrs=Hike_letters.objects.all()
    off_ltrs=Offer_Letters.objects.all()
    dict={'appoint_letters':appoint_letters,'termination_letters':termination_letters,'service_letters':service_letters,'intent_ltrs':intent_ltrs,'intern_ltrs':intern_ltrs,'hik_ltrs':hik_ltrs,'offr_ltrs':off_ltrs}
    return render(request,'app/letters_bucket.html',dict)


@login_required(login_url='main')
def new_appoint_letter(request):
    dt=datetime.today()
    if request.method=="POST":
        header=request.POST['header']
        naMe=request.POST['fullname']

        roLe=request.POST['role']
        date=request.POST['date']
        ctc=request.POST['ctc']
        jOin_date=request.POST.get('join_date')

        report=request.POST['reports_to']
        notic_priod=request.POST.get('notice_period')
        if date!='':
            x=list(map(int,date.split('-')))
            y=datetime(x[0],x[1],x[2])
            z=y.strftime('%b %d,%Y')
            ref=datetime.now().strftime('%Y/%d/%m/%H%M')
        else:
            y=''
            z=''
            ref=''
        try:
            f=read_num_in_Indian_format(int(ctc))
        except:
            f=0
        #doc=MailMerge('media/doc_appointment.docx')
        #print(ref)
        
        if date!='':
            x=list(map(int,date.split('-')))
            y=datetime(x[0],x[1],x[2])
            date=y.strftime('%Y-%m-%d')
            
            employee=employees.objects.create(name=naMe,role=roLe,join_date=jOin_date,appointmentletter_issued_on=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),notice_period=notic_priod,annual_package=ctc)
            paTh="media/appointment_letters/"+str(employee.id)+"_appointment.pdf"
            #print('working')
            #print('working 2')
            #store_file
            #print('working 4')
            ##print(f)
            record=records.objects.create(user=request.user.username,record='issued new appointment letter for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            #print('5')
            download_record=download_records.objects.create(user=request.user.username,downloads='issued new appointment letter for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            #print('6')
            messages.info(request,'user details saved in database')
            apt_generator(
                    header=header,
                    date=z,
                    name=naMe,
                    role=roLe,
                    ref_date=ref,
                    ctc_in_words=f,
                    annual_ctc=num2Indian_num_sys(ctc),
                    reports_to=report,
                    notice_period=read_num_in_Indian_format(int(notic_priod)),
                    path=paTh,
                    join_date=jOin_date
                    )
            Appointment_Letters.objects.create(employee=employee,path=paTh)
        return redirect('preview_apt/'+str(employee.id))
        #return render(request,'app/test_without_ajax.html',{'download_link':paTh})
    else:
        return render(request,'app/new_employeee_apt_creation.html',{'dt':dt})

@login_required(login_url='main')
def preview_apt(request,pk):
    emp=employees.objects.get(id=pk)
    apt=Appointment_Letters.objects.get(employee=emp)
    dwnld_path=apt.path
    mail_link='/send_apt/'+str(apt.id)
    #+str(apt.id)
    return render(request,'app/preview.html',{'dwnld_path':dwnld_path,'id':'downloaddoc/'+str(pk),'mail_link':mail_link})

@login_required(login_url='main')
def preview_int_ltr(request,pk):
    emp=employees.objects.get(id=pk)
    int_ltr=Intent_Letters.objects.get(employee=emp)
    dwnld_path=int_ltr.path
    #print(int_ltr.id)
    #print(f)
    mail_link='/send_intL/'+str(int_ltr.id)
    return render(request,'app/preview.html',{'dwnld_path':dwnld_path,'edit_path':f'letter_of_intent_creation/{pk}','mail_link':mail_link})


@login_required(login_url='main')
def issue_letter_of_intent(request,pk):
    if pk=='0':
        x=0
        if request.method=='POST':
            naMe=request.POST['name']
            date=request.POST['date']
            join_date='234'
            Present_role=request.POST['present_role']
            Temporary_role =request.POST['temporary_role']
            appointed_aS=request.POST['appointed_as']
            cTc=request.POST['ctc']
            x=list(map(int,date.split('-')))
            y=datetime(x[0],x[1],x[2])
            date=y.strftime('%Y-%m-%d')
            #doc=MailMerge('media/letter_intent.docx')
            record=records.objects.create (user=request.user.username,record='issued letter of intenr for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            download_record=download_records.objects.create(user=request.user.username,downloads='issued letter of intenr for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            emply=employees.objects.create(name=naMe,temporary_role=Temporary_role,role=appointed_aS,annual_package=cTc,join_date=date,letter_of_intent_issued_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            paTH='media/Intent_letters/'+str(emply.id)+'letter_of_intent.pdf'
            Intnt_ltr=Intent_Letters.objects.create(employee=emply,path=paTH)
            Intnt_ltr.save()
            #strftime('%d-%b,%Y'),
            intent_letter_generator(
            date=y.strftime('%d-%b,%Y'),
            name=naMe,
            role_offered=Present_role,
            temporary_Role=Temporary_role,
            appointed_as=appointed_aS,
            annual_Ctc=num2Indian_num_sys(cTc),
            path=paTH
            )
            
            return redirect('/preview_int_ltr/'+str(emply.id))
            #return render(request,'app/tst_intnt_without_ajax.html',{'emply':emply,'x':x,'download_link':paTH})
        else:
            return render(request,'app/new_employee_intent_letter_creation.html')
    else:
        emply=employees.objects.get(id=pk)
        x=emply.id
        paTH='media/Intent_letters/'+str(emply.id)+'letter_of_intent.pdf'
        if request.method=="POST":
            emply=employees.objects.get(id=pk)
            naMe=request.POST['name']
            date=request.POST['date']
            Present_role=request.POST['present_role']
            Temporary_role =request.POST['temporary_role']
            appointed_aS=request.POST['appointed_as']
            cTc=request.POST['ctc']
            x=list(map(int,date.split('-')))
            y=datetime(x[0],x[1],x[2])
            date=y.strftime('%Y-%m-%d')
            #doc=MailMerge('media/letter_intent.docx')

            paTH='media/Intent_letters/'+str(emply.id)+'letter_of_intent.pdf'
            intent_letter_generator(
            date=y.strftime('%d-%b,%Y'),
            name=naMe,
            role_offered=Present_role,
            temporary_Role=Temporary_role,
            appointed_as=appointed_aS,
            annual_Ctc=num2Indian_num_sys(cTc),
            path=paTH
            )
            emply.letter_of_intent_issued_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            emply.save()
            try:
                int_ltr=Intent_Letters.objects.get(employee=emply)
            except:
                int_ltr=Intent_Letters.objects.create(employee=emply,path=paTH)
                int_ltr.save()
            record=records.objects.create (user=request.user.username,record='issued letter of intenr for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            download_record=download_records.objects.create(user=request.user.username,downloads='issued letter of intenr for '+naMe+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
        return render(request,'app/issue_letter_of_intent.html',{'emply':emply,'x':x,'download_link':paTH})

@login_required(login_url='main')  
def preview_servc_agreement(request,pk):
    emp=employees.objects.get(id=pk)
    srv_agmnt=Service_letters.objects.get(employee=emp)
    dwnld_path=srv_agmnt.path
    #print(f)
    mail_link='/send_srv_agmnt/'+str(srv_agmnt.id)
    return render(request,'app/preview.html',{'f':dwnld_path,'edit_path':f'service_agreement_creation/{pk}','mail_link':mail_link})
 
@login_required(login_url='main')
def issue_new_service_agreement(request,pk):
    if pk!='0':
        emply=employees.objects.get(id=pk)
        x=emply.id
        paTH='media/service_agreements/'+str(emply.id)+'service_agreement.pdf'
        if request.method=='POST':

            namE=request.POST['name']
            Penautly=request.POST['penaulty']
            employee_Duration=request.POST['employee_duration']
            traniNg_period=request.POST['traning_period']
            #doc=MailMerge('media/service_agreement.docx')
            ##print(doc.get_merge_fields())
            service_agreement_generator(
            employee_duration=str(employee_Duration),
                employee_duration_in_words=num2words(str(employee_Duration)),
                penaulty_amount=num2Indian_num_sys(Penautly),
                penaulty_in_words=read_num_in_Indian_format(Penautly),
                training_duration=str(traniNg_period),
                path=paTH
                    )
            record=records.objects.create (user=request.user.username,record='issued service aggrement for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            paTH='media/service_agreements/'+str(emply.id)+'service_agreement.pdf'
            download_record=download_records.objects.create(user=request.user.username,downloads='issued service aggrement for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            emply.name=namE
            emply.traning_period=traniNg_period
            emply.penaulty=Penautly
            emply.service_agreement_issued_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            emply.join_date=datetime.today().strftime('%Y-%m-%d',)
            emply.save()
            try:
                servc=Service_letters.objects.get(employee=emply)
            except:
                servc=Service_letters.objects.create(employee=emply,path=paTH)
                servc.save()
            return render(request,'app/issue_service_agreement.html',{'emply':emply,'x':x,'download_link':paTH})

        else:
            return render(request,'app/issue_service_agreement.html',{'emply':emply,'x':x,'download_link':paTH})
    else:
        emply=None
        x=0
        #issuing to new employee
        if request.method=='POST':
            namE=request.POST['name']
            Penautly=request.POST['penaulty']
            employee_Duration=request.POST['employee_duration']
            traniNg_period=request.POST['traning_period']
            #doc=MailMerge('media/service_agreement.docx')
            ##print(doc.get_merge_fields())
            
            record=records.objects.create (user=request.user.username,record='issued service aggrement for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            download_record=download_records.objects.create(user=request.user.username,downloads='issued service aggrement for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            emply=employees.objects.create(name=namE,traning_period=traniNg_period,penaulty=Penautly,service_agreement_issued_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),join_date=datetime.today().strftime('%Y-%m-%d',))
            emply.save()
            paTH='media/service_agreements/'+str(emply.id)+'service_agreement.pdf'
            service_agreement_generator(
                employee_duration=str(employee_Duration),
                employee_duration_in_words=num2words(str(employee_Duration)),
                penaulty_amount=num2Indian_num_sys(Penautly),
                penaulty_in_words=read_num_in_Indian_format(Penautly),
                training_duration=str(traniNg_period),
                path=paTH
                    )
            srvc=Service_letters.objects.create(employee=emply,path=paTH)
            srvc.save()
            return redirect('/preview_servc_agreement/'+str(emply.id))
        else:
            return render(request,'app/new_srvc_agmnt_crtn.html')

@login_required(login_url='main')    
def internship_certificate_creation(request,pk):
    dt=datetime.today()
    x=pk
    if x=='0':
        if request.method=='POST':
            header=request.POST['header']
            namE=request.POST['name']
            daTe=request.POST['date']
            roLe=request.POST['role']
            eNd_date=request.POST['end_date']
            start_datE=request.POST['start_date']
            #intern creation
            intrn=Interns.objects.create(name=namE,role=roLe,joinied_date=start_datE,leaving_date=eNd_date,internship_letter_issue_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            intrn.save()

            paTh='media/internship_certificates/'+str(intrn.id)+'_internship_certificate.pdf'

            intrn_certifict=Intenship_certificates.objects.create(intern=intrn,path=paTh)
            intrn_certifict.save()

            issue_internship_certificate(
            name=header+'. '+namE,
            id=intrn.id,
            role=roLe,
            date=daTe,
            end_date=eNd_date,
            start_date=start_datE,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            path=paTh
            )

            record=records.objects.create (user=request.user.username,record='created Internship certicate for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()

            download_record=download_records.objects.create(user=request.user.username,downloads='created Internship certicate for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()

            return redirect('/view_intrn_certificate/'+str(intrn.id))
        else:
            return render(request,'app/internship_certificate_creation.html',{'dt':dt})
    elif x!='0':
        intrn=Interns.objects.get(id=pk)
        if request.method=='POST':
            header=request.POST['header']
            namE=request.POST['name']
            daTe=request.POST['date']
            roLe=request.POST['role']
            eNd_date=request.POST['end_date']
            start_datE=request.POST['start_date']
            #updation of existing data..
            intrn.name=namE
            intrn.role=roLe
            intrn.joinied_date=start_datE
            intrn.leaving_date=eNd_date
            intrn.internship_letter_issue_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            intrn.save()
            
            paTh='media/internship_certificates/'+str(intrn.id)+'_internship_certificate.pdf'

            issue_internship_certificate(
            name=header+'. '+namE,
            id=intrn.id,
            role=roLe,
            date=daTe,
            end_date=eNd_date,
            start_date=start_datE,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            path=paTh
            )

            record=records.objects.create (user=request.user.username,record='created Internship certicate for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()

            download_record=download_records.objects.create(user=request.user.username,downloads='created Internship certicate for '+namE+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            
            return redirect('/view_intrn_certificate/'+str(intrn.id))
        else:
            return render(request,'app/internship_certificate_creation.html',{'intern':intrn,'dt':dt})

@login_required(login_url='main')
def view_intern_certificate(request,pk):

    intrn=Interns.objects.get(id=pk)
    certfict=Intenship_certificates.objects.get(intern=intrn)
    dwnld_path=certfict.path
    mail_link='/send_Iltr/'+str(certfict.id)
    return render(request,'app/preview.html',{'dwnld_path':dwnld_path,'edit_path':f'intrn_crtificate_crtn/{pk}','mail_link':mail_link})

def view_hik(request,pk):
    hik=Employees_hike.objects.get(id=pk)
    dwnld_path=hik.path
    edit_path=f'hike_edit/{hik.id}'
    
    mail_link=mail_link='/send_hik_ltr/'+str(hik.id)
    return render(request,'app/preview.html',{'dwnld_path':dwnld_path,'edit_path':edit_path,'mail_link':mail_link})

@login_required(login_url='main')
def hike_edit(request,pk):

    emp_hik=Employees_hike.objects.get(id=pk)
    t=emp_hik.id

    if request.method=='POST':
        header=request.POST['header']
        worth=request.POST['hike_worth']
        date=request.POST['date']
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        start_date=list(map(int,start_date.split('-')))
        end_date=list(map(int,end_date.split('-')))
        sTart_date=datetime(start_date[0],start_date[1],1).strftime('%b %Y')
        eNd_date=datetime(end_date[0],end_date[1],1).strftime('%b %Y')
        start_date=datetime(start_date[0],start_date[1],1).strftime('%Y-%m-01')
        end_date=datetime(end_date[0],end_date[1],1).strftime('%Y-%m-01')

        #print(start_date)
        x=map(int,date.split('-'))
        x=list(x)
        date=datetime(x[0],x[1],x[2])
        #print('test',date)
        var=date
        #doc=MailMerge('media/increment_doc.docx')

        hike_generator(
            daTe=date.strftime('%b %d,%Y'),
            increment_effective_date=date.strftime('%b %d,%Y'),
            header=header,
            name=emp_hik.employee.name,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            increment_in_words=read_num_in_Indian_format(int(worth)),
            duration=sTart_date+'-'+eNd_date,
            path=emp_hik.path
        )
        #doc.write(paTh)

        hk=Hike_letters.objects.get(path=emp_hik.path)
        
        emp_hik.hike=worth
        emp_hik.hike_duration_start_year=start_date
        emp_hik.hike_duration_end_year=end_date
        emp_hik.save()

        hk.created=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hk.save()
        """emp_hike=Employees_hike.objects.create(employee=hik.employee,hike=worth,hike_duration_start_year=start_date,hike_duration_end_year=end_date)
        emp_hike.hike_letter_issued_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        emp_hike.save()"""

        emp_hik.employee.annual_package+=int(worth)
        emp_hik.employee.save()

        record=records.objects.create(user=request.user.username,record='issued hike letter for '+hk.employee.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        record.save()

        download_record=download_records.objects.create(user=request.user.username,downloads='issued hike letter for '+hk.employee.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        download_record.save()
        messages.info(request,'hike isssued successfully')
        return  redirect('/view_hik/'+str(t))
    return render(request,'app/emloyee_hike_issue.html',{'employee':emp_hik.employee})

@login_required(login_url='main')
def offer_ltr_generator(request,pk):
    dt=datetime.today()
    #print('entered')
    if pk=='0':
        #print('post entered')
        if request.method=='POST':
            nAme=request.POST['name']
            header=request.POST['header']
            roLE=request.POST['role']
            hrA=request.POST['hra']
            variable_Pay_t=request.POST['variable_pay_type']
            v_pay=request.POST['variable_pay']
            lta=request.POST['lta']
            spl=request.POST['spl_allowance']
            Basic=request.POST['basic']
            cTc=(int(hrA)+int(v_pay)+int(spl)+int(lta)+int(Basic))
            daTe=request.POST['date']
           
            emp=employees.objects.create(name=nAme,role=roLE,annual_package=cTc,offer_letter_issued_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            emp.save()
            paTh=f'media/offer_letters/{emp.id}offerletter.pdf'

            offer_lt=Offer_Letters.objects.create(employee=emp,path=paTh)
            offer_lt.save()
            x=map(int,daTe.split('-'))
            x=list(x)
            daTe=datetime(x[0],x[1],x[2]).strftime('%b %d,%Y')

            validity=datetime.strptime(daTe,'%b %d,%Y')

            validity= validity + DT.timedelta(days=14)

            Offer_letter_generator(
            name=nAme,
            header=header,
            role=roLE,
            ctc=num2Indian_num_sys(cTc),
            hra=int(hrA),
            validity_date=validity.strftime('%b %d,%Y'),
            date=daTe,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            basic=int(Basic)
            ,variable_pay=variable_Pay_t
            ,varibale_pay_amt=int(v_pay)
            ,special_allowance=int(spl)
            ,lta=int(lta)
            ,path=paTh
            )
            messages.success(request,'letter created')
            record=records.objects.create(user=request.user.username,record='downloaded offer letter for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            download_record=download_records.objects.create(user=request.user.username,downloads='downloaded offer letter for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            return redirect('/view_offer_ltr/'+str(offer_lt.id))
           
        else:
            return render(request,'app/offer_letter_creation.html',{'dt':dt})
    elif pk!='0':
        emp=employees.objects.get(id=pk)
        if request.method=='POST':
            nAme=request.POST['name']
            header=request.POST['header']
            #cTc=request.POST['ctc']
            roLE=request.POST['role']
            hrA=request.POST['hra']
            variable_Pay_t=request.POST['variable_pay_type']
            v_pay=request.POST['variable_pay']
            lta=request.POST['lta']
            spl=request.POST['spl_allowance']
            daTe=request.POST['date']
            Basic=request.POST['basic']
            (cTc)=(int(hrA)+int(v_pay)+int(spl)+int(lta)+int(Basic))
            
            paTh=f'media/offer_letters/{emp.id}offerletter.pdf'
            
            x=map(int,daTe.split('-'))
            x=list(x)
            daTe=datetime(x[0],x[1],x[2]).strftime('%b %d,%Y')
            validity=datetime.strptime(daTe,'%b %d,%Y')
            validity= validity + DT.timedelta(days=14)

            emp.role=roLE
            emp.annual_package=cTc
            emp.offer_letter_issued_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            emp.save()

            Offer_letter_generator(
            header=header,
            name=nAme,
            role=roLE,
            ctc=num2Indian_num_sys(cTc),
            hra=int(hrA),
            validity_date=validity.strftime('%b %d,%Y'),
            date=daTe,
            ref_date=datetime.now().strftime('%Y/%d/%m/%H%M'),
            basic=int(Basic)
            ,variable_pay=variable_Pay_t
            ,varibale_pay_amt=int(v_pay)
            ,special_allowance=int(spl)
            ,lta=int(lta)
            ,path=paTh
            )
            try:
                offer_lt=Offer_Letters.objects.get(employee=emp,path=paTh)
            except:
                offer_lt=Offer_Letters.objects.create(employee=emp,path=paTh)
                offer_lt.save()
            record=records.objects.create(user=request.user.username,record='downloaded offer letter for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            download_record=download_records.objects.create(user=request.user.username,downloads='downloaded offer letter for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            download_record.save()
            messages.success(request,'letter created')
            return redirect('/view_offer_ltr/'+str(offer_lt.id))
        
        else:
            return render(request,'app/offer_letter_creation.html',{'emp':emp,'dt':dt})

@login_required(login_url='main')
def view_offer_ltr(request,pk):
    off_ltr=Offer_Letters.objects.get(id=pk)
    dwnld_path=off_ltr.path
    #print(f)
    mail_link='/send_offer_ltr/'+str(off_ltr.id)
    return render(request,'app/preview.html',{'dwnld_path':dwnld_path,'edit_path':f'offer_ltr/{off_ltr.employee.id}','mail_link':mail_link})

# below 7 functions, are used to send mail to the emmployees,with an attachment to generated pdfs
@login_required(login_url='main')
def send_apt_pdf_mail_on_pdf(request,pk):
    apt_ltr=Appointment_Letters.objects.get(id=pk)
    if request.method =='POST':
        maIl=request.POST['mail']
        x=apt_ltr.employee.id
        #print(x)
        emp=employees.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST   
        msg=EmailMessage('appointment letter', 'appointment letter from FNC',sender,[maIl] )
        msg.attach_file(apt_ltr.path)
        try:
            msg.send()
            messages.success(request,'email sent')
            record=records.objects.create(user=request.user.username,record='sent the appointment created,on his mail for '+emp.name+' at ',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            return redirect(f'/preview_apt/{apt_ltr.employee.id}')
        except:
            messages.info(request,'mail not sent,inavlid recipient address')
    return render(request,'app/send_mail.html',{'emp':apt_ltr.employee.email})

@login_required(login_url='main')

def send_ltr_int(request,pk):
    intL=Intent_Letters.objects.get(id=pk)
    if request.method =='POST':
        maIl=request.POST['mail']
        x=intL.employee.id
        #print(x)
        emp=employees.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST_USER   
        msg=EmailMessage('Intent letter','letter of intent from FNC ',sender,[maIl] )
        msg.attach_file(intL.path)
        try:
            msg.send()
            messages.info(request,'"email sent"')
            record=records.objects.create(user=request.user.username,record='sent appointmenr letter created,to his mail for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            return redirect(f'/preview_int_ltr/{intL.employee.id}')
        except:
            messages.info(request,'email not sent,invalid recipient address')
    return render(request,'app/send_mail.html',{'emp':intL.employee.email})

@login_required(login_url='main')
def send_trm_ltr(request,pk):
    trm=Termination_Letters.objects.get(id=pk)
    if request.method =='POST':
        maIl=request.POST['mail']
        x=trm.employee.id
        #print(x)
        emp=employees.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST_USER   
        msg=EmailMessage('Termination letter','termination letter from FNC',sender,[maIl] )
        msg.attach_file(trm.path)
        try:
            msg.send()
            messages.info(request,'email sent')
            record=records.objects.create(user=request.user.username,record='sent letter of service or termination created,to his mail for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            return redirect (f'/view_trm/{trm.employee.id}')
        except:
            messages.info(request,'email not sent,invalid recipient address')
    return render(request,'app/send_mail.html',{'emp':trm.employee.email})

@login_required(login_url='main')
def send_srv_agmnt(request,pk):
    srv=Service_letters.objects.get(id=pk)
    if request.method =='POST':
        maIl=request.POST['mail']
        x=srv.employee.id
        #print(x)
        emp=employees.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST_USER   
        msg=EmailMessage('service agreement',' service agreement from FNC',sender,[maIl] )
        msg.attach_file(srv.path)
        try:
            msg.send()
            messages.info(request,'email sent')
            record=records.objects.create(user=request.user.username,record='sent service agreement created,to his mail for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            return redirect(f'/preview_servc_agreement/{srv.employee.id}')
        except:
            messages.info(request,'email not sent,invalid recipient address')
    return render(request,'app/send_mail.html',{'emp':srv.employee.email})

@login_required(login_url='main')
def send_offer_ltr(request,pk):
    offl=Offer_Letters.objects.get(id=pk)

    if request.method =='POST':
        maIl=request.POST['mail']
        x=offl.employee.id
        #print(x)
        emp=employees.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST_USER   
        msg=EmailMessage('Offer letter','offer letter from FNC',sender,[maIl] )
        msg.attach_file(offl.path)
        try:
            msg.send()
            messages.info(request,'email sent')
            record=records.objects.create(user=request.user.username,record='sent offer letter created,to his mail for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            return redirect(f'/view_offer_ltr/{offl.id}')
        except:
            messages.info(request,'email not sent,invalid recipient address')
    return render(request,'app/send_mail.html',{'emp':offl.employee.email})

@login_required(login_url='main')
def send_hik_ltr(request,pk):
    hik=Employees_hike.objects.get(id=pk)
    if request.method =='POST':
        maIl=request.POST['mail']
        x=hik.employee.id
        #print(x)
        emp=employees.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST_USER   
        msg=EmailMessage('Hike letter','Hike letter from FNC',sender,[maIl] )
        msg.attach_file(hik.path)
        try:
            msg.send()
            messages.info(request,'email sent')
            record=records.objects.create(user=request.user.username,record='sent hike letter created,to his mail for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
        except:
            messages.info(request,'email not sent,invalid recipient address')
    return render(request,'app/send_mail.html',{'emp':hik.employee.email})

@login_required(login_url='main')
def send_internship_ltr(request,pk):

    intrn=Intenship_certificates.objects.get(id=pk)
    if request.method =='POST':
        maIl=request.POST['mail']
        x=intrn.intern.id
        emp=Interns.objects.get(id=x)
        emp.email=maIl
        emp.save()
        sender=settings.EMAIL_HOST_USER   
        msg=EmailMessage('Internship certificate','Internship certificate from FNC',sender,[maIl] )
        msg.attach_file(intrn.path)
        try:
            msg.send()
            messages.info(request,'email sent')
            record=records.objects.create(user=request.user.username,record='sent Internship letter created,to his mail for '+emp.name+' at',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            record.save()
            return redirect(f'/view_intrn_certificate/{intrn.intern.id}')
        except:
            messages.info(request,'email not sent,invalid recipient address')
    return render(request,'app/send_mail.html',{'emp':intrn.intern.email})


@login_required(login_url='main')
def preview_trm(request,pk):

    emp=employees.objects.get(id=pk)
    trm_ltr=Termination_Letters.objects.get(employee=emp)
    dwnld_path=trm_ltr.path
    ##print(itrm_r.id)
    #print(f)
    st=[]

    mail_link='/send_trm_ltr/'+str(trm_ltr.id)

    return render(request,'app/preview.html',{'st':st,'dwnld_path':dwnld_path,'edit_path':f'termination/{pk}','mail_link':mail_link})

#here view_letter_name or preview_ltr_name are used to handle preview page which provides download,preview functionallities
 
"""here except for apt ltr,to handle letter ceration for  new employee and letter creation for existing,i used  pk,for handling ltr creation for
new employee i used pk as as pk will never be zero"""

#testing sidebar template

def template_test(request):
    return render(request,'app/test_templates.html')