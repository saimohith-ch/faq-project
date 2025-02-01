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
  
  1.**Clone the repository:**
  ```bash
     git clone https://github.com/saimohith-ch/faq-project.git
  ```
  2. Create a virtual environment:
  ```bash
     python -m venv env
  ```
  3. Activate the virtual environment:
     **On Windows:
       ```bash
          .\env\Scripts\activate
       ```
     **On macOS/Linux:
        ```bash
           source env/bin/activate
        ```
  4. Install the dependencies:
  ```bash
     pip install -r requirements.txt
  ```
  5. Apply database migrations:
  ```bash
     python manage.py migrate
  ```
  6. Create a superuser for admin access:
  ```bash
     python manage.py createsuperuser
  ```
  7. Run the development server:
  ```bash
     python manage.py runserver
  ```
 8. Visit the API and Admin Panel:
    **API Endpoint: http://127.0.0.1:8000/api/faqs/
    **Admin Panel: http://127.0.0.1:8000/admin/
###API Endpoints
##Fetch FAQs in Different Languages
  **GET /api/faqs/?lang=hi: Fetches all the FAQs in Hindi (using the lang query parameter; 
    defaults to English if not provided).
Example Requests:
```
  #Fetch FAQs in English (default)
   curl http://127.0.0.1:8000/api/faqs/
  #Fetch FAQs in Hindi:
   curl http://127.0.0.1:8000/api/faqs/?lang=hi
  #Fetch FAQs in Bengali:
    curl http://127.0.0.1:8000/api/faqs/?lang=bn
```
###Contribution Guidelines
1.Fork the repository and clone it locally.
2.Create a new branch with a descriptive name.
3.Make your changes following PEP8 guidelines.
4.Test your changes before committing.
5.Use clear and meaningful commit messages.
6.Push your changes and create a pull request.
  


