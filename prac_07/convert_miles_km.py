"""
CP1404 | Prac_07 | Dannielle Jones
Convert miles to kilometres.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = "Dannielle Jones"

ONE_MILE_IN_KM = 1.60934


class ConvertMilesToKm(App):
    """ConvertMilesToKm is a Kivy App to convert miles to kilometres."""
    result_in_km = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result_in_km = ""
        return self.root

    def handle_conversion(self):
        """Convert miles to kilometres."""
        value = self.get_validated_miles()
        result = value * ONE_MILE_IN_KM
        self.result_in_km = str(result)

    def handle_increment(self, increment):
        """Reduce or increase input value."""
        increment_result = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(increment_result)
        self.handle_conversion()

    def get_validated_miles(self):
        """Get text input from widget, convert to float or if error return 0."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


# Create and start app
ConvertMilesToKm().run()
