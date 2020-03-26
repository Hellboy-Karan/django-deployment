from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'Hello world','number':100}
    return render(request,'basic_app/index.htm',context_dict)

def other(request):
    return render(request,'basic_app/other.htm')

def relative(request):
    return render(request,'basic_app/relative_url_template.htm')