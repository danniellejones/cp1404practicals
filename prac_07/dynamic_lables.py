"""
CP1404 | Prac_07 | Dannielle Jones
Dynamic labels app.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to create dynamic labels."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # List of names
        self.names = ["Jane", "Bobby", "Westley", "Peter"]

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from names list and add to GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
