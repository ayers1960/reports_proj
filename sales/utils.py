
import uuid, base64
from customers.models import Customer
from profiles.models import Profile
from io import BytesIO
import matplotlib.pyplot as plt

def generate_code():
    #code = str(uuid.uuid4()).replace('-','').upper[:12]
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code

def get_salesman_from_id(val):
    return Profile.objects.get(id=val).user.username

def get_customer_from_id(val):
    return Customer.objects.get(id=val)
    
def get_graph():
    buffer = BytesIO()
    plt.safefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf8')
    buffer.close()
    return graph

def get_chart():
    chart = get_graph()
    return chart