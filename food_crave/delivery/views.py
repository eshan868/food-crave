from django.shortcuts import render
from . models import DeliveryAssignment
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from orders.models import Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum

# Create your views here.
def delivery_dashboard(request):

    
    assignments = Order.objects.filter(
        delivery_partner=request.user
    ).exclude(
        status='delivered'
    )
    completed_orders = Order.objects.filter(
        delivery_partner=request.user,
        status='delivered'
    ).count()

    today_earnings = Order.objects.filter(
        delivery_partner=request.user,
        status='delivered'
    ).aggregate(
        total=Sum('delivery_fee')
    )['total'] or 0



    
    return render(request,'delivery/delivery_dashboard.html',{
        'assignments':assignments,
         'completed_orders': completed_orders,
            'today_earnings': today_earnings,
            'progress_percent': min(
                completed_orders * 5,
                100
            )})





def new_orders(request):

    orders = Order.objects.filter(
        delivery_partner=None,
        status='placed'
    )

    return render(request, 'delivery/new_orders.html', { 'orders': orders})




def accept_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    if order.delivery_partner:
        return redirect(
            'new_orders'
        )

    order.delivery_partner = request.user

    order.status = 'accepted'

    order.save()
    return redirect('delivery-man-dashboard')

def picked_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        delivery_partner=request.user
    )

    order.status = 'picked'
    order.save()

    return redirect('delivery-man-dashboard')

def verify_otp(request, order_id):

    assignment = get_object_or_404(
        DeliveryAssignment,
        order_id=order_id,
        delivery_man=request.user
    )

    entered_otp = request.POST.get('otp')

    if entered_otp == assignment.order.delivery_otp:

        assignment.order.status = 'delivered'
        assignment.order.save()

    return redirect('delivery-man-dashboard')

@csrf_exempt
def update_location(request):

    if request.method == "POST":

        data = json.loads(request.body)

        request.user.latitude = data.get("latitude")
        request.user.longitude = data.get("longitude")

        request.user.save()

        return JsonResponse({
            "success": True
        })

    return JsonResponse({
        "success": False
    })
