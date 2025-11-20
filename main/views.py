from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import (
    Course,
    Teacher,
    Partner,
    BannerImage,
    CourseDescription,
    CourseIcon,
    CourseDescriptionGroup,
    FAQ,
)
from .serializers import (
    CourseSerializer,
    TeacherSerializer,
    PartnerSerializer,
    BannerImageSerializer,
    CourseDescriptionSerializer,
    CourseIconSerializer,
    CourseDescriptionGroupSerializer,
    CourseDetailSerializer,
    LoginSerializer,
    FAQSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer


class CourseDescriptionGroupView(viewsets.ModelViewSet):
    queryset = CourseDescriptionGroup.objects.all()
    serializer_class = CourseDescriptionGroupSerializer
    permission_classes = [IsAdminOrReadOnly]


class CourseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = CourseDescription.objects.all()
    serializer_class = CourseDescriptionSerializer
    permission_classes = [IsAdminOrReadOnly]


class CourseIconViewSet(viewsets.ModelViewSet):
    queryset = CourseIcon.objects.all()
    serializer_class = CourseIconSerializer
    permission_classes = [IsAdminOrReadOnly]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAdminOrReadOnly]


class BannerImageViewSet(viewsets.ModelViewSet):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer
    permission_classes = [IsAdminOrReadOnly]


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {"token": token.key, "username": user.username, "is_admin": user.is_staff},
            status=status.HTTP_200_OK,
        )


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAdminOrReadOnly]
