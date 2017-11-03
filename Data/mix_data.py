"""
Mix lines of dataset
"""

import random
with open("languages_data.txt") as f:
    lines = f.readlines()
random.shuffle(lines)
with open("data.txt", "w") as f:
    f.writelines(lines)