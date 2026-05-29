# {{ title }}
**Author**: {{ author }}

{% for highlight in highlights %}
> {{ highlight.text }} (Page {{ highlight.page }})
{% endfor %}