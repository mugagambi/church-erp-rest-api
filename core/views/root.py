from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'News': reverse('news_list', request=request, format=format),
        'Order Of Service': reverse('order_of_service', request=request, format=format),
    })
