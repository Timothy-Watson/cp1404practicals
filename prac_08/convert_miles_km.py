from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKM(App):
    """The main app."""
    output_label = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Miles To Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        """Increment input box by value."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)

    def handle_calculate(self):
        """Handle the calculation from miles to kilometers."""
        miles = self.get_valid_miles()
        kilometers = miles * MILES_TO_KM
        self.output_label = str(kilometers)

    def get_valid_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


MilesToKM().run()
