from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return "%s" % self.first_name

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Policy(models.Model):
    PERSONAL_ACCIDENT = 'personal-accident'
    TYPES = ((PERSONAL_ACCIDENT, "Personal Accident"),)

    # type = models.CharField(max_length=100)
    type = models.CharField(choices=TYPES, max_length=50)
    premium = models.IntegerField()
    cover = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='customers', null=True, on_delete=models.SET_NULL)

    def  __str__(self):
        return "%s" % self.get_type_display()

