from.models import Category, Publication, Hashtag
from modeltranslation.translator import TranslationOptions, register
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
@register(Hashtag)
class HashtagTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Publication)
class PublicationTranslaionOptions(TranslationOptions):
    fields = ('title', 'description',)