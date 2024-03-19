from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Notice
from .serializers import NoticeSerializer


class NoticeList(APIView):
    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


notice_list = NoticeList.as_view()


class NoticeDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)

    def put(self, request, pk):
        notice = self.get_object(pk)
        if not request.user.is_authenticated or notice.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notice = self.get_object(pk)
        if not request.user.is_authenticated or notice.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


notice_detail = NoticeDetail.as_view()
