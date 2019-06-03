from django.shortcuts import render, get_object_or_404
from .serializer import MemoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Memo


# Create your views here.
@api_view(['GET', 'POST']) #허용할 http method를 적어줌
def memo_list(request):
    if request.method=="GET":
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return Response(serializer.data)
    else:
        # CREATE
        memo = request.data
        # Create an article from the above data
        serializer = MemoSerializer(data=memo)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
        