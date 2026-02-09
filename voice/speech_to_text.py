import os
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# =========================
# CONFIG
# =========================
SAMPLE_RATE = 16000  # REQUIRED by VOSK
CHANNELS = 1

# =========================
# MODEL PATH (BULLETPROOF)
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "vosk-small-en")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"[EVA][STT] Model path not found: {MODEL_PATH}")

# =========================
# INIT VOSK
# =========================
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

audio_queue = queue.Queue()

# =========================
# AUDIO CALLBACK
# =========================
def audio_callback(indata, frames, time, status):
    if status:
        print("[EVA][STT] Status:", status)
    audio_queue.put(bytes(indata))

# =========================
# LISTEN FUNCTION
# =========================
def listen(timeout=4):
    try:
        with sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=8000,
            dtype="int16",
            channels=CHANNELS,
            callback=audio_callback,
        ):
            try:
                data = audio_queue.get(timeout=timeout)
            except queue.Empty:
                return ""

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                return result.get("text", "").lower().strip()

    except Exception as e:
        print("[EVA][STT] ERROR:", e)
        return ""

    return ""
