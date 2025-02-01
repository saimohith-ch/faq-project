# faq-project
This is a simple Django-based FAQ system that supports multiple languages for questions and answers. It uses Django REST framework to expose an API to fetch FAQ data. Additionally, the FAQ model automatically translates the questions and answers into multiple languages (Hindi, Bengali) if not already provided.

## Features
- **Multi-language Support:** Fetch FAQs in English, Hindi, and Bengali.
- **API Endpoint:** `GET /api/faqs/` to retrieve the list of FAQs.
- **Database Caching:** Frequently fetched data is cached to improve performance.

### Prerequisites
- Python 3.x
- Django 5.1+
- Django REST framework
- Google Translate API or the `googletrans` library (you may need to install this manually)
- Redis (for caching)

  ### Steps to Run Locally
  **Clone the repository:**
      
