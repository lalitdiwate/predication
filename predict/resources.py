from import_export import resources
from .models import clg_list,sipna_direct_cutt_offs,tfws_clg_list,predict_table,first_predict_table
class clg_listResource(resources.ModelResource):
    class Meta:
        model = clg_list

class first_predict_tableResource(resources.ModelResource):
    class Meta:
        model = first_predict_table
# class dataResource(resources.ModelResource):
#     class Meta:
#         model = data

# class cuttoffResource(resources.ModelResource):
#     class Meta:
#         model = cuttoff

# class sampleResource(resources.ModelResource):
#     class Meta:
#         model = sample

# class pcuttResource(resources.ModelResource):
#     class Meta:
#         model = pcutt

class tfws_clg_listResource(resources.ModelResource):
    class Meta:
        model = tfws_clg_list

class predict_tableResource(resources.ModelResource):
    class Meta:
        model = predict_table

# class cuttoff(resources.ModelResource):
#     class Meta:
#         model = cuttoff


# class cutt_offsResource(resources.ModelResource):
#     class Meta:
#         model = cutt_offs


# class direct_cutt_offsResource(resources.ModelResource):
#     class Meta:
#         model = direct_cutt_offs


class sipna_direct_cutt_offsResource(resources.ModelResource):
    class Meta:
        model = sipna_direct_cutt_offs