from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from .serializers import *
from .swaper_p_p import *
from .swaper_pp import *


def index(request):
    return render(request, "index.html")

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
                serializer.zip_files(f"{serializer.data['folder']}")
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
    def download(request, uid):
        return render(request, '')    
    
        
class HandelFaceFileUpload(APIView):
    def post(self, request):
        
        try: 
            data = request.data
            serializer = FlieListSerilizers(data=data)
            
            if serializer.is_valid():
                print("here")
                serializer.save()
                items = []
                for item in os.listdir(f"public/static/{serializer.data['folder']}"):
                    print(item, "pp")
                    items.append(f"{serializer.data['folder']}\{item}")
                run_iit(items[0], f"{serializer.data['folder']}")
                print("here")
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
        
