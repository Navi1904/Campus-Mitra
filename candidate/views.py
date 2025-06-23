from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from hr.models import Hr, JobPost,CandidateApplications
from candidate.models import MyApplyJobList
# Create your views here.
@login_required
def candidate_dashbordh(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    jobs=JobPost.objects.all()
    print(jobs)
    return render(request,'candidate/dashboradh.html',{'jobs':jobs})
@login_required
def myJobListviews(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    myjobList=MyApplyJobList.objects.filter(user=request.user)
    return render(request,'candidate/myjoblist.html',{'myjobList':myjobList})
@login_required
def applyforjob(request,pk):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        if CandidateApplications.objects.filter(user=request.user,job=job).exists():
            return redirect('candidate_dashbordh')
        
    
        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            college = request.POST.get('college')
            passing_year = request.POST.get('passing_year')
            yearOfExperience = request.POST.get('yearOfExperience')
            resume = request.FILES.get('resume')
            cgpa=  request.POST.get("cgpa")
            Candidat_applications=CandidateApplications(user=request.user,job=job,passingYear=passing_year,yearOfExp=yearOfExperience,resume=resume,cgpa=cgpa)
            Candidat_applications.save()
            
            MyApplyJobList(user=request.user,job=Candidat_applications).save()
            job.applyCount += 1
            job.save()
            return redirect('candidate_dashbordh')
        return render(request,'candidate/apply.html')
    return redirect('candidate_dashbordh')

def aboutcom(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    jobs=JobPost.objects.all()
    print(jobs)
    return render(request,'candidate/aboutcompany.html',{'jobs':jobs})