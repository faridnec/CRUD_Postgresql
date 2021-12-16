from django.shortcuts import render
from CRUD_Uygulama.models import Calisan
from django.contrib import messages
from CRUD_Uygulama.forms import Form


def Ara(request):
    if request.method == "POST":
        gorev = request.POST.get('gorev')
        calisanaraobj = Calisan.objects.raw(
            'SELECT * FROM public."Calisan" WHERE gorev=\''+gorev+'\'')
        return render(request, 'index.html', {"Calisan": calisanaraobj})
    else:
        calisanobj = Calisan.objects.raw('SELECT * FROM public."Calisan"')
        return render(request, 'index.html', {"Calisan": calisanobj})


def Ekle(request):
    if request.method == 'POST':
        if request.POST.get('ad') and request.POST.get('soyad') and request.POST.get('adres') and request.POST.get('cinsiyet') and request.POST.get('gorev') and request.POST.get('calisanTipi'):
            saverecord = Calisan()
            saverecord.ad = request.POST.get('ad')
            saverecord.soyad = request.POST.get('soyad')
            saverecord.adres = request.POST.get('adres')
            saverecord.cinsiyet = request.POST.get('cinsiyet')
            saverecord.gorev = request.POST.get('gorev')
            saverecord.calisanTipi = request.POST.get('calisanTipi')
            saverecord.save()
            messages.success(request, 'Calisan '+saverecord.ad +
                             ' '+saverecord.soyad+' eklendi....')
            return render(request, 'ekle.html')
    else:
        return render(request, 'ekle.html')


def Duzelt(request, calisanNo):
    editcalisan = Calisan.objects.get(calisanNo=calisanNo)
    return render(request, 'duzelt.html', {"Calisan": editcalisan})


def Guncelle(request, calisanNo):
    updatecalisan = Calisan.objects.get(calisanNo=calisanNo)
    form = Form(request.POST, instance=updatecalisan)
    if form.is_valid():
        form.save()
        messages.success(request, 'Veri(ler) güncellenmiştir...')
        return render(request, 'duzelt.html', {"Calisan": updatecalisan})


def Sil(request, calisanNo):
    delcalisan = Calisan.objects.get(calsianNo=calisanNo)
    delcalisan.delete()
    showdata = Calisan.objects.all()
    return render(request, "index.html", {"Calisan": showdata})
