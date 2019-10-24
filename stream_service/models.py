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

    view_count = models.PositiveIntegerField(default=0)

    is_disabled = models.BooleanField(default=False)

    # Date published
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    # Date of update
    date_of_update = models.DateTimeField(blank=True, null=True, editable=True, default=timezone.now)


    def update_view_count(self, view_count):
        current_min = int((timezone.now()).strftime("%M"))
        updated_min = int(self.date_of_update.strftime("%M"))

        self.view_count = view_count
        time_delta = current_min - updated_min
        if time_delta < 0 or time_delta >= 15:
            self.date_of_update = timezone.now()
            self.save()

    def __str__(self):
        return "%s(%s) - %s" % (self.title, self.performer_name, self.name_in_code)