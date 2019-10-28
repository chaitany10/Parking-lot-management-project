from .models import parkingLot, block, floor, parking_slot
# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render

from .models import parkingLot, block, floor, parking_slot

# from users.models import UserInfo
# from tariff.models import Tariffs,Tickets,Rates
User = get_user_model()


def parking_lot_index(request):  # ,site_num):
    # site_no = get_object_or_404(Site, site_num=site_num)
    # if not request.user.is_authenticated:
    #     return redirect('/users/home')
    # rates= Rates.objects.filter()
    positions_list = parkingLot.objects.filter()  # (position_status=True)
    # for rate in rates:
    #     print(rate.pay_per_time)
    zipped_data = zip(positions_list)
    context = {
        # 'rates': rates,
        'positions_list': positions_list,
        'zipped_data': zipped_data
    }
    return render(request, 'parking_lot_index.html', context)


def block_index(request, parking_lot_no):
    positions_list = block.objects.filter(parking_lot_id=parking_lot_no)
    context = {
        'positions_list': positions_list
    }
    return render(request, 'block_index.html', context)


def floor_index(request, block_no):
    positions_list = floor.objects.filter(block_id=block_no)
    context = {
        'positions_list': positions_list
    }
    return render(request, 'floor_index.html', context)


def parking_slot_index(request, floor_no):
    positions_list = parking_slot.objects.filter(floor_id=floor_no and is_reserved=False)
    context = {
        'positions_list': positions_list
    }
    return render(request, 'parking_slot_index.html', context)

# def site_position_book(request,site_no):
#     # status_list = Positions.objects.get(site_no=site_no)
#     if not request.user.is_authenticated:
#         return redirect('/users/home')
#     positions_list = Site.objects.filter(site_no=site_no)# and status_list.site_no=site_no and status_list.position_status=True )
#     # site_name= Site.objects.filter(site_no=site_no).site_address
#     context = {
#         'site_no':site_no,
#         # 'site_name':site_name
#     }

#     # print(positions_list)
#     context['positions_list']=positions_list
#     return render(request,'car_posi_index.html',context)


# def download_positions(request):
#     if not request.user.is_superuser :
#         return redirect('/users/home')

#     qs = Site.objects.all()    
#     return render_to_csv_response(qs,filename=u'slots.csv')

# def order_position(request,site_no,posi_num):
#     if not request.user.is_authenticated:
#         return redirect('/users/home')

#     position_object=Positions.objects.get(site_no=site_no, position_num = posi_num)
#     position_object.position_status = False
#     position_object.save()

#     Siteobject = Site.objects.get(site_no=site_no)
#     user_info = User.objects.get(username=request.user) #Get user information
#     ticket = Tickets.objects.order_by('-per_hour_money')
#     tariff = Tariffs()
#     tariff.user_name = request.user

#     UserInfoInstance = UserInfo.objects.get(user_name=user_info)
#     # print(UserInfoInstance.car_number)
#     UserInfoInstance.car_booking_status = True
#     UserInfo.admin_bit=False
#     UserInfoInstance.car_site_address = Siteobject.site_address
#     UserInfoInstance.car_slot_no = position_object.position_num

#     # print(UserInfoInstance.car_booking_status)
#     UserInfoInstance.save()

#     tariff.car_number = UserInfoInstance.car_number
#     tariff.ticket_type = 'Hour'
#     tariff.start_time= datetime.now()
#     tariff.end_time= datetime.now()

#     # print(datetime.now())
#     # print(tariff.start_time)
#     tariff.parking_time = 0
#     tariff.site_address = Siteobject.site_address
#     tariff.postion_no=position_object.position_num
#     tariff.per_hour_money = Siteobject.pay_per_time
#     tariff.parking_money= tariff.per_hour_money
#     # print(tariff.per_hour_money)

#     tariff.save()       

#     return render(request , 'bocked.html')


# def admins(request):
#     if not (request.user.is_superuser or request.user.is_site_manager):
#         return redirect('/users/home')
#     rates= Rates.objects.filter()
#     positions_list = Site.objects.filter()#(position_status=True)
#     # for rate in rates:
#     #     print(rate.pay_per_time)
#     zipped_data=zip(positions_list, rates)
#     context = {
#         'rates': rates,
#         'positions_list':positions_list,
#         'zipped_data':zipped_data
#     }
#     return render(request,'car_site_index_admin.html',context)

# def admin_position(request,site_no):
#     if not (request.user.is_superuser or request.user.is_site_manager):
#         return redirect('/users/home')

#     positions_list = Site.objects.filter(site_no=site_no)# and status_list.site_no=site_no and status_list.position_status=True )
#     # site_name= Site.objects.filter(site_no=site_no).site_address
#     context = {
#         'site_no':site_no,
#         # 'site_name':site_name
#     }

#     # print(positions_list)
#     context['positions_list']=positions_list
#     return render(request,'car_posi_index_admin.html',context)
