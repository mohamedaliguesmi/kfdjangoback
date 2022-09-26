import profile
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

from finalback.models import  (
    Arbitrator,
    Coach,
    Athlete,
    Club,
    Profile,
    Supporter,
    role
)
from .serializers import  (
    ArbitratorSerializer,
    CoachSerializer,
    AthleteSerializer,
    ClubSerializer,
    ProfileSerializer,
    RegisterSerializer,
    RoleSerializer,
    SupporterSerializer
)

def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
        
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })


#just for testing the token (ichouf ken el user mte3ou)
@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info': {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                #"location" : profile.location
                
            }
        })  
    return Response({'error':'token'}, status=400)



class RoleList(generics.ListCreateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArbitratorList(generics.ListCreateAPIView):
    queryset = Arbitrator.objects.all()
    serializer_class = ArbitratorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArbitratorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arbitrator.objects.all()
    serializer_class = ArbitratorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoachList(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AthleteList(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SupporterList(generics.ListCreateAPIView):
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SupporterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]