from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from api.utils import paginate


# parameters: page, pagesize
@api_view(['GET'])
def get_data(request):
    page_param = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('pagesize', 15))
    with open(r'./data/pcr_region_coverage.json') as f:
        data = json.load(f)
    return Response(paginate(data, page_param, page_size))
