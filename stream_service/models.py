from django.db import models
from django.utils import timezone

####
# SOURCE: STREAMABLE
####
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
        self.view_count = view_count
        self.date_of_update = timezone.now()
        self.save()

    def should_update_view_count(self):
        current_min = int((timezone.now()).strftime("%M"))
        updated_min = int(self.date_of_update.strftime("%M"))
        time_delta = current_min - updated_min
        return time_delta < 0 or time_delta >= 15

    def __str__(self):
        return "%s(%s) - %s" % (self.title, self.performer_name, self.name_in_code)


class ShowInfo(models.Model):
    title = models.CharField(max_length=100)
    title_in_japanese = models.CharField(max_length=30, default="なし")

    small_info = models.CharField(max_length=100, default="Enter added info")

    # The name used in urls and cloudinary img files
    name_in_code = models.CharField(max_length=50)

    is_disabled = models.BooleanField(default=False)

    #num_episodes = models.IntegerField(default=0) // Use django count instead

    # Date published
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return "%s(%s)" % (self.title, self.name_in_code)

####
# SOURCE: DAILYMOTION
####
class ShowEpisode(models.Model):
    title = models.CharField(max_length=100)
    
    show = models.ForeignKey(ShowInfo, on_delete=models.CASCADE, default='1', related_name='episodes')

    # Link for dailymotion
    embed_link = models.CharField(max_length=350, default="Enter embed link here")

    is_disabled = models.BooleanField(default=False)

    video_duration = models.CharField(max_length=8, default="00:00:00")

    # Date published
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    # Date of update
    date_of_update = models.DateTimeField(blank=True, null=True, editable=True, default=timezone.now)

    def __str__(self):
        return "%s" % (self.title)
