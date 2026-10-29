import json
import random
import shutil
from pathlib import Path
from pycocotools.coco import COCO

# ---- Settings (must match docs/subset_selection.md) ----
ANN_FILE = Path("data/raw/annotations/instances_val2017.json")
RAW_IMG_DIR = Path("data/raw/val2017")
OUT_DIR = Path("data/coco_subset")
IDS_OUT = Path("docs/selected_image_ids.json")   # inside git, so the list is versioned
N_IMAGES = 300
SEED = 42
MIN_INST = 1
MAX_INST = 8

(OUT_DIR / "images").mkdir(parents=True, exist_ok=True)
(OUT_DIR / "annotations").mkdir(parents=True, exist_ok=True)

coco = COCO(str(ANN_FILE))

# Rule 2-3: keep images with 1 to 8 non-crowd instances
candidates = []
for img_id in coco.getImgIds():
    anns = coco.loadAnns(coco.getAnnIds(imgIds=img_id, iscrowd=0))
    if MIN_INST <= len(anns) <= MAX_INST:
        candidates.append(img_id)

# Rule 4: sort candidates so the order never depends on the JSON file
candidates = sorted(candidates)
print("Candidates after filtering:", len(candidates))
assert len(candidates) >= N_IMAGES, "Not enough candidate images"

# Rule 5: sample with a fixed seed
random.seed(SEED)
chosen = sorted(random.sample(candidates, N_IMAGES))

# Save the ID list (goes to git)
with open(IDS_OUT, "w") as f:
    json.dump(chosen, f, indent=2)

# Build the subset annotation file
subset = {
    "info": coco.dataset.get("info", {}),
    "licenses": coco.dataset.get("licenses", []),
    "categories": coco.dataset["categories"],
    "images": coco.loadImgs(chosen),
    "annotations": coco.loadAnns(coco.getAnnIds(imgIds=chosen)),
}
with open(OUT_DIR / "annotations" / "subset.json", "w") as f:
    json.dump(subset, f)

# Copy the chosen images
for img in subset["images"]:
    shutil.copy(RAW_IMG_DIR / img["file_name"], OUT_DIR / "images" / img["file_name"])

print("Saved images:", len(subset["images"]))
print("Saved annotations:", len(subset["annotations"]))
print("ID list written to:", IDS_OUT)