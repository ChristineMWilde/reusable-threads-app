=====
Threads
=====
 
Threads is a reusable forum app for Django with the Motorholic project formatting
 
Detailed documentation is in the "ProjectDocumentation" directory.
 
Quick start
-----------
 
1. Add 'reusable_threads' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'reusable_threads',
    )
 
2. Include the threads URLconf for your project forum page in the urls.py like this::
 
    url(r'^threads/', include('reusable_threads.urls')),
 
3. Run `python manage.py migrate` to create the threads models.
 
4. Add the threads css::
    <link rel="stylesheet" href="{% static "css/mechanic.css" %}">

5. Add the brand image::
    <link rel="stylesheet" href="{% static "images/logo.jpg" %}">

6. Add the custom js file::
    <link rel="stylesheet" href="{% static "js/myScript.js" %}">

7. Ensure you have the templatetags folder for filtering

8. In order to use the "voting feature" please download the polls app to use in conjunction with the threads app. Download link:

9. Add a link to the threads in the base.html
	<li><a href="/threads/">Our Forum</a></li>
 
8. Visit http://127.0.0.1:8000/forum/ to view the blogs you create.