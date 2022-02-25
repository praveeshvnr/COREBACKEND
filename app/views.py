
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from datetime import datetime

# Create your views here.

def login(request):
    if request.method =='POST':
        
        design=designation.objects.get(designation="TL")
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['tlid'] = member.id
            if request.session.has_key('tlid'):
                tlid = request.session['tlid']
            else:
                variable = "dummy"
            mem = user_registration.objects.filter(id=tlid)
            return render(request, 'TLdashboard.html', {'mem':mem})
        des = designation.objects.get(designation='Developer')
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=des).exists():
            dev = user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['devid'] = dev.id
            if request.session.has_key('devid'):
                devid = request.session['devid']
            else:
                variable = "dummy"
            dev = user_registration.objects.filter(id=devid)
            return render(request, 'devdashboard.html', {'dev': dev})
        design1=designation.objects.get(designation="project manager")
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design1).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['prid'] = member.id
            if request.session.has_key('prid'):
                prid = request.session['prid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=prid)
            return render(request, 'pmanager_dash.html', {'pro':pro})
        else:
            context={'msg':'Invalid uname or password'}
            return render(request,'login.html',context)
    return render(request, 'login.html')


# def home(request):
#     if request.method == 'POST':
#         var=designation.objects.get(designation='developer')
#         if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
#             dev = user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
           
#             request.session['devfn'] = dev.fullname
#             request.session['devid'] = dev.id
#             request.session['desid'] = dev.designation_id
            
#             return render(request, 'DEVsec.html', {'dev': dev})

#         var=designation.objects.get(designation='projectmanager')
#         if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
#             vars = user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
           
#             request.session['pmfn'] = vars.fullname
#             request.session['pmid'] = vars.id
#             request.session['pmsid'] = vars.designation_id
            
#             return render(request, 'PRsec.html', {'vars': vars})
#         else:
#             context = {'msg': 'Invalid uname or password'}
#             return render(request, 'login.html', context)
        


def devindex(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        dev = user_registration.objects.filter(id=devid)
        return render(request,'devindex.html',{'dev':dev})
    else:
        return redirect('/')

def devdashboard(request):
    if 'devid' in request.session:
        if request.session.has_key('devdes'):
            devdes = request.session['devdes']
        if request.session.has_key('devdep'):
            devdep = request.session['devdep']
        if request.session.has_key('devfn'):
            devfn = request.session['devfn']
        else:
            variable = "dummy"
        dev = user_registration.objects.filter(fullname=devfn)
        return render(request,'devdashboard.html', {'dev': dev})
    else:
        return redirect('/')

def devReportedissues(request):
    if 'devid' in request.session:    
        return render(request,'devReportedissues.html')
    else:
        return redirect('/')
def devreportissue(request):
    if 'devid' in request.session:
        
        return render(request,'devreportissue.html')
    else:
        return redirect('/')

def devreportedissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
            variable = "dummy"
        
        var=reported_issue.objects.filter(reporter_id=devid)
        # vars=user_registration.objects.filter(fullname=devfn)
        
        return render(request,'devreportedissue.html',{'var':var})
    else:
        return redirect('/')


def devsuccess(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        
        mem = user_registration.objects.filter(id=devid)
        
        
        
        
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('reportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=1
            vars.reporter_id=devid
            vars.status='pending'
            vars.save()
        return render(request,'devsuccess.html',{'mem':mem})
    else:
        return redirect('/')


def devissues(request,id):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        # mem = user_registration.objects.filter(id=devid)

        return render(request, 'devissues.html',{'var':var})
    else:
        return redirect('/')



def devsample(request):
    if 'devid' in request.session:
        return render(request,'devsample.html')

    else:
        return redirect('/')
#*********************praveesh*********************


def Devapplyleav(request):
    if 'devid' in request.session:
        return render(request,'Devapplyleav.html')
    else:
        return redirect('/')
def Devapplyleav1(request):
    if 'devid' in request.session:
        return render(request,'Devapplyleav1.html')
    else:
        return redirect('/')
def Devapplyleav2(request):
    return render(request,'Devapplyleav2.html')
def Devleaverequiest(request):
    return render(request,'Devleaverequiest.html')
def Devattendance(request):
    return render(request,'Devattendance.html')
def Tattend(request):
    return render(request,'Tattend.html')
def Devapplyleav3(request):
    return render(request,'Devapplyleav3.html')



#**************************maneesh*********************


def DEVprojects(request):
    return render(request,'DEVprojects.html')
def DEVtable(request):
    return render(request,'DEVtable.html')
def DEVtaskmain(request):
    return render(request,'DEVtaskmain.html')   
def DEVtaskform(request):
    return render(request,'DEVtaskform.html')
def DEVtask(request):
    return render(request,'DEVtask.html')
def DEVsuccess(request):
    return render(request,'DEVsuccess.html')



#**************************Rohit**************************


def TSdashboard(request):
    return render(request,'TSdashboard.html')
def TStask(request):
    return render(request,'TStask.html')
def TSproject(request):
    return render(request,'TSproject.html')
def TSprojectdetails(request):
    return render(request,'TSprojectdetails.html')
def TSassigned(request):
    return render(request,'TSassigned.html')
def TSsubmitted(request):
    return render(request,'TSsubmitted.html')
def TSsucess(request):
    return render(request,'TSsucess.html')


#****************************amal*******************


def tldashboard(request):
    if request.session.has_key('usernametl'):
        usernameM1 = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernameM = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernameM2 = request.session['usernametl2']
    else:
        usernameM2 = "dummy"
    mem = user_registration.objects.filter(designation=usernameM1).filter(fullname=usernameM2)
    return render(request, 'TLdashboard.html')
def tlprojects(request):
    return render(request, 'TLprojects.html')
def tlprojecttasks(request):
    return render(request, 'TLprojecttasks.html')
def tlsplittask(request):
    return render(request, 'TLsplittask.html')
def tlgivetask(request):
    return render(request, 'TLgivetask.html')


#**************************abin*************************


def TLattendance(request):
    return render(request, 'TLattendance.html')
def TLreportissues(request):
    return render(request, 'TLreportissues.html')
def TLreportedissue1(request):
    return render(request, 'TLreportedissue1.html')
def TLreportedissue2(request):
    return render(request, 'TLreportedissue2.html')
def TLreport1(request):
    return render(request, 'TLreport1.html')
def TLreportsuccess(request):
    return render(request, 'TLreportsuccess.html')


#***********************bibin*****************************


def TLtasks(request):
    return render(request, 'TLtasks.html')
def TLleave(request):
    return render(request, 'TLleave.html')
def TLleavereq(request):
    return render(request, 'TLleavereq.html')
def TLreqedleave(request):
    return render(request, 'TLreqedleave.html')
def TLgivetasks(request):
    return render(request, 'TLgivetasks.html')
def TLgavetask(request):
    return render(request, 'TLgavetask.html')
def TLsuccess(request):
    return render(request, 'TLsuccess.html')



# project manager module
def promanagerindex(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        dev = user_registration.objects.filter(id=prid)
        return render(request,'promanagerindex.html',{'dev':dev})
        
    else:
        return redirect('/')
def pmanager_dash(request):
    if 'prid' in request.session:
        return render(request, 'pmanager_dash.html')
    else:
        return redirect('/')

def projectmanager_projects(request):
    if 'prid' in request.session:
        return render(request, 'projectmanager_projects.html')
    else:
        return redirect('/')

#nirmal
def projectmanager_assignproject(request):
    return render(request, 'projectmanager_assignproject.html')

#jensin
def projectmanager_createproject(request):
    return render(request, 'projectmanager_createproject.html')

#maneesh
def projectmanager_description(request):
    return render(request, 'projectmanager_description.html')

def projectmanager_table(request):
    return render(request, 'projectmanager_table.html')

def projectmanager_upprojects(request):
    return render(request, 'projectmanager_upprojects.html')

#praveesh

def projectmanager_accepted_projects(request):
    return render(request, 'projectmanager_accepted_projects.html')

def projectmanager_rejected_projects(request):
    return render(request, 'projectmanager_rejected_projects.html')



#bibin #amal #abin #rohit
def manindex(request):
    return render(request, 'manager_index.html')

def projectmanEmp(request):
    return render(request, 'projectman_emp.html')

def projectmanDev(request):
    return render(request, 'projectman_dev.html')

def projectmanDevDashboard(request):
    return render(request, 'projectman_dev_Dashboard.html')

def projectman_developer_attendance(request):
    return render(request, 'projectman_developer_attendance.html')

def projectman_team(request):
    return render(request, 'projectman_team.html')

def projectman_team_profile(request):
    return render(request, 'projectman_team_profile.html')

def projectman_team_attendance(request):
    return render(request,'projectman_team_attendance.html')

def projectMANattendance(request):
    return render(request, 'projectMANattendance.html')

def projectMANreportedissues(request):
    return render(request, 'projectMANreportedissues.html')

def projectMANreportedissue(request):
    if 'prid' in request.session:
        if request.session.has_key('devdes'):
            devdes = request.session['devdes']
        if request.session.has_key('devdep'):
            devdep = request.session['devdep']
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        var=reported_issue.objects.filter(reporter=prid)
    
        return render(request, 'projectMANreportedissue.html',{'var':var})
    else:
        return redirect('/')

def projectMANreportissue(request):
    if 'prid' in request.session:
        return render(request, 'projectMANreportissue.html')
    else:
        return redirect('/')

def projectmanagerreportedissue2(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var})
    else:
        return redirect('/')
def projectmanagerreportedissue3(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var})
    else:
        return redirect('/')


def MANreportsuccess(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        
        mem = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('MANreportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=1
            vars.reporter_id=prid
            vars.status='pending'
            vars.save()
        return render(request, 'MANreportsuccess.html',{'mem':mem})
    else:
        return redirect('/')

def projectMANleave(request):
    return render(request, 'projectMANleave.html')

def projectMANleavereq(request):
    return render(request, 'projectMANleavereq.html')

def projectMANreqedleave(request):
    return render(request, 'projectMANreqedleave.html') 

def Manager_employees(request):
    return render(request,'Manager_employees.html')

def projectManager_tl(request):
    return render(request,'projectManager_tl.html')

def projectManager_tl_dashboard(request):
    return render(request,'projectManager_tl_dashboard.html')

def man_tl_attendance(request):
    return render(request,'man_tl_attendance.html')


def projectmanager_currentproject(request):
    return render(request, 'projectmanager_currentproject.html')

def projectmanager_currentdetail(request):
    return render(request, 'projectmanager_currentdetail.html')

def projectmanager_currentteam(request):
    return render(request, 'projectmanager_currentteam.html')

def projectmanager_completeproject(request):
    return render(request, 'projectmanager_completeproject.html')

def projectmanager_completedetail(request):
    return render(request, 'projectmanager_completedetail.html')

def projectmanager_completeteam(request):
    return render(request, 'projectmanager_completeteam.html')

def projectmanager_teaminvolved(request):
    return render(request, 'projectmanager_teaminvolved.html')

def projectmanager_devteam(request):
    return render(request, 'projectmanager_devteam.html')

def projectmanager_currenttl(request):
    return render(request, 'projectmanager_currenttl.html')

def projectmanager_completetl(request):
    return render(request, 'projectmanager_completetl.html')

def projectmanager_tlreported(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
    
        else:
            variable = "dummy"
        vars=user_registration.objects.filter(designation=2)
        var=reported_issue.objects.filter(reported_to_id=prid)
        # vars=user_registration.objects.filter(designation_id=2).filter(id=devid)
        return render(request, 'projectmanager_tlreported.html',{'var':var,'vars':vars})
    else:
        return redirect('/')


def projectreply(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.save()
        return redirect('projectmanager_tlreported')
    else:
        return redirect('/')


def logout(request):
    if 'devid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
def prlogout(request):
    if 'prid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
    