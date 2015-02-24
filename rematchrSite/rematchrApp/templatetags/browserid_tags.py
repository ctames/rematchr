
{% load browserid %}
<html>
  <head>
    <link rel="stylesheet" href="{% static 'browserid/persona-buttons.css' %}">
  </head>
  <body>
    {% browserid_info %}
    {% if user.is_authenticated %}
      <p>Current user: {{ user.email }}</p>
      {% browserid_logout text='Logout' %}
    {% else %}
      {% browserid_login text='Login' color='dark' %}
    {% endif %}

    <script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="https://login.persona.org/include.js"></script>
    <script src="{% static 'browserid/api.js' %}"></script>
    <script src="{% static 'browserid/browserid.js' %}"></script>
  </body>
</html>
