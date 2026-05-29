# {{ title }}

> **Author**: {{ author }}
> **Location**: {{ highlights[0].location if highlights else "?" }}

## Highlights
{% for highlight in highlights %}
- {{ highlight.text }} *(Page {{ highlight.page }})*
{% endfor %}