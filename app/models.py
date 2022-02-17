from django.db import models

# Create your models here.

class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(max_length=240, null=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240,null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.EmailField(max_length=240, null=True)
    idproof = models.FileField(upload_to='', default='')
    photo = models.FileField(upload_to='', default='')
    designation = models.CharField(max_length=240, null=True,default='')
    department = models.CharField(max_length=240, null=True,default='')
    branch = models.CharField(max_length=240, null=True,default='')
    team = models.CharField(max_length=240, null=True,default='')
    attitude = models.PositiveIntegerField(default='')
    creativity = models.PositiveIntegerField(default='')
    workperformance = models.PositiveIntegerField(default='')
    joiningdate =  models.DateField(max_length=240, null=True,default='')
    startdate =  models.DateField(max_length=240, null=True,default='')
    enddate =  models.DateField(max_length=240, null=True,default='')
    status =  models.CharField(max_length=240, null=True,default='')

    
    def __str__(self):
        return self.fullname

class extracurricular(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='extracurricularuser')
    internshipdetails = models.CharField(max_length=240,null=True)
    internshipduration = models.CharField(max_length=240,null=True)
    internshipcertificate = models.FileField(upload_to='', default='')
    onlinetrainingdetails = models.CharField(max_length=240,null=True)
    onlinetrainingduration = models.CharField(max_length=240,null=True)
    onlinetrainingcertificate= models.FileField(upload_to='', default='')
    projecttitle = models.CharField(max_length=240,null=True)
    projectduration = models.CharField(max_length=240,null=True)
    projectdescription = models.TextField(null=True)
    projecturl = models.CharField(max_length=240, default='',null=True,blank=True)
    skill1 = models.CharField(max_length=240, default='',null=True,blank=True)
    skill2 = models.CharField(max_length=240, default='',null=True,blank=True)
    skill3 = models.CharField(max_length=240, default='',null=True,blank=True)
    status = models.CharField(max_length=240,default='')
    
    
    def __str__(self):
        return self.projecttitle


class qualification(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='qualificationuser')
    plustwo = models.CharField(max_length=240,null=True)
    schoolaggregate = models.CharField(max_length=240,null=True)
    schoolcertificate = models.FileField(upload_to='', default='')
    ugdegree = models.CharField(max_length=240,null=True)
    ugstream = models.CharField(max_length=240,null=True)
    ugpassoutyr = models.CharField(max_length=240,null=True)
    ugaggregrate = models.CharField(max_length=240,null=True)
    backlogs= models.CharField(max_length=240,null=True)
    ugcertificate = models.FileField(upload_to='', default='')
    pg= models.CharField(max_length=240,null=True)
    status = models.CharField(max_length=100,default='')


    def __str__(self):
        return self.user


class branch_registration(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    branch_admin=models.CharField(max_length=100)
    branch_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.branch_name


class designation(models.Model):
    branch =models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='designationbranch')
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.designation


class department(models.Model):
    department=models.CharField(max_length=100)
    branch =models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING , related_name='departmentbranch')
    status=models.CharField(max_length=100)


    def __str__(self):
        return self.department

class project(models.Model):
    branch = models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='projectbranch')
    department =models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='projectdepartment')
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='projectuser')
    project = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    startdate=models.DateField(max_length=100)
    enddate=models.DateField(max_length=100)
    files=models.FileField(upload_to='', default='')
    status=models.CharField(max_length=100)
    

    def __str__(self):
        return self.project



class test_status(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='test_statususer')
    project = models.ForeignKey(project, on_delete=models.DO_NOTHING, related_name='test_statusproject')
    taskname = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='test_statustaskname')
    date=models.DateField(max_length=100)
    workdone = models.TextField()
    files=models.FileField(upload_to='', default='')


    def __str__(self):
        return self.project


class project_taskassign(models.Model):
    project = models.ForeignKey(project, on_delete=models.DO_NOTHING, related_name='project_taskassignproject')
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='project_taskassignuser')
    tl = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='project_taskassigntl')
    task = models.CharField(max_length=240)
    description = models.TextField()
    startdate=models.DateField(max_length=100)
    enddate=models.DateField(max_length=100)
    files=models.FileField(upload_to='', default='')
    department = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    employee = models.CharField(max_length=200)
    tester = models.CharField(max_length=200)
    extension = models.IntegerField()
    reason = models.TextField()
    extension_status = models.CharField(max_length=200)
    tl_description = models.CharField(max_length=200)
    submitted_date=models.DateField(max_length=100)
    employee_files = models.FileField(upload_to='', default='')
    employee_description = models.TextField()
    status = models.CharField(max_length=200)


    def __str__(self):
        return self.project


class tester_status(models.Model):
    tester = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='tester_statustester')
    project =models.ForeignKey(project, on_delete=models.DO_NOTHING, related_name='tester_statusproject')
    task = models.ForeignKey(project_taskassign, on_delete=models.DO_NOTHING, related_name='tester_statustask')
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='tester_statususer')
    date=models.DateField(max_length=100)
    workdone = models.TextField()
    files=models.FileField(upload_to='', default='')
    subtask = models.TextField()
    progress = models.IntegerField()
    status = models.CharField(max_length=200)


    def __str__(self):
        return self.project


class reported_issue(models.Model):
    reporter = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='reported_issuereporter')
    reported_to = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='reported_issuereported_to')
    issue = models.TextField()
    reported_date = models.DateField(max_length=100)
    reply = models.TextField()
    status = models.CharField(max_length=200)


    def __str__(self):
        return self.reporter

    
class attendance(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='attendanceuser')
    date=models.DateField(max_length=100)
    status = models.CharField(max_length=200)


    def __str__(self):
        return self.user


class leave(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='leaveuser')
    from_date =models.DateField(max_length=100)
    to_date = models.DateField(max_length=100)
    reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


    def __str__(self):
        return self.user


class internship(models.Model):
    reg_date = models.DateField(max_length=200)
    fullname = models.CharField(max_length=200) 
    collegename = models.CharField(max_length=200) 
    reg_no = models.CharField(max_length=200) 
    course = models.CharField(max_length=200) 
    stream = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    alternative_no = models.CharField(max_length=200)
    email = models.EmailField()
    profile_pic= models.ImageField(upload_to='' ,null=True)
    attach_file= models.FileField(default="")  
    rating = models.CharField(max_length=200)  
    hrmanager = models.CharField(max_length=200)
    guide = models.CharField(max_length=200)
    qr = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=200)


    def __str__(self):
        return self.fullname


class create_team(models.Model):
    name = models.CharField(max_length=200) 
    trainer = models.CharField(max_length=200) 
    progress =  models.IntegerField() 
    status =  models.CharField(max_length=200)  


    def __str__(self):
        return self.name


class trainer_task(models.Model):
    trainee = models.CharField(max_length=240)
    trainer = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='trainer_tasktrainer')
    taskname =  models.CharField(max_length=240)
    startdate=models.DateField(max_length=100)
    enddate=models.DateField(max_length=100)
    files=models.FileField(upload_to='', default='')
    description = models.TextField()
    trainee_description = models.TextField()
    trainee_files = models.FileField(upload_to='', default='')
    status =  models.CharField(max_length=200)  


    def __str__(self):
        return self.trainee


class topic(models.Model):
    trainer = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='topictrainer')
    team = models.ForeignKey(create_team, on_delete=models.DO_NOTHING, related_name='topicteam')
    topic = models.CharField(max_length=240)
    startdate=models.DateField(max_length=100)
    enddate=models.DateField(max_length=100)
    files=models.FileField(upload_to='', default='')
    description = models.TextField()
    review = models.TextField()
    status =  models.CharField(max_length=200)


    def __str__(self):
        return self.topic






