from django.http import HttpResponse
import math

def rectangle_area(request,height, width):
    response = HttpResponse(f"The area of the rectangle with height {height} and width {width} is {height * width}")
    return response

def rectangle_area_query(request):
    height=request.GET.get("height")
    width=request.GET.get("width")
    response = HttpResponse(f"The area of the rectangle with height {height} and width {width} is {int(height) * int(width)}")
    response.status_code=409
    return response

# http://127.0.0.1:8000/rectangle/area/?height=2&width=5












# def test(request, width):
#     return HttpResponse("hello world %o" % width) 

def rectangle_perimeter(request, height, width):
    response = HttpResponse(f"The perimeter of the rectangle with height {height} and width {width} is {2*height + 2*width}")
    return response


def circle_perimeter(request, radius):
    response = HttpResponse(f"The perimeter of the circle with radius {radius} is {2*radius*math.pi}")
    return response


def circle_area(request, radius):
    response = HttpResponse(f"The area of the circle with radius {radius} is {(radius*radius)*math.pi}")
    return response

    