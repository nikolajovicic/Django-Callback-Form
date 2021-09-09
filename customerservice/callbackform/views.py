from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from .models import SupportRequest
from .forms import SupportRequestForm

class IndexView(generic.FormView):
    form_class = SupportRequestForm
    template_name = 'callbackform/index.html'
    success_url ="success/"
    

def contact_view(request):
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'callbackform/success.html')
    form = SupportRequestForm()
    context = {'form': form}
    return render(request, 'callbackform/index.html', context)

def sucess_request(request):
    return render(request, 'callbackform/success.html')
