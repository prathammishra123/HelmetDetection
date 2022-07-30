import os
# Inside cropped folder WithHelmet and WithoutHelmet which has final dataset after face cascade without being augmented we rename them just to be safe
for idx, filename in enumerate(os.listdir("./Dataset/cropped/WithHelmet")):
    os.rename(f"./Dataset/cropped/WithHelmet/{filename}", f"./Dataset/cropped/WithHelmet/WithHelmet-{idx + 1}.jpg")

for idx, filename in enumerate(os.listdir("./Dataset/cropped/WithoutHelmet")):
    os.rename(f"./Dataset/cropped/WithoutHelmet/{filename}", f"./Dataset/cropped/WithoutHelmet/WithoutHelmet-{idx + 1}.jpg")