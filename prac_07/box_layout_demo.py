"""CP1404 | Prac_07 | Dannielle Jones
Modified box layout demo program."""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        print("clear")
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
