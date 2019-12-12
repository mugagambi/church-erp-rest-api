from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.utils import models, admin_uid, erp_database, erp_admin_password


@api_view(['GET'])
def index(request):
    """
    Fetch the latest news
    """
    if request.method == 'GET':
        news_list = models.execute_kw(erp_database, admin_uid, erp_admin_password,
                                      'church.news', 'search_read',
                                      [[]],
                                      {'fields': ['name', 'article', 'date', 'author', 'website']})
        return Response(news_list)
