from django.shortcuts import render
from .forms import NewsletterForm
import requests 
from django.http import JsonResponse 
from accounts.models import Referral, User
from django.conf import settings
# Create your views here.






def dashboard(request):
    user = request.user.username
    current_user = request.user
    referral = Referral.objects.filter(user__username=user).values('code').first()['code']

    
    



    context = {"username": user, "ref":referral}
    return render(request,"dashboard.html", context)



def hashrate(request):  #work on this later!!!
    user = request.user.username
    API = "PK_kAVDnrlnNQtn8WfnynHE7"
    response = requests.get(f"https://webminepool.com/api/{API}/user_hashes/{user}")
    data = response.json()["hashes"]


    return JsonResponse({"data": data})



def  newsletter(request):
    if request.method == "POST":
        form = NewsletterForm()
        if form.is_valid():
            form.save()

    else:
        form = NewsletterForm()
    

    context = {"form": form}
    return render(request, "index.html", context)




def privacy(request):


    return render(request, "privacy.html")











