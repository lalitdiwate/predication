from django.db import models

class clg_list(models.Model):
    # number = models.IntegerField() 
    name = models.CharField(max_length = 50)
    id=models.IntegerField(primary_key=True,null=False)

    

    class Meta:
        managed=True
        db_table = "clg_list"

    def __str__(self):
        return "%s %s" % (self.name, self.id)


   

# class cuttoff(models.Model):
# 	name = models.CharField(max_length = 50)
# 	fcutt = models.IntegerField()
# 	scutt = models.IntegerField()
# 	tcutt = models.IntegerField()
# 	ficutt = models.IntegerField()
# 	scutt = models.IntegerField()
# 	class Meta:
# 		db_table = "cuttoff"

class tfws_clg_list(models.Model):
    # number = models.IntegerField() 
    clg_name=models.ForeignKey('clg_list',on_delete=models.CASCADE,null=False)
    course_name=models.CharField(max_length = 50)
    intake=models.IntegerField(null=True,blank=True)

    class Meta:
    	managed=True
    	db_table = "tfws_clg_list"

# class sample(models.Model):
#     # number = models.IntegerField() 
#     clg_name=models.ForeignKey('clg_list',on_delete=models.CASCADE,null=False)
#     course_name=models.CharField(max_length = 50)
#     intake=models.IntegerField(null=True,blank=True)

#     class Meta:
#     	managed=True
#     	db_table = "sample"

class cutt_offs(models.Model):
	name = models.CharField(max_length = 50)
	fcutt = models.IntegerField()
	scutt = models.IntegerField()
	tcutt = models.IntegerField()
	ficutt = models.IntegerField()
	scutt = models.IntegerField()
	class Meta:
		db_table = "cutt_offs"



class sipna_direct_cutt_offs(models.Model):
	seat_type = models.CharField(max_length = 50)
	GOPEN = models.IntegerField(null=True,blank=True)
	LOPEN = models.IntegerField(null=True,blank=True)
	GOBC = models.IntegerField(null=True,blank=True)
	GSC = models.IntegerField(null=True,blank=True)
	GST = models.IntegerField(null=True,blank=True)
	GNTA = models.IntegerField(null=True,blank=True)
	LNTA = models.IntegerField(null=True,blank=True)
	GNTD = models.IntegerField(null=True,blank=True)
	LNTC = models.IntegerField(null=True,blank=True)
	DEF = models.IntegerField(null=True,blank=True)
	PHC = models.IntegerField(null=True,blank=True)
	OPEN = models.IntegerField(null=True,blank=True)
	GNTB = models.IntegerField(null=True,blank=True)
	LSC = models.IntegerField(null=True,blank=True)
	LVJDT = models.IntegerField(null=True,blank=True)
	GVJDT = models.IntegerField(null=True,blank=True)
	
	class Meta:
		managed=True
		db_table = "sipna_direct_cutt_offs"


# class cuttoff(models.Model):
# 	clg_id=models.IntegerField(null=True,blank=True)
# 	branch=models.CharField(max_length=100)

# 	per_13=models.IntegerField(null=True,blank=True)
# 	per_15=models.IntegerField(null=True,blank=True)
# 	per_16=models.IntegerField(null=True,blank=True)
# 	per_17=models.IntegerField(null=True,blank=True)
# 	per_18=models.IntegerField(null=True,blank=True)
# 	cuttoff=models.IntegerField(null=True,blank=True)

# 	class Meta:
# 		db_table = "cuttoff"


class predict_table(models.Model):
	clg_id=models.IntegerField(null=True,blank=True)
	branch=models.CharField(max_length=100)
	cate=models.CharField(max_length=100)
	per_13=models.IntegerField(null=True,blank=True)
	per_15=models.IntegerField(null=True,blank=True)
	per_16=models.IntegerField(null=True,blank=True)
	per_17=models.IntegerField(null=True,blank=True)
	per_18=models.IntegerField(null=True,blank=True)
	cuttoff=models.IntegerField(null=True,blank=True)

	class Meta:
		managed=True
		db_table = "predict_table"


class first_predict_table(models.Model):
	clg_id=models.IntegerField(null=True,blank=True)
	branch=models.CharField(max_length=100)
	cate=models.CharField(max_length=100)
	per_13=models.IntegerField(null=True,blank=True)
	per_15=models.IntegerField(null=True,blank=True)
	per_16=models.IntegerField(null=True,blank=True)
	per_17=models.IntegerField(null=True,blank=True)
	per_18=models.IntegerField(null=True,blank=True)
	cuttoff=models.IntegerField(null=True,blank=True)

	class Meta:
		managed=True
		db_table = "first_predict_table"

# class pcutt(models.Model):
# 	clg_id=models.IntegerField(null=True,blank=True)
# 	branch=models.CharField(max_length=100)
	
# 	per_13=models.IntegerField(null=True,blank=True)
# 	per_15=models.IntegerField(null=True,blank=True)
# 	per_16=models.IntegerField(null=True,blank=True)
# 	per_17=models.IntegerField(null=True,blank=True)
# 	per_18=models.IntegerField(null=True,blank=True)
# 	cuttoff=models.IntegerField(null=True,blank=True)

# 	class Meta:
# 		db_table = "pcutt"