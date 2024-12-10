from .models import product,menu,serv,about,projectss,Us
from modeltranslation.translator import register, TranslationOptions

@register(product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'name2','but','but2')
    
@register(menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('home', 'contact','project','about','service','testimonial')
    
@register(serv)
class ServTranslationOptions(TranslationOptions):
    fields = ('servicee', 'text1','text11','text2','text22','text3','text33','text4','text44','read')
    
@register(about)
class AboutTranslationOptions(TranslationOptions):
    fields = ('a_me', 'read','ab_me')
    
@register(projectss)
class ProjectssTranslationOptions(TranslationOptions):
    fields = ('text', 'text1','text2','text3','text4','text5','text6')
    
@register(Us)
class UsTranslationOptions(TranslationOptions):
    fields = ('text', 'text1','text2','text3','text11','text22','text33')