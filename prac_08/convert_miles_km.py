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
        value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(value)

    def handle_calculate(self):
        """Handle the calculation from miles to kilometers."""
        miles = float(self.root.ids.input_miles.text)
        kilometers = miles * MILES_TO_KM
        self.output_label = str(kilometers)


MilesToKM().run()
