from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .swaper_p_p import *
from .swaper_pp import *


def index(request):
    return render(request, "index2.html")

class HandelFileUpload(APIView):
    def post(self, request):
        try: 
            data = request.data
            serializer = FlieListSerilizers(data=data)
            if serializer.is_valid():
                serializer.save()
                items = []
                for item in os.listdir(f"public/static/{serializer.data['folder']}"):
                    print(item)
                    items.append(f"{serializer.data['folder']}\{item}")
                run_it(items[0], items[1], f"{serializer.data['folder']}")

                return Response({
                    'status': 200,
                    'message': 'Files uploaded successfully',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'data': serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error'
            })
        
class HandelFaceFileUpload(APIView):
    def post(self, request):
        try: 
            data = request.data
            serializer = FlieListSerilizers(data=data)
            if serializer.is_valid():
                serializer.save()
                items = []
                for item in os.listdir(f"public/static/{serializer.data['folder']}"):
                    print(item)
                    items.append(f"{serializer.data['folder']}\{item}")
                run_iit(items[0], f"{serializer.data['folder']}")

                return Response({
                    'status': 200,
                    'message': 'Files uploaded successfully',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'data': serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error'
            })
        
