from core.state_manager import StateManager
from voice.text_to_speech import speak
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
            speak("Hello. I am EVA. I’m ready when you are.")
            self.state.set_active(True)
        else:
            speak("Authentication failed. Access denied.")
