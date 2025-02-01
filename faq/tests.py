# faq/tests.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_get_translation_method():
    """
    Test that get_translation returns a string and falls back to English if needed.
    """
    faq = FAQ.objects.create(question="Hello", answer="World")
    # Attempt to fetch translation for Hindi
    translated_question = faq.get_translation('question', lang='hi')
    assert isinstance(translated_question, str)
    # If translation fails, it should return the original English text
    if translated_question == faq.question:
        assert faq.question == "Hello"
    else:
        assert translated_question != ""

@pytest.mark.django_db
def test_api_faq_list():
    """
    Test the FAQ list API endpoint with language selection.
    """
    FAQ.objects.create(question="Test", answer="Answer")
    client = APIClient()
    url = reverse('faq-list')  # Provided by the DefaultRouter
    response = client.get(url, {'lang': 'en'})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Check that the FAQ in response has the proper keys
    faq_data = data[0]
    assert 'question' in faq_data
    assert 'answer' in faq_data
