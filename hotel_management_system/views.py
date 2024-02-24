from django.shortcuts import render
from hotel_management_system.models import Hotel
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
      return render(request,'index.html')

def hotel_signup(request):
      print("+++++++++++++++++++++++")
      error = ""
      # if request.user.role == "HOTEL":
      print("==============================")
      if request.method == "POST":
            hotel_name = request.POST['hotel_name']
            username = request.POST['username']
            password = request.POST['password']
            address = request.POST['address']
            place = request.POST['place']
            district = request.POST['district']
            state = request.POST['state']
            emails = request.POST['emails']
            phone = request.POST['phone']
            photo = request.FILES.get('photo')
            print("=====================================================",hotel_name,photo,phone)

            try:
                  hotels=Hotel.objects.create(hotel_name = hotel_name, username = username, password = password, address = address, place = place, district = district, state = state, emails = emails, phone = phone, photo = photo)
                  hotels.save()
                  error = 'no'
            except:
                  error = 'yes'
      content = {'error':error}
      return render(request,'hotel_signup.html',content)

def hotel_login(request):
      print("================")
      error = ""
      if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)

      return render(request,'hotel_login.html')