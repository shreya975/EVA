from core.state_manager import StateManager
from voice.text_to_speech import speak
from voice.speech_to_text import listen
from voice.wake_word import is_wake_word
from auth.voice_auth import authenticate_voice

class EVA:
    def __init__(self):
        self.state = StateManager()

    def boot(self):
        self.state.load_settings()
        self.state.load_permissions()

        speak("Initializing systems.")

        if authenticate_voice():
            speak("Authentication successful.")
            speak("EVA online.")
            self.state.set_active(True)
            self.idle_loop()
        else:
            speak("Authentication failed. Access denied.")

    def idle_loop(self):
        speak("Standing by.")

        while True:
            text = listen()
            if not text:
                continue

            if is_wake_word(text):
                speak("Yes? I’m listening.")
