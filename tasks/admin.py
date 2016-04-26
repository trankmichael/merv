from django.contrib import admin
from .models import Task
from django.http import HttpResponse

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Task Name"),
        smart_str(u"Collaborative"),
        smart_str(u"Strength"),
        smart_str(u"Travel"),
        smart_str(u"Outdoor"),
        smart_str(u"Language"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.task_name),
            smart_str(obj.collaborative),
            smart_str(obj.strength),
            smart_str(obj.outdoor),  
            smart_str(obj.language),            
        ])
    return response
export_csv.short_description = u"Export CSV"


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','task_name', 'collaborative','strength','transportation','outdoor','language')
    actions = [export_csv]


admin.site.register(Task, TaskAdmin)