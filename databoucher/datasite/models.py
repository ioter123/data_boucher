from django.db import models

# Create your models here.


class Data(models.Model):
    base_ym = models.IntegerField()
    kywrd_nm = models.CharField(max_length=200)
    rnk = models.IntegerField()
    agegrd_5_unit_nm = models.CharField(max_length=200)
    sex_type_nm = models.CharField(max_length=200)
    dow_nm = models.CharField(max_length=200)
    wday_eweek_div_nm = models.CharField(max_length=200)
    timezn_cd = models.IntegerField()
    sido_nm = models.CharField(max_length=200)
    sgg_nm = models.CharField(max_length=200)
    main_sojn_site_nm = models.CharField(max_length=200)
    main_sojn_url = models.CharField(max_length=200)
    prmr_ctgry_ctg_nm = models.CharField(max_length=200)
    daytm_sido_nm = models.CharField(max_length=200)
    daytm_sgg_nm = models.CharField(max_length=200)
    night_sido_nm = models.CharField(max_length=200)
    night_sgg_nm = models.CharField(max_length=200)

    class Meta:
        db_table = 'data'



