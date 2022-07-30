import os
#  To rename the initial dataset that we have before face cascade and all 
for idx, filename in enumerate(os.listdir("./Dataset/WithHelmet")):
    os.rename(f"./Dataset/WithHelmet/{filename}", f"./Dataset/WithHelmet/WithHelmet-{idx + 1}.jpg")

for idx, filename in enumerate(os.listdir("./Dataset/WithoutHelmet")):
    os.rename(f"./Dataset/WithoutHelmet/{filename}", f"./Dataset/WithoutHelmet/WithoutHelmet-{idx + 1}.jpg")