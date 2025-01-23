from django.contrib import admin
from django.urls.resolvers import URLPattern
from .models import CourseOutcome,Attainment,Course,Subject,CalculateExcel
# Register your models here.
from django.utils.html import format_html
admin.site.site_header = 'COPO'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('name',
#                     'course',
#                     'semester',
#                     )

class AttainmentAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'IA_1',
                    'IA_2',
                    'Assignment',
                    'ESE',
                    )

class CourseOutcomeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'per1',
                    'per2',
                    'per3',
                    'per4',
                    )
class CalculateExcelAdmin(admin.ModelAdmin):
    def get_urls(self) -> list[URLPattern]:
        return super().get_urls()
    
    def view(self,obj):
        return format_html( '''<a class="btn btn-info btn-sm" href = "/view/{}">view</a>'''.format(obj.id))

    list_display = (
        'subject',
        'type',
        'semester',
        'attainment',
        'courseOutCome',
        'file',
        'view'        
    )
    
    list_filter = [
        'subject',
        'type',
        'semester'
    ]
    
from django.contrib import admin
from .models import Department, Teacher, Class, Subject, Student

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hod')  # Display department name and HOD in admin panel
    search_fields = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'user_type')  # Show ID, name, and user type
    list_filter = ('user_type',)  # Filter by user type
    search_fields = ('teacher_id', 'name')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('department', 'batch', 'division')  # Show related department, batch, and division
    list_filter = ('department', 'division')  # Filter by department and division
    search_fields = ('batch',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_assigned', 'teacher')  # Show subject name, class, and teacher
    list_filter = ('class_assigned', 'teacher')  # Filter by class and teacher
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'enrollment_id', 'student_class')  # Display student info
    list_filter = ('student_class',)  # Filter by class
    search_fields = ('name', 'roll_no', 'enrollment_id')


admin.site.register(Attainment, AttainmentAdmin)
admin.site.register(CourseOutcome, CourseOutcomeAdmin)
admin.site.register(Course, CourseAdmin)
# admin.site.register(Subject, SubjectAdmin)
admin.site.register(CalculateExcel, CalculateExcelAdmin)

