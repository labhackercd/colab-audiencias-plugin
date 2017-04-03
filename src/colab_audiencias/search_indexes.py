from haystack import indexes
from colab_audiencias import models


class AudienciasRoomIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True,
                                  stored=False)
    type = indexes.EdgeNgramField()

    # Model fields
    legislative_body_alias = indexes.EdgeNgramField(
        model_attr='legislative_body_alias')
    youtube_status = indexes.EdgeNgramField(model_attr='youtube_status')
    youtube_id = indexes.EdgeNgramField(model_attr='youtube_id')
    cod_reunion = indexes.EdgeNgramField(model_attr='cod_reunion')
    online_users = indexes.EdgeNgramField(model_attr='online_users')
    max_online_users = indexes.EdgeNgramField(model_attr='max_online_users')
    url = indexes.EdgeNgramField(model_attr='get_url')

    def get_model(self):
        return models.AudienciasRoom

    def prepare_type(self, obj):
        return u'video'

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
