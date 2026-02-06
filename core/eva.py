import time

from core.state_manager import StateManager
from voice.text_to_speech import speak
from voice.speech_to_text import listen
from voice.wake_word import is_wake_word
from auth.voice_auth import authenticate_voice


class EVA:
    def __init__(self):
        print("[EVA] Initializing state manager")
        self.state = StateManager()
        self.last_wake = 0

    def boot(self):
        print("[EVA] Booting...")
        self.state.load_settings()
        self.state.load_permissions()

        speak("Initializing systems.")
        print("[EVA] Systems initialized")

        print("[EVA] Authenticating...")
        if authenticate_voice():
            print("[EVA] Auth success")
            speak("Authentication successful.")
            speak("EVA online.")
            self.state.set_active(True)
            self.idle_loop()
        else:
            speak("Authentication failed. Access denied.")

    def idle_loop(self):
        print("[EVA] Entered idle loop")
        speak("Standing by.")
        print("[EVA] Listening for wake word...")

        while  True:
            print("[EVA] Waiting for audio...")
            text = listen()
            if text:
                print(f"[EVA] Heard (raw): {text}")

            if is_wake_word(text):
                now = time.time()
                if now - self.last_wake < 2:
                    continue

                self.last_wake = now
                print("[EVA] Wake word detected")

                time.sleep(0.4)  # allow mic to release
                speak("Yes? I’m listening.")
