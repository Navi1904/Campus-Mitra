from django.shortcuts import redirect, render
from hr.models import CandidateApplications, Hr, JobPost, SelectCandidateJob
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def hrhome(request):
    if Hr.objects.filter(user=request.user).exists():
        jobpost=JobPost.objects.filter(user=request.user)
        print(jobpost)
        return render(request,'hr/hrdashbordh.html',{'jobpost':jobpost})
    return redirect ('hr_dash')
@login_required
def post_job(request):
    msg=None
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date  = request.POST.get('last-date')
        
        companydescription=request.POST.get('company-des')

        jobpost = JobPost(user=request.user,title=job_title,address=address,compnayName=company_name,salaryLow=salary_low,salaryHigh=salary_high,lastDateToApply=last_date,companyDescription=companydescription)
        jobpost.save()
        msg = "Job posted successfully!"
        return render(request,'hr/post_job.html',{'msg':msg})
    return render(request,'hr/post_job.html')

@login_required
def candidate(request,pk):
    if JobPost.objects.filter(id=pk).exists():
        job=JobPost.objects.get(id=pk)
        applications=CandidateApplications.objects.filter(job=job)
        selectedapplication=SelectCandidateJob.objects.filter(job=job)
        return render(request,'hr/candidate.html',{'applications':applications,'selectedapplication':selectedapplication,'jobpost':job})
    return redirect('hr_dash')

@login_required
def selectedCandidate(request):
    if request.method == 'POST':
        candidateid=request.POST.get('candidateid')
        jobpostid=request.POST.get('jobpostid')
        
        job=JobPost.objects.get(id=jobpostid)
        candidate=CandidateApplications.objects.get(id=candidateid)
        SelectCandidateJob(job=job,candidate=candidate).save()
        return redirect('hr_dash')
    return redirect('hr_dash')
@login_required
def deleteCandidate(request):
    if request.method=="POST":
        candidateid=request.POST.get('candidateid')
        jobpostid=request.POST.get('jobpostid')
        
        job=JobPost.objects.get(id=jobpostid)
        CandidateApplications.objects.get(id=candidateid).delete()
        job.applyCount = job.applyCount - 1
        job.save()
    return redirect('hr_dash')
def about(request):
    return render(request,'hr/about.html')
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from .models import CandidateApplications

def send_email(request, candidate_id):
    if request.method == 'POST':
        # Get the candidate application
        candidate = get_object_or_404(CandidateApplications, id=candidate_id)
        
        # Compose email
        subject = 'Your Profile Details'
        message = (
            f'Hello {candidate.user.username},\n\n'
            f'Here are your profile details:\n\n'
            f'Name: {candidate.user.username}\n'
            f'Email: {candidate.user.email}\n'
            f'Passing Year: {candidate.passingYear}\n'
            f'Years of Experience: {candidate.yearOfExp}\n'
            f'CGPA: {candidate.cgpa}\n'
            f'Resume: {candidate.resume.url if candidate.resume else "No resume available"}\n\n'
            f'Thank you!'
        )
        from_email = settings.DEFAULT_FROM_EMAIL  # Or replace with your email
        recipient_list = [candidate.user.email]
        
        # Send email
        send_mail(subject, message, from_email, recipient_list)
        
        # Redirect or send a success message
        return render(request,'hr/success_page.html')  # Replace with the actual success page name

    return redirect('error_page')  # Replace with an error handling page
