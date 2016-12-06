from haystack import indexes
from colab_audiencias import models


class AudienciasVideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True,
                                  stored=False)
    type = indexes.EdgeNgramField()

    # Model fields
    videoId = indexes.EdgeNgramField(model_attr='videoId')
    thumb_default = indexes.EdgeNgramField(
        model_attr='thumb_default', null=True)
    thumb_medium = indexes.EdgeNgramField(model_attr='thumb_medium', null=True)
    thumb_high = indexes.EdgeNgramField(model_attr='thumb_high', null=True)
    title = indexes.EdgeNgramField(model_attr='title')
    description = indexes.EdgeNgramField(model_attr='description')
    slug = indexes.EdgeNgramField(model_attr='slug', null=True)
    published_date = indexes.EdgeNgramField(model_attr='published_date')
    closed_date = indexes.EdgeNgramField(model_attr='closed_date', null=True)
    url = indexes.EdgeNgramField(model_attr='get_url')

    def get_model(self):
        return models.AudienciasVideo

    def prepare_type(self, obj):
        return u'video'

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
