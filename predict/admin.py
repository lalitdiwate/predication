
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import clg_list,tfws_clg_list,sipna_direct_cutt_offs,predict_table,first_predict_table
@admin.register(clg_list)
class clgAdmin(ImportExportModelAdmin):
    pass


@admin.register(first_predict_table)
class first_predict_tableAdmin(ImportExportModelAdmin):
    pass
# @admin.register(data)
# class dataAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(sample)
# class sample(ImportExportModelAdmin):
#     pass

# @admin.register(cuttoff)
# class cuttoffAdmin(ImportExportModelAdmin):
#     pass

@admin.register(predict_table)
class predict_tableAdmin(ImportExportModelAdmin):
    pass

@admin.register(tfws_clg_list)
class tfws_clgAdmin(ImportExportModelAdmin):
    pass


# @admin.register(cutt_offs)
# class cutt_offsAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(direct_cutt_offs)
# class direct_cutt_offsAdmin(ImportExportModelAdmin):
#     pass


@admin.register(sipna_direct_cutt_offs)
class sipna_direct_cutt_offsAdmin(ImportExportModelAdmin):
    pass

