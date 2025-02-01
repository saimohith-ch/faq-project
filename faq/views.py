# faq/views.py
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FAQs to be viewed or edited.
    Language selection is supported via the ?lang= query parameter.
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
