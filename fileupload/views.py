import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm


def handle_uploaded_file(f):
    # Read the file into a DataFrame
    if f.name.endswith('.csv'):
        df = pd.read_csv(f)
    elif f.name.endswith('.xlsx'):
        df = pd.read_excel(f)  
    else:
       return None
    return df

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            if summary:
                return render(request, 'fileupload/summary.html', {'summary': summary.to_html(index=False)})
            return render(request, 'fileupload/error.html')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})
