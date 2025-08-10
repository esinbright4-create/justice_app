from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class JusticeLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.label = Label(text="Justice AI Ready. Say something!", font_size=24)
        self.add_widget(self.label)

        self.input = TextInput(hint_text="Type your command here", multiline=False, font_size=20)
        self.add_widget(self.input)

        self.btn = Button(text="Send Command", font_size=22)
        self.btn.bind(on_press=self.process_command)
        self.add_widget(self.btn)

    def process_command(self, instance):
        command = self.input.text.lower()
        if "hello" in command:
            self.label.text = "Justice says: Hello Boss! How can I help you?"
        elif "time" in command:
            now = datetime.now().strftime("%H:%M:%S")
            self.label.text = f"Justice says: Current time is {now}"
        else:
            self.label.text = "Justice says: Sorry, I don't understand that command."
        self.input.text = ""

class JusticeApp(App):
    def build(self):
        return JusticeLayout()

if __name__ == "__main__":
    JusticeApp().run()