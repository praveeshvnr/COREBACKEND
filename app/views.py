from django.http import request
from django.shortcuts import render
from .models import *
from datetime import datetime

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            dev = user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
           
            request.session['devfn'] = dev.fullname
            request.session['devid'] = dev.id
            
            return render(request, 'DEVsec.html', {'dev': dev})
        else:
            context = {'msg': 'Invalid uname or password'}
            return render(request, 'login.html', context)


def devindex(request):
    return render(request,'devindex.html')

def devdashboard(request):
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

def devReportedissues(request):
        
        return render(request,'devReportedissues.html')

def devreportissue(request):
        
        return render(request,'devreportissue.html')

def devreportedissue(request):
    
    if request.session.has_key('devdes'):
        devdes = request.session['devdes']
    if request.session.has_key('devdep'):
        devdep = request.session['devdep']
    if request.session.has_key('devfn'):
        devfn = request.session['devfn']
    else:
        variable = "dummy"
    var=reported_issue.objects.all()
    vars=user_registration.objects.filter(fullname=devfn)
    
    return render(request,'devreportedissue.html',{'var':var,'vars':vars})

# def devsuccess(request):
    
            
#     if request.method == 'POST':
       
#         issue=request.POST.get("reportissue")
#         vars=reported_issue(issue=issue)
#         vars.save()
#     return render(request,'devsuccess.html')

# def devsuccess(request):
#     # if request.session.has_key('devfn'):
#     #     devfn = request.session['devfn']
#     # if request.session.has_key('devid'):
#     #     devid = request.session['devid']
#     # else:
#     #     variable = "dummy"
#     if request.method == 'POST':
#         issue = request.POST.get("reportissue")
#         vars = reported_issue(issue=issue)
#         vars.save()
#     return render(request, 'devsuccess.html')

def devsuccess(request):
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

# def devissues(request):
     
#     if request.session.has_key('devid'):
#         devid = request.session['devid']
#     if request.session.has_key('devfn'):
#         devfn = request.session['devfn']
#     if request.session.has_key('repid'):
#         repid = request.session['repid']
#     else:
#         variable = "dummy"
    
#     vars=user_registration.objects.filter(fullname=devfn)
#     var=reported_issue.objects.filter( reported_to=devid)
#     return render(request,'devissues.html',{'vars':vars,'var':var})
def devissues(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    rid=request.GET.get('rid')
    var=reported_issue.objects.filter(id=rid)
    mem = user_registration.objects.filter(id=devid)

    return render(request, 'devissues.html',{'mem':mem,'var':var})




def devsample(request):
    return render(request,'devsample.html')


#*********************praveesh*********************


def Devapplyleav(request):
    return render(request,'Devapplyleav.html')
def Devapplyleav1(request):
    return render(request,'Devapplyleav1.html')
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
    return render(request, 'promanagerindex.html')

def pmanager_dash(request):
    return render(request, 'pmanager_dash.html')

def projectmanager_projects(request):
    return render(request, 'projectmanager_projects.html')

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
    return render(request, 'projectMANreportedissue.html')

def projectMANreportissue(request):
    return render(request, 'projectMANreportissue.html')

def projectmanagerreportedissue2(request):
    return render(request, 'projectmanagerreportedissue2.html')

def MANreportsuccess(request):
    return render(request, 'MANreportsuccess.html')

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
    return render(request, 'projectmanager_tlreported.html')