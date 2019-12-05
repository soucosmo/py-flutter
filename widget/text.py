from .widget import Widget


class Text(Widget):

    def __init__(self, text = '', style = {}):

        self._style_generate(style)

        self._widget = f"Text('{text}', textDirection: TextDirection.ltr)"


    def _style_generate(self, style = {}):
        self._style = {
            'color': f"Colors.{style.get('color', '')}"
        }

    def __str__(self):
        return self._widget
