import os
# One-liner entry (102 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "My agent apologizes so often it once said sorry to a 404 page, and the 404 page has not replied since."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
