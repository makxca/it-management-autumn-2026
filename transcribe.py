from faster_whisper import WhisperModel
import sys

audio_path = sys.argv[1]

model = WhisperModel(
    "large-v3",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe(
    audio_path,
    language="ru",
    vad_filter=True
)

with open("transcript.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        line = f"[{segment.start/60:.1f}–{segment.end/60:.1f} мин] {segment.text.strip()}"
        print(line)
        f.write(line + "\n")

print("\nГотово: transcript.txt")
