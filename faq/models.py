from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    # Default English fields
    question = models.TextField(help_text="Question in English")
    answer = RichTextField(help_text="Answer in English")

    # Example additional language fields (Hindi, Bengali)
    question_hi = models.TextField(blank=True, null=True, help_text="Question in Hindi")
    answer_hi = RichTextField(blank=True, null=True, help_text="Answer in Hindi")
    question_bn = models.TextField(blank=True, null=True, help_text="Question in Bengali")
    answer_bn = RichTextField(blank=True, null=True, help_text="Answer in Bengali")

    def __str__(self):
        return self.question

    def get_translation(self, field, lang='en'):
        """
        Return the translation for the given field ('question' or 'answer') and language.
        Uses cache and falls back to auto-translation via googletrans if no manual translation exists.
        """
        # If English, return default value
        if lang == 'en':
            return getattr(self, field)
        
        # Construct cache key
        cache_key = f"faq_{self.id}_{field}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        # Check if we have a manually set translation field
        attr_name = f"{field}_{lang}"
        manual_translation = getattr(self, attr_name, None)
        if manual_translation:
            cache.set(cache_key, manual_translation, timeout=3600)
            return manual_translation

        # Otherwise, perform auto-translation using googletrans.
        original_text = getattr(self, field)
        try:
            result = translator.translate(original_text, dest=lang)
            translated_text = result.text
        except Exception:
            # Fallback to original text in case of error
            translated_text = original_text

        cache.set(cache_key, translated_text, timeout=3600)
        return translated_text
