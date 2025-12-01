from django.contrib import admin
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

# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Partner)
admin.site.register(BannerImage)
admin.site.register(CourseDescription)
admin.site.register(CourseIcon)
admin.site.register(FAQ)
admin.site.register(CourseDescriptionGroup)
