class Widget: 

    def semicolon(self, widget):
        widget = widget.replace(' ', '').replace('\n', '').replace('\r', '')

        if widget[-2:] == "))":
            return ';'
        
        return ''
