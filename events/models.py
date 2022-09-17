from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify 


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, on_delete= models.CASCADE, null=True, related_name='children',)
    
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    capacity = models.IntegerField(("Venue Capacity"))
    parent = models.ForeignKey('self',blank=True, on_delete= models.CASCADE, null=True, related_name='children',)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Venue, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(("Event Title"), max_length=200)
    category = models.ForeignKey('Category', on_delete= models.CASCADE, null=False, blank=False,)
    start_date = models.DateField(("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(("End Date"), auto_now=False, auto_now_add=False)
    start_time = models.TimeField(("What time does it start?"), auto_now=False, auto_now_add=False)
    end_time = models.TimeField(("What time does it end?"), auto_now=False, auto_now_add=False)
    ticket_price = models.IntegerField(("How much is the ticket?"),)
    available_tickets = models.IntegerField(("Total tickets available")) 
    venue = models.ForeignKey('Venue', on_delete= models.CASCADE, null=False, blank=False,)
    description = RichTextField(("Event Description"))
    slug = models.SlugField(null=False, unique=True)
    published_date = models.DateField(auto_now_add=True,)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title