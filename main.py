import os

LINE = "After eleven months of 4 a.m. alarms, she pressed the last seam of her first quilt flat, held it up to the lamplight, and said nothing."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
