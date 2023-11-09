from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import sys
import json

class Recognizer:
    def __init__(self):
        self.model = Model(lang="de")
        self.q = queue.Queue()

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def listen(self):
        result = {
            "success": True,
            "error": None,
            "transcription": None
        }
        device = 0
        device_info = sd.query_devices(device, "input")
        samplerate = int(device_info["default_samplerate"])

        with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device,
            dtype="int16", channels=1, callback=self.callback):
            rec = KaldiRecognizer(self.model, samplerate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    res = json.loads(rec.Result())["text"]
                    result["transcription"] = res
                    break

        return result


if __name__ == "__main__":
    print("Say something!")
    rec = Recognizer()
    prompt = rec.listen()
    print(prompt)