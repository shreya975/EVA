import time
from core.state_manager import StateManager
from voice.text_to_speech import speak
from voice.speech_to_text import listen
from voice.wake_word import is_wake_word
from auth.voice_auth import authenticate_voice

class EVA:
    def __init__(self):
        self.state = StateManager()
        self.last_wake = 0

    def boot(self):
        print("[EVA] Booting...")
        self.state.load_settings()
        self.state.load_permissions()

        speak("Initializing systems.")
        print("[EVA] Systems initialized")

        if authenticate_voice():
            speak("Authentication successful.")
            speak("EVA online.")
            self.state.set_active(True)
            self.idle_loop()
        else:
            speak("Authentication failed. Access denied.")

    def idle_loop(self):
        speak("Standing by.")
        print("[EVA] Listening for wake word...")

        while True:
            text = listen()
            if text:
                print(f"[EVA] Heard: {text}")

            if is_wake_word(text):
                now = time.time()
                if now - self.last_wake < 2:
                    continue
                self.last_wake = now

                print("[EVA] Wake word detected")
                time.sleep(0.4)  # release mic
                speak("Yes? I’m listening.")
