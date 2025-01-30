from django.shortcuts import *
from .models import *
from .forms import *
def index(request):
    pisos = Piso.objects.all()
    return render(request, 'mesas/index.html', {'pisos': pisos})

def agregar_piso(resquest):
    if resquest.method == 'POST':
        form = PisoForm(resquest.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')
    