from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.utils import models, admin_uid, erp_database, erp_admin_password


@api_view(['GET'])
def index(request):
    """
    Fetch the order of service
    """
    if request.method == 'GET':
        services = models.execute_kw(erp_database, admin_uid, erp_admin_password,
                                     'church.services', 'search_read',
                                     [[]],
                                     {'fields': ['name', 'date', 'group']})
        for idx, service in enumerate(services):
            sessions = models.execute_kw(erp_database, admin_uid, erp_admin_password,
                                         'church.services.sessions', 'search_read',
                                         [[['service_id', '=', service['id']]]],
                                         {'fields': ['name', 'start', 'end']})
            services[idx]['sessions'] = sessions
        return Response(services)
