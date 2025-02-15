from django.shortcuts import render, redirect
from django.conf import settings
import os

# Create your views here.
def home(request):
    return render(request, 'index.html')


def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        file_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)
        
        with open(file_path, 'wb+') as destination:
            for chunk in pdf_file.chunks():
                destination.write(chunk)
        
        return redirect(f'/kitab/search?pdf={pdf_file.name}')

    return render(request, 'upload.html')

def search_pdf(request):
    pdf_name = request.GET.get('pdf', '')
    return render(request, 'search.html', {'pdf': pdf_name})