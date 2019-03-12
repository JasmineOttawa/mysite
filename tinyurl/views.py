from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.shortcuts import redirect,reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import timezone
from .models import mapURL

def index(request):
    return render(request,'tinyurl/index.html') 

def shortenurl(request):
    sURL = get_random_string(6) 
    p = mapURL()
    p.sURL = sURL 
    p.lURL = request.POST['lURL'] 
    p.created = timezone.now() 
    p.save()
    html = "<html><body>short URL is %s.</body></html>" % sURL
    return HttpResponse(html)

def longURL(request,sURL):
#    lURL = mapURL.objects.get(sURL="%s" % sURL)
#    html = "<html><body>long URL is %s.</body></html>" % lURL 
#    return HttpResponse(html)
#    return redirect(lURL) # return message "argument of type '....' is not iterable" lURL is an object instead of a string
#    return redirect('http://www.google.com')
     p = mapURL.objects.get(sURL="%s" % sURL)
     return redirect(p.lURL)

