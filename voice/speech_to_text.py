import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

MIC_INDEX = 5  # KEEP YOUR CORRECT MIC INDEX

def listen(timeout=2, phrase_time_limit=3):
    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print("[EVA][STT] Mic opened")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        print("[EVA][STT] Audio captured")

        text = recognizer.recognize_google(audio)
        print(f"[EVA][STT] Recognized: {text}")

        return text.lower().strip()

    except sr.WaitTimeoutError:
        print("[EVA][STT] Timeout (no speech)")
        return ""

    except sr.UnknownValueError:
        print("[EVA][STT] Could not understand")
        return ""

    except Exception as e:
        print("[EVA][STT] ERROR:", e)
        return ""
