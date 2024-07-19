from django.shortcuts import render,redirect
from .models import FundaoCirurgicoTB

# Create your views here.
def main(request):
    
    if request.method == "GET":
        return render(request, "page.html")
    
    text = request.POST.get("text")
    subtext = request.POST.get("subtext")
    author = request.POST.get("author")
        
    fundones = FundaoCirurgicoTB(
        text=text, 
        subtext=subtext, 
        author=author, 
        processed=False
        )
    
    fundones.save()
    
    return redirect("main")