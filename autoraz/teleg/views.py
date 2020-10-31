from django.views.generic import ListView, View
from .models import User
from django.shortcuts import render, get_object_or_404
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

class VideoListView(View):
    def get(self, request):
        obj = User.objects.all()
        return render(request, "welcome.html", context={"app_list": obj})
class AddressView(View):
    def get(self, request, pk):
        obj = User.objects.get(url=pk)
        return render(request, 'twr.html', {"app_list": obj})
class AddressView1(View):
    def get(self, request, pk):
        obj = User.objects.get(url1=pk)
        return render(request, 'twr1.html', {"app_list": obj})
class AddressView2(View):
    def get(self, request, pk):
        obj = User.objects.get(url2=pk)
        return render(request, 'twr2.html', {"app_list": obj})
class AddressView3(View):
    def get(self, request, pk):
        obj = User.objects.get(url3=pk)
        return render(request, 'twr3.html', {"app_list": obj})
class AddressView4(View):
    def get(self, request, pk):
        obj = User.objects.get(url4=pk)
        return render(request, 'twr4.html', {"app_list": obj})
class AddressView5(View):
    def get(self, request, pk):
        obj = User.objects.get(url5=pk)
        return render(request, 'twr5.html', {"app_list": obj})
class AddressView6(View):
    def get(self, request, pk):
        obj = User.objects.get(url6=pk)
        return render(request, 'twr6.html', {"app_list": obj})
class AddressView7(View):
    def get(self, request, pk):
        obj = User.objects.get(url7=pk)
        return render(request, 'twr7.html', {"app_list": obj})
class AddressView8(View):
    def get(self, request, pk):
        obj = User.objects.get(url8=pk)
        return render(request, 'twr8.html', {"app_list": obj})
class AddressView9(View):
    def get(self, request, pk):
        obj = User.objects.get(url9=pk)
        return render(request, 'twr9.html', {"app_list": obj})
class AddressView10(View):
    def get(self, request, pk):
        obj = User.objects.get(url10=pk)
        return render(request, 'twr10.html', {"app_list": obj})
class AddressView11(View):
    def get(self, request, pk):
        obj = User.objects.get(url11=pk)
        return render(request, 'twr11.html', {"app_list": obj})
class AddressView12(View):
    def get(self, request, pk):
        obj = User.objects.get(url12=pk)
        return render(request, 'twr12.html', {"app_list": obj})
class AddressView13(View):
    def get(self, request, pk):
        obj = User.objects.get(url13=pk)
        return render(request, 'twr13.html', {"app_list": obj})
class AddressView14(View):
    def get(self, request, pk):
        obj = User.objects.get(url14=pk)
        return render(request, 'twr14.html', {"app_list": obj})
class AddressView15(View):
    def get(self, request, pk):
        obj = User.objects.get(url15=pk)
        return render(request, 'twr15.html', {"app_list": obj})
class AddressView16(View):
    def get(self, request, pk):
        obj = User.objects.get(url16=pk)
        return render(request, 'twr16.html', {"app_list": obj})
class AddressView17(View):
    def get(self, request, pk):
        obj = User.objects.get(url17=pk)
        return render(request, 'twr17.html', {"app_list": obj})
class AddressView18(View):
    def get(self, request, pk):
        obj = User.objects.get(url18=pk)
        return render(request, 'twr18.html', {"app_list": obj})
class AddressView19(View):
    def get(self, request, pk):
        obj = User.objects.get(url19=pk)
        return render(request, 'twr19.html', {"app_list": obj})

