import pyqrcode

from django.shortcuts import render, HttpResponse

def main(request):
    return render(request, 'qrcode_generator/main.html')

def qrcode_coupon(request):
    coupon_url = request.GET['coupon_url']
    coupon_key = request.GET['coupon_key']
    url = coupon_url + coupon_key
    qr = pyqrcode.create(url, error='L', version=10, mode='binary')

    response = HttpResponse(content_type="image/png")
    qr.png(response, scale=2)

    return response
