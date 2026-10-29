\# Subset Selection Rules



\*\*Source dataset:\*\* COCO val2017 (`annotations/instances\_val2017.json`, 5000 images)



\*\*Target size:\*\* 300 images



\*\*Random seed:\*\* 42 (Python `random` module)



\*\*Selection procedure:\*\*

1\. Load all image IDs from the COCO val2017 annotation file.

2\. For each image, count its non-crowd annotations (`iscrowd = 0`).

3\. Keep only images with between 1 and 8 non-crowd instances (inclusive).

4\. Sort the remaining candidate image IDs in ascending order.

5\. Sample 300 IDs with `random.seed(42)` and `random.sample`.

6\. Save the chosen IDs and their annotations as the subset.



\*\*Evaluation exclusions:\*\*

\- Crowd annotations (`iscrowd = 1`) are excluded from all evaluation.

\- Instances with area below a minimum threshold are reported separately (threshold to be fixed in `docs/evaluation\_rules.md`).



\*\*Rationale:\*\*

\- A few hundred images is enough for a 9-week comparison and fits a laptop-class CPU.

\- Limiting instances per image to 1-8 keeps annotation timing comparable across images.

\- Fixing the seed and the candidate order makes the subset exactly reproducible.

