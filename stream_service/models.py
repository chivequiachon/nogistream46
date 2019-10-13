from django.db import models
from django.utils import timezone

class MvInfo(models.Model):
    title = models.CharField(max_length=100)
    performer_name = models.CharField(max_length=50)
    description = models.TextField()

    # The name used in urls and cloudinary img files
    name_in_code = models.CharField(max_length=50)

    # ID for streamable
    mv_id = models.CharField(max_length=15, default="Enter ID here")

    # Link for streamable
    embed_link = models.CharField(max_length=350, default="Enter embed link here")

    view_count = None

    is_disabled = models.BooleanField(default=False)

    # Date published
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s(%s) - %s" % (self.title, self.performer_name, self.name_in_code)