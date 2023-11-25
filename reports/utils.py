
import base64, uuid
from django.core.files.base import ContentFile

def get_report_image(data):
    f, str_image = data.split(";base64")
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + '.png'
    print(f"img_name={img_name}")
    data = ContentFile(decoded_img, name=img_name)
    return data


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
