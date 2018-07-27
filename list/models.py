from django.db import models
import uuid # Required for unique id in each row

class listModel(models.Model):
    """A Class for name-email list Data"""

    # Fields
    lst_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='id')
    lst_name = models.CharField(max_length=81, verbose_name='Name', help_text='To store each person name')
    lst_email = models.EmailField(max_length=81, verbose_name='Email', help_text='To store each person email')

    # Metadata
    class Meta: 
        ordering = ['lst_name']

    # Methods
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.field_name