from rest_framework.response import Response
from movie.models import Movie
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import MovieSerializer , userSerializer



@api_view(["GET",])
@permission_classes([IsAuthenticated,])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(["POST",])
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"movie has been created"
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def api_signup(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                "success":False,
                "errors":str(e)
            },status=status.HTTP_400_BAD_REQUEST)
        return Response(data={
            "success":True,
            "message":"user has been created successfully "
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)


class createMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class showMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


