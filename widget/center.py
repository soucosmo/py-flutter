from .widget import Widget


class Center(Widget):

    def __init__(self, widget):
        self._widget = f"Center(\n    child:{widget}\n)"

    def __str__(self):
        return self._widget + super().semicolon(self._widget)
        
