from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from . models import InternUser,EmployeeUser,Domain,Module,InternAnswer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create index
def index(request):
    return render(request,'index.html')

# Create intern login  signup ilogout
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            try:
                if user.internuser:
                    login(request, user)
                    return redirect('internsdash')
            except InternUser.DoesNotExist:
                messages.error(request, 'please login with Employee signup page.')
        else:
            messages.error(request, 'Invalid credentials')

        
    return render (request,'login.html')
def signup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            print(request.POST)
            #create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                is_active=False
            )
            #creating intern user
            intern=InternUser.objects.create(
                user=user,
                phone=phone,
                email=email,
                name=username

            )
            return redirect('signin')
        except Exception as e:
            error_message="Username is already assigned"
            messages.error(request,error_message)

    return render(request,'signup.html')
def ilogout(request):
    logout(request)
    return redirect('index')
# intern dashboard
@login_required(login_url='signin')
def internsdash(request):
    intern_user = InternUser.objects.get(user=request.user)
    modules = Module.objects.filter(domain=intern_user.domain)
    completed_modules = InternAnswer.objects.filter(intern_user=intern_user).values_list('module_id', flat=True)

    # Calculate the active module index
    no = len(completed_modules)
    

    context = {
        'intern_user':intern_user,
        'modules': modules,
        'completed_modules': completed_modules,
        'no': no,
    }
    print(intern_user)
    return render(request, 'internsdash.html', context)


#submitting answer for each module by internuser
@login_required(login_url='signin')
def answersubmit(request, moduleid):
    module=Module.objects.get(id=moduleid)
    
    if request.method == 'POST':
        answer = request.POST.get('answer')

        if answer:
            intern_user = request.user.internuser
            existing_answer = InternAnswer.objects.filter(intern_user=intern_user, module=module).exists()

            if not existing_answer:
                InternAnswer.objects.create(
                    intern_user=intern_user,
                    module=module,
                    answer_text=answer
                )
                return redirect('internsdash')
            else:
                return HttpResponse("You have already submitted an answer for this module.")
        else:
            return HttpResponse("Answer cannot be empty.")

    context = {'module': module}
    return render(request, 'answersubmit.html', context)

@login_required(login_url='signin')
def ineditprofile(request,id):
    internuser=InternUser.objects.get(id=id)
    print(internuser.phone)
    user=User.objects.get(id=request.user.id)
    print(user.id)
    if request.POST:
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        user.email=email
        internuser.email=email
        internuser.username=name
        internuser.phone=phone
        user.save()
        internuser.save()
        return redirect('internsdash')
    context={
        'internuser':internuser,
        'user':user
    }


    return render(request,'editinternprofile.html',context)



#EMPLOYEE


# Create employee login  signup employee dash  elogout
def esignup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            password=request.POST.get('password')
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                is_active=False
                
            )
            empuser=EmployeeUser.objects.create(
                user=user,
                email=email,
                name=username,
                phone=phone
            )
            return redirect('esignin')
        except Exception as e:
            error_messages="Username not available"
            messages.error(request,error_messages)

    return render(request,'esignup.html')
def esignin(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(
            username=username,
            password=password
        )
        if user is not None:
            try:
                if user.employeeuser:
                    login(request, user)
                    return redirect('edash')
            except EmployeeUser.DoesNotExist:
                messages.error(request, 'please login with intern signup page.')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request,'esignin.html')
@login_required(login_url='esignin')
def edash(request): 
    
    user=EmployeeUser.objects.get(user=request.user.id)
    domain = Domain.objects.all()
    context = {'user': user, 'domain': domain}

    if request.POST:
        name=request.POST.get('domain')
        domain=Domain.objects.create(
            name=name
        )
        return redirect('edash')
    
    return render(request,'edash.html',context)
def elogout(request):
    logout(request)
    return redirect('index')

#display internlist in empployee dash
@login_required(login_url='esignin')
def internlist(request):
    internlist=InternUser.objects.all()
    context={'internlist':internlist}
    return render(request,'internlist.html',context)

#edit intern domain by employee
@login_required(login_url='esignin')
def editdomain(request, id):
    intern=InternUser.objects.filter(id=id).first()
    domain=Domain.objects.all()
    context={'intern':intern,'domain':domain}
    if request.POST:
        newdomain=request.POST.get('new_domain')
        print(newdomain)
        ndomain=Domain.objects.filter(name=newdomain).first()
        intern.domain=ndomain
        intern.save()
        return redirect('internlist')
    
    return render(request, 'editdomain.html',context)

#list the interns based on domain
@login_required(login_url='esignin')
def domaininternlist(request,dname):
    # Retrieve the Domain object based on the provided dname
    domain = Domain.objects.get(name=dname)
    # Retrieve all interns assigned to the specified domain
    intern = InternUser.objects.filter(domain=domain)
    context={'dname':dname,'intern':intern}
    return render(request,'domaininternlist.html',context)

#deactivate Intern useraccount
@login_required(login_url='esignin')
def deactivate_account(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_active=False
    user.save()
    return redirect('domaininternlist',dname=user.internuser.domain.name)

#activate Intern useraccount
@login_required(login_url='esignin')
def activate_account(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_active=True
    user.save()
    return redirect('domaininternlist',dname=user.internuser.domain.name)

#module creation
@login_required(login_url='esignin')
def createmodule(request):
    domain = Domain.objects.all()
    context={'domain':domain}
    if request.POST:
        name=request.POST.get('module')
        domain=request.POST.get('domain')
        topic=request.POST.get('topic')
        question=request.POST.get('question')
        selected_domain = Domain.objects.get(name=domain)
        new_module = Module(name=name, 
                            domain=selected_domain,
                            topic=topic,
                            question=question
                            )
        new_module.save()
        return redirect('edash')
    return render(request,'createmodule.html',context)

#module display
@login_required(login_url='esignin')
def modulelist(request,dname):
    domain=Domain.objects.get(name=dname)
    module=Module.objects.filter(domain=domain)
    context={'dname':dname,'module':module}
    return render(request,'modulelist.html',context)

#update module 
@login_required(login_url='esignin')
def updatemodule(request,id):
    module=Module.objects.filter(id=id)
    context={'module':module}
    if request.POST:
        name=request.POST.get('name')
        topic=request.POST.get('topic')
        question=request.POST.get('question')
        module=Module.objects.get(id=id)
        module.name=name
        module.topic=topic
        module.question=question
        module.save()
        return redirect('edash')

    return render(request,'updatemodule.html',context)
#delete module
@login_required(login_url='esignin')
def deletemodule(request,id):
    module=Module.objects.filter(id=id)
    module.delete()
    return redirect('edash')

    return render(request,'updatemodule.html')

#module completion status for each modules
@login_required(login_url='esignin')
def modulecompletionstatus(request, dname):
    domain = get_object_or_404(Domain, name=dname)

    # Retrieve all interns assigned to the specified domain
    interns = InternUser.objects.filter(domain=domain)

    # Retrieve all modules for the specified domain
    modules = Module.objects.filter(domain=domain)

    # Create a dictionary to store the completion status for each intern and module
    completion_status = {}

    for intern in interns:
        intern_status = {}
        for module in modules:
            # Check if there is an answer for the intern and module
            answer_exists = InternAnswer.objects.filter(intern_user=intern, module=module).exists()
            intern_status[module] = answer_exists

        completion_status[intern] = intern_status

    context = {
        'dname': dname,
        'interns': interns,
        'modules': modules,
        'completion_status': completion_status,
    }

    return render(request, 'modulecompletionstatus.html', context)

# Retrieve the answer details using intern_id and module_id
@login_required(login_url='esignin')
def answer_detail(request, intern_id, module_id):
    answer = InternAnswer.objects.get(intern_user__id=intern_id, module__id=module_id)
    return render(request, 'answer_detail.html', {'answer': answer})

#Profile editing
@login_required(login_url='esignin')
def empedit(request,id):
    empuser=EmployeeUser.objects.get(id=id)
    print(empuser.id)
    user=User.objects.get(id=request.user.id)
    print(user.id)
    
    context={
        'empuser':empuser,
        'user':user
    }
    if request.POST:
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        empuser.name=name
        empuser.phone=phone
        empuser.email=email
        user.email=email
        user.save()
        empuser.save()
        
        return redirect('edash')


    return render(request,'editprofile.html',context)
