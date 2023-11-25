
import base64, uuid
from django.core.files.base import ContentFile

def get_report_image(data):
    f, str_image = data.split(";base64")
    return str_image


def is_ajax(request):
    rmg = request.META.get("HTTP_X_REQUESTED_WITH")
    xhr = "XMLHttpRequest"
    if  rmg ==  xhr:
        print("it is ajax")
        ret = True
    else:
        print( f"{rmg} vs {xhr}")
        ret = False

    return ret
