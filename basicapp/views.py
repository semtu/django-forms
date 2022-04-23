from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print('validation success')
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"TEXT: {form.cleaned_data['text']}")
    return render(request, 'basicapp/form_page.html', context={'form':form})