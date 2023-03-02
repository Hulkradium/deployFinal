from django.shortcuts import render, redirect
from Intervention.models import Lecturer, Student, Intervention, Severity
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'GET':
        lect_id = request.GET.get("lect_id")
        data = Lecturer.objects.filter(lect_id=lect_id)
        num_lect = data.count()
        dict = {
            'data': data,
            'num_lect': num_lect,
        }
        if lect_id is None:
            dict['message'] = "Please enter your Lecturer's ID."
        return render(request, "index.html", dict)
    else:
        return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        lect_id = request.POST.get('lect_id')
        password = request.POST.get('password')
        try:
            lecturer = Lecturer.objects.get(lect_id=lect_id)
        except Lecturer.DoesNotExist:
            error_message = 'Lecturer ID not found. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
        if lecturer.password == 'null':
            error_message = 'Account not yet registered. Please Sign Up first.'
            request.session['lect_id'] = lecturer.lect_id
            return render(request, 'login.html', {'error_message': error_message})
        elif lecturer.password == password:
            # Redirect to the lecturer's specific home page
            return redirect('home', lect_id=lect_id)
        else:
            error_message = 'Invalid password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        lect_id = request.POST['lect_id']
        password = request.POST['password']
        try:
            lecturer = Lecturer.objects.get(lect_id=lect_id)
            lecturer.password = password
            lecturer.save()
            message = 'Password updated successfully!'
        except Lecturer.DoesNotExist:
            message = 'Invalid Lecturer ID. Please try again.'
        return render(request, 'signup.html', {'message': message})
    else:
        return render(request, 'signup.html')


def home(request, lect_id):
    lecturer = Lecturer.objects.get(lect_id=lect_id)
    return render(request, 'home.html', {'lecturer': lecturer})


def logout(request):
    return redirect('login')


def intervention_report(request, lect_id):
    if request.method == 'POST':
        # get the form data
        int_id = request.POST.get('int_id')
        int_stud_id = request.POST.get('int_stud_id')
        int_lect_id = request.POST.get('int_lect_id')
        date_report = request.POST.get('date_report')
        description = request.POST.get('description')
        action = request.POST.get('action')
        category = request.POST.get('category')
        int_sev_id = request.POST.get('int_sev_id')

        # get the student and lecturer objects
        try:
            student = Student.objects.get(stud_id=int_stud_id)
        except Student.DoesNotExist:
            messages.error(request, 'Student ID not found')
            return redirect('intervention_report', lect_id=lect_id)
        
        try:
            lecturer = Lecturer.objects.get(lect_id=int_lect_id)
        except Lecturer.DoesNotExist:
            messages.error(request, 'Lecturer ID not found')
            return redirect('intervention_report', lect_id=lect_id)
        
        severity = Severity.objects.get(sev_id=int_sev_id)

        # create the Intervention object
        intervention = Intervention(
            int_id=int_id,
            int_stud_id=student,
            int_lect_id=lecturer,
            date_report=date_report,
            description=description,
            action=action,
            category=category,
            int_sev_id=severity
        )

        # save the Intervention object to the database
        intervention.save()

        messages.success(request, 'Intervention report submitted successfully.')
        # redirect user back to the report page
        return redirect('intervention_report', lect_id=lect_id)

    return render(request, 'intervention_report.html')


def intervention_list(request, lect_id):
    interventions = Intervention.objects.all()
    return render(request, "intervention_list.html", {"interventions": interventions})


def update_intervention(request, lect_id, int_id):
    data = Intervention.objects.get(int_id=int_id)
    if not data:
        return redirect("intervention_list")
    context = {
        "data": data,
        "lect_id": lect_id
    }
    return render(request, "update_intervention.html", context)


def save_update_intervention(request, int_id):
    submit = request.POST.get("submit")
    data = Intervention.objects.get(int_id=int_id)
    data.submit = submit
    data.save()
    return HttpResponseRedirect(reverse('intervention_list', args=[data.int_lect_id.lect_id]))


def delete_intervention(request, int_id, lect_id):
    data = Intervention.objects.filter(int_id=int_id)
    if not data:
        return redirect("intervention_list", lect_id=lect_id)
    data.delete()
    return redirect("intervention_list", lect_id=lect_id)


def student_list(request, lect_id):
    if request.method == 'GET':
        student_id = request.GET.get('student_id')

        if student_id:
            try:
                student = Student.objects.get(stud_id=student_id)
                interventions = Intervention.objects.filter(
                    int_stud_id=student)

                return render(request, 'student_list.html', {
                    'student': student,
                    'interventions': interventions
                })
            except Student.DoesNotExist:
                message = "Student does not exist. Please enter a valid ID."
                return render(request, 'student_list.html', {
                    'message': message
                })

    return render(request, 'student_list.html')