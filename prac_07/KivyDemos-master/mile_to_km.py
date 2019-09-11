from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.60934

class MileToKm(App):
    message = StringProperty()

    def build(self):
        Window.size = (550, 250)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('mile_to_km_frame.kv')
        return self.root

    def handle_calculation(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.message = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(value)
        # self.handle_calculation()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


# create and start the App running
MileToKm().run()