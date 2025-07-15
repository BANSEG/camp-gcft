from django.db import models
import random, string

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract =True

class Floor(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Hall(BaseModel):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class BedSpace(BaseModel):
    name = models.CharField(max_length=150)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    number_of_beds = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class Program(BaseModel):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year
    


class Applicants(BaseModel):
    year = models.ForeignKey(Program, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=16, unique=True)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    marital_status = models.CharField(max_length=20)
    num_children_below_10 = models.PositiveIntegerField(default=0)
    names_of_children = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    arrival_date = models.DateField()
    disability_or_allergy = models.TextField(blank=True, null=True)
    local_assembly = models.CharField(max_length=150)
    local_assembly_address = models.TextField()
    bed_space = models.ForeignKey("BedSpace", on_delete=models.SET_NULL, null=True, blank=True)  # 🔥 New field
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            suffix = self.year.year if self.year else "XXXX"
            self.code = ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + suffix

        if not self.bed_space:
            # Find any available BedSpace not already assigned to another applicant
            taken_beds = Applicants.objects.exclude(bed_space=None).values_list('bed_space_id', flat=True)
            available_beds = BedSpace.objects.exclude(id__in=taken_beds)

            if available_beds.exists():
                self.bed_space = random.choice(available_beds)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname
