from django.contrib import admin
from django.urls.resolvers import URLPattern
from .models import CourseOutcome,Attainment,Course,Subject,CalculateExcel
# Register your models here.
from django.utils.html import format_html
admin.site.site_header = 'COPO'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'course',
                    'semester',
                    )

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
    
    

admin.site.register(Attainment, AttainmentAdmin)
admin.site.register(CourseOutcome, CourseOutcomeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(CalculateExcel, CalculateExcelAdmin)

