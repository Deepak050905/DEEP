# make_jsonl.py (classification)
import os, csv, json

labels = {}
with open("labels.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        labels[row['filename']] = row['label']

os.makedirs("dataset", exist_ok=True)
out_path = "dataset/train.jsonl"
with open(out_path, "w", encoding="utf-8") as out:
    for txt_file in os.listdir("transcripts"):
        if not txt_file.endswith(".txt"): continue
        base = txt_file
        # map transcripts filename to mp3 filename if needed
        corresponding_mp3 = txt_file.rsplit(".",1)[0] + ".mp3"
        if corresponding_mp3 not in labels:
            print("No label for", corresponding_mp3, "skipping")
            continue
        with open(os.path.join("transcripts", txt_file), encoding="utf-8") as t:
            text = t.read().strip()
        item = {
            "input": f"Transcript: {text}",
            "output": labels[corresponding_mp3]
        }
        out.write(json.dumps(item, ensure_ascii=False) + "\n")
print("Wrote:", out_path)
