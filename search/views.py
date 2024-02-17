from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mentors
from .serializers import MentorSerializers
import requests
from django.db.models import Q


# Create your views here.

def index(request):        
    return render(request , "index.html",{} )

def search(request):
    print("The request is a ",request.method," method.")
    if request.method == "GET":
        query = request.GET.get("query"," ")
        if query =="" or query==" ":
            return HttpResponse("Internal django server error")
        print("The query is :",query)
        api_url = "http://127.0.0.1:8000/api/search_mentors/"
        response = requests.get(api_url,params={'expertise': query})
        if response.status_code == 200:
            return HttpResponse(response.content)
        return HttpResponse("None")

@api_view(["POST" , "GET"])
def use_api(request):
    print("The request method is :",request.method)
    if request.method == "POST":
        datas = request.data
        for data in datas:
            print(data)
            serializer = MentorSerializers(data = data)
            if serializer.is_valid():
                serializer.save()
        return Response({"Message":"Details saved"})
    
    elif request.method == "GET":
        allobjs = Mentors.objects.all()
        serializer = MentorSerializers(allobjs,many=True)
        return Response(serializer.data)



@api_view(["GET"])
def search_api(request):
    query = request.query_params.get("expertise", "")
    print("API recieved this query.",query)
    if query.strip():
        print(query.strip())
        mentors = Mentors.objects.filter(Q(expertise__icontains=query) | Q(description__icontains=query))
        serializer = MentorSerializers(mentors, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "No query parameter provided"})