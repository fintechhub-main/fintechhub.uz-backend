from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    CourseDescriptionViewSet,
    CourseIconViewSet,
    LoginView,
    TeacherViewSet,
    PartnerViewSet,
    BannerImageViewSet,
    CourseDescriptionGroupView,
    FAQViewSet,
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"course-descriptions", CourseDescriptionViewSet)
router.register(r"course-icons", CourseIconViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"partners", PartnerViewSet)
router.register(r"banners", BannerImageViewSet)
router.register(r"course-description-groups", CourseDescriptionGroupView)
router.register(r"faqs", FAQViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
]
