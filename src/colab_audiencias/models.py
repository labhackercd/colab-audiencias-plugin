from django.db import models
from django.conf import settings
from colab.plugins import helpers


class AudienciasVideo(models.Model):
    id = models.IntegerField(primary_key=True)
    videoId = models.CharField(max_length=200, unique=True)
    thumb_default = models.URLField(null=True, blank=True)
    thumb_medium = models.URLField(null=True, blank=True)
    thumb_high = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def get_url(self):
        prefix = helpers.get_plugin_prefix('colab_audiencias', regex=False)
        return '/{}sala/{}'.format(prefix, self.id)

    def questions_count(self):
        return self.questions.all().count()


class AudienciasAgenda(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True)
    session = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    situation = models.CharField(max_length=200, null=True, blank=True)
    commission = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)


class AudienciasQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    video = models.ForeignKey(AudienciasVideo, related_name='questions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.TextField()
    answer_time = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
