from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import text_gen,cb


@api_view(['POST'])
def seeeeeeeed(request):
    product = request.data.get("product")
    category = request.data.get("category")
    desc = request.data.get("desc")
    return Response({"desc":text_gen.response_from_ai(desc,product,category)}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def seeeeeeed(request):
    inp = request.data.get("input")
    product = request.data.get("pro")
    desc = request.data.get("desc")
    return Response({"inp":text_gen.resp_from_ai(inp,desc,product)}, status=status.HTTP_201_CREATED)

