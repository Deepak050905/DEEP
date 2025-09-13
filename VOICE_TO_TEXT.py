import os
import whisper

# Folder where your mp3 files are located
INPUT_DIR = r"C:\Users\deepak bhati\OneDrive\Desktop\gemini\New folder2"
OUT_DIR = os.path.join(INPUT_DIR, "transcripts")
os.makedirs(OUT_DIR, exist_ok=True)

print("Loading Whisper model...")
model = whisper.load_model("small")

files_found = False

for fn in os.listdir(INPUT_DIR):
    print("Checking file:", fn)

    if fn.lower().endswith((".mp3", ".wav")):
        files_found = True
        print("🎵 Found audio file:", fn)

        path = os.path.join(INPUT_DIR, fn)

        try:
            res = model.transcribe(path, language='en')
            text = res["text"].strip()

            out_path = os.path.join(OUT_DIR, fn.rsplit(".", 1)[0] + ".txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)

            print("✅ Saved transcript:", out_path)

        except Exception as e:
            print("❌ Error processing", fn, ":", e)

if not files_found:
    print("\n⚠️ No mp3/wav files found in:", INPUT_DIR)
else:
    print("\n🎉 All done! Check the 'transcripts' folder.")
