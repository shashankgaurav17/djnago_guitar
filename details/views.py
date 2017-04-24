from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from details.models import Details as Details
from details.models import Login
import logging
#from login.models import Login

# Create your views here.

logger = logging.getLogger(__name__)

class DetailsList(ListView):
    template_name = "details/index.html"
    model = Details

class DetailsId(ListView):
    template_name = "details/detailsID.html"

    def get_queryset(self):
        return Details

    def get(self, request,album_id):
        #requested_id = request.GET.get('id', None)
        req_id = self.get_queryset().objects.all().filter(id=album_id)
        return render(request, "details/detailsID.html", {'list':req_id})

#def detailsId(request, album_id):
#    return HttpResponse("<h2>Details for Album id : " + str(album_id) + "</h2>")
    #return render(request,album_id,'details/detailsID.html')


def browse(request):
    requested_capo = request.GET.get('cappo',None)
    requested_type = request.GET.get('type',None)
    requested_language = request.GET.get('language',None)
    details1 = Details.objects.all()
    if requested_capo is not None:
        details1 = details1.filter(cappo = requested_capo)

    if requested_type is not None:
        details1 = details1.filter(type = requested_type)

    if requested_language is not None:
        details1 = details1.filter(language = requested_language)

    details1.values()

    logger.debug("hello "+str(details1))
    return render(request,'details/browse.html',{'details2':details1})

class LoginList(ListView):
    template_name = "details/login.html"
    model = Login

def home(request):
    return render(request,'details/home.html')

#def browse(request):
#    return render(request,'details/browse.html')