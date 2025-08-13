from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import EncryptedFileForm
from .models import EncryptedFile
from django.http import HttpResponse
from .utils import encrypt_file, decrypt_file
import os

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            filename = request.POST.get('filename', uploaded_file.name)
            encrypted_data = encrypt_file(uploaded_file.read())

            file_path = f'media/encrypted_files/{filename}.enc'
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)
                
            saved = EncryptedFile.objects.create(
                filename=filename,
                file=f'encrypted_files/{filename}.enc',
            )
            return render(request, 'file_list.html', {'uid': saved.uid})
    else:
        form = EncryptedFileForm()
    return render(request, 'upload.html', {'form': form})

def list_files(request):
    files = EncryptedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def download_file(request, file_id):
    file_obj = get_object_or_404(EncryptedFile, pk=file_id)
    file_path = os.path.join('media', file_obj.file.name)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_file(encrypted_data)
    response = HttpResponse(decrypted_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename={file_obj.filename}'
    return response