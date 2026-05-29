- {{ title }}
  author:: {{ author }}
  highlights::
  {% for highlight in highlights %}
  - {{ highlight.text }} (page:: {{ highlight.page }})
  {% endfor %}