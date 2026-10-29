import cv2
import pandas as pd
from pathlib import Path
from pycocotools.coco import COCO
from tqdm import tqdm

SUBSET_JSON = Path("data/coco_subset/annotations/subset.json")
OUT_DIR = Path("data/gt_masks")
OUT_DIR.mkdir(parents=True, exist_ok=True)

coco = COCO(str(SUBSET_JSON))

rows = []
skipped_crowd = 0
skipped_empty = 0

for ann in tqdm(coco.dataset["annotations"]):
    # Crowd annotations are excluded from evaluation (see docs/subset_selection.md)
    if ann["iscrowd"] == 1:
        skipped_crowd += 1
        continue

    mask = coco.annToMask(ann)  # height x width, values 0 or 1
    if mask.sum() == 0:
        skipped_empty += 1      # safety guard: an empty mask cannot be scored
        continue

    img_dir = OUT_DIR / str(ann["image_id"])
    img_dir.mkdir(exist_ok=True)
    out_path = img_dir / f"{ann['id']}.png"
    cv2.imwrite(str(out_path), mask * 255)   # save as 0/255 so you can see it

    rows.append({
        "ann_id": ann["id"],
        "image_id": ann["image_id"],
        "category_id": ann["category_id"],
        "area": ann["area"],
        "mask_path": str(out_path),
    })

pd.DataFrame(rows).to_csv(OUT_DIR / "gt_index.csv", index=False)
print("Masks saved:", len(rows))
print("Skipped crowd:", skipped_crowd)
print("Skipped empty:", skipped_empty)