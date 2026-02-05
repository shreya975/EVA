import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

MIC_INDEX = 5  # <-- PUT YOUR INDEX HERE

def listen(timeout=4, phrase_time_limit=5):
    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )
        text = recognizer.recognize_google(audio)
        return text.lower().strip()
    except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
        return ""
