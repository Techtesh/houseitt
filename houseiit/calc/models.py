from django.db import models

# Create your models here.
#no commas.......snhhh
class primaryform(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    type_of_lease=models.CharField(max_length=20)
    rent=models.IntegerField(default=0)
    nego1=models.BooleanField(default=False)
    deposit=models.IntegerField(default=0)
    nego2=models.BooleanField(default=False)
    type_of_students=models.CharField(max_length=20)
    restrictions=models.BooleanField(default=False)
    
    
class subform_curfew(models.Model):
    main_id=models.ForeignKey("primaryform",on_delete=models.CASCADE) #(primaryform.id),
    curfew_time=models.TimeField(auto_now=False, auto_now_add=False)
    no_of_students=models.IntegerField(default=1)
    student_gender= models.CharField(max_length=10)
    
class subform_amenities(models.Model):
    main_id=models.ForeignKey(primaryform,on_delete=models.CASCADE)
    isDining=models.BooleanField(default=False)
    isFurnished=models.BooleanField(default=False)
    noparking=models.IntegerField(default=0)
    no1cupboards=models.IntegerField()
    iswater_puri=models.BooleanField(default=False)
    isAC=models.BooleanField(default=False)
    noBeds=models.IntegerField()
    isWashing_machine=models.BooleanField(default=False)
    isTV=models.BooleanField(default=False)
    isgeyser=models.BooleanField(default=False)
    isPower=models.BooleanField(default=False)
    isPower_bckup=models.BooleanField(default=False)
    iskitchen=models.BooleanField(default=False)
    ismicrowave=models.BooleanField(default=False)
    
class subform_restrictions(models.Model):
    main_id=models.ForeignKey(primaryform,on_delete=models.CASCADE)
    Drinking=models.BooleanField(default=False)
    Smoking=models.BooleanField(default=False)
    Pets=models.BooleanField(default=False)
    Music=models.BooleanField(default=False)
    Guests=models.BooleanField(default=False)
    