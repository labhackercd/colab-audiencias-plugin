from django.db import models
from django.conf import settings
from colab.plugins import helpers


class AudienciasRoom(models.Model):
    YOUTUBE_STATUS_CHOICES = (
        (0, 'Sem transmissão'),
        (1, 'Em andamento'),
        (2, 'Transmissão encerrada')
    )
    id = models.IntegerField(primary_key=True)
    cod_reunion = models.CharField(max_length=200, null=True, blank=True)
    online_users = models.IntegerField(default=0)
    max_online_users = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
    legislative_body_alias = models.CharField(max_length=200, null=True,
                                              blank=True)
    youtube_status = models.IntegerField(choices=YOUTUBE_STATUS_CHOICES,
                                         default=0)
    youtube_id = models.CharField(max_length=200, null=True, blank=True)

    def get_url(self):
        prefix = helpers.get_plugin_prefix('colab_audiencias', regex=False)
        return '/{}sala/{}'.format(prefix, self.id)

    def questions_count(self):
        return self.questions.all().count()


class AudienciasQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.ForeignKey(AudienciasRoom, related_name='questions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.TextField()
    answer_time = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
