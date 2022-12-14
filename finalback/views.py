from cgi import print_form
import profile
from django.http.response import HttpResponseNotAllowed

from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.shortcuts import render


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
    role,
    Categorie,
    Grade,
    Licences,
    Weights,
    Seasons,

)
from .serializers import  (
    ArbitratorSerializer,
    CoachSerializer,
    AthleteSerializer,
    ClubSerializer,
    ProfileSerializer,
    RegisterSerializer,
    RoleSerializer,
    SupporterSerializer,
    UserSerializer,
    CategorieSerializer,
    LicencesSerializer,
    GradeSerializer,
    SeasonsSerializer,
    WeightSerializer

)
#exel
import xlwt
import csv

from django.http import HttpResponse
from django.contrib.auth.models import User

def serialize_user(user):
    return {
        "id":user.id,
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
                "id":user.id,
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

# csv
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response
#exel
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategorieList(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategorieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LicencesList(generics.ListCreateAPIView):
    queryset = Licences.objects.all()
    serializer_class = LicencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LicencesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Licences.objects.all()
    serializer_class = LicencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeasonsList(generics.ListCreateAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SeasonsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WeightsList(generics.ListCreateAPIView):
    queryset = Weights.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WeightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weights.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



@csrf_exempt
def pro_list(request):
    """
    List all code snippets, or create a new Profile.
    """
    if request.method == 'GET':
        userb =User.objects.all()
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles , many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def user_info(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    # username = self.kwargs['username']
    # username=int(request.user)
    # return Profile.objects.filter(user=username)
    # try:
        
    #     pro = Profile.objects.filter(user_id=pk)
    # except Profile.DoesNotExist:
    #     return HttpResponse(status=404)

    # if request.method == 'GET':
        
    #     serializer = ProfileSerializer(pro)
    #     return JsonResponse(serializer.data)

    if request.method == 'GET':
        
        
        user = User.objects.filter(id=pk)
        userserializer = UserSerializer(user, many=True)
        ok=False
        profile = Profile.objects.all()
        for p in profile:
            print(p.user)
            
            if(p.user.pk==pk): 

                print('a')
            
                profileserializer = ProfileSerializer(p, many=False)
                # info.append(userserializer.data)
                info=profileserializer.data
                ok=True
                break
        if ok:

         return JsonResponse(info, safe=False)
        else :
            return JsonResponse([], safe=False)
        
