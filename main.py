from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label

import client


def change_text(label, period):
    message = client.message_checker()
    if message:
        if 'ПОВІТРЯНА ТРИВОГА' in message:
            label.text = message
            sound = SoundLoader.load('Sound.mp3')
            sound.play()
        elif 'ВІДБІЙ ПОВІТРЯНОЇ ТРИВОГИ' in message:
            label.text = message

    Clock.schedule_once(lambda _: change_text(label, period), period)


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        change_text(label, period=60)
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()
