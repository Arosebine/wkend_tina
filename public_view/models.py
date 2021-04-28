from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.

class Agents(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Agent')
    phone = models.CharField(max_length=17)
    website = models.URLField(blank=True, null=True)
    profile = models.FileField(blank=True, null=True, upload_to='uploads/profile')
    biography = models.TextField()
    address = models.TextField()

    class Meta():
        verbose_name_plural='Agent'

class Location(models.Model):
    name =models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    RENT = 'Rent'
    SALE = 'Sale'
    CHOOSE = ''
    OFFER_TYPE = [
        (RENT, 'Rent'),
        (SALE, 'Sale'),
        (CHOOSE, 'Choose An Offer Type'),
    ]
    property_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    property_img1 = models.FileField(blank=True, null=True, verbose_name='Property Image 1', upload_to='uploads/properties')
    property_img2 = models.FileField(blank=True, null=True, verbose_name='Property Image 2', upload_to='uploads/properties')
    property_img3 = models.FileField(
        blank=True, null=True, verbose_name='Property Image 3', upload_to='uploads/properties')
    property_address = models.TextField(blank=True, null=True)
    property_description = models.TextField(blank=True, null=True)
    rooms = models.PositiveIntegerField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE, default=CHOOSE)
    location_id = models.ForeignKey(Location, related_name='property_location', on_delete=models.CASCADE)
    agent_id = models.ForeignKey(User, related_name='property_agent', on_delete=models.CASCADE)
    property_type_id = models.ForeignKey(
        PropertyType, related_name='property_type', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    approve = models.BooleanField(default=False)

    def property_img_url1(self):
        if self.property_img1:
            return self.property_img1.url
        else:
            return '/public/images/hero_bg_1.jpg'

    def property_img_url2(self):
        if self.property_img2:
            return self.property_img2.url
        else:
            return '/public/images/hero_bg_1.jpg'

    def property_img_url3(self):
        if self.property_img3:
            return self.property_img3.url
        else:
            return '/public/images/hero_bg_1.jpg'


    def __str__(self):
        return self.property_name

    class Meta():
        verbose_name_plural = 'Property'

    def approve_property(self):
        self.approve = True
        self.save()
    
    def disapprove_property(self):
        self.approve = False
        self.save()

    def get_property_url(self):
        return reverse('public_view:property_details', kwargs={'slug':self.slug})


class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100, blank=True, null=True)
    profile = models.FileField(blank=True, null=True, upload_to='uploads/propfile/')
    biography = models.TextField()

    def __str__(self):
        return self.name

    def profile_url(self):
        if self.profile:
            return self.profile.url
        else:
            return '/public/images/person_1.jpg'


class ContactAgent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(default='mail@gmail.com',)
    agent_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





