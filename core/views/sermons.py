from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.utils import models, admin_uid, erp_database, erp_admin_password


@api_view(['GET'])
def index(request):
    """
    Fetch the latest sermons
    """
    if request.method == 'GET':
        sermon_list = models.execute_kw(erp_database, admin_uid, erp_admin_password,
                                        'church.sermons', 'search_read',
                                        [[]],
                                        {'fields': ['name', 'sermon', 'youtube_video_url', 'date', 'preached_by',
                                                    'type', 'image']})
        return Response(sermon_list)
