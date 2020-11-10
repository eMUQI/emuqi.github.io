import os

imagetype = ["png", "jpg", "tiff"]
print("in " + os.getcwd())
filelist = os.listdir()
for image in filelist:
    if image.split(".")[-1] in imagetype:
        newimage = image.split(".")[0] + ".webp"
        command = "cwebp -q 50 " + image + " -o " + newimage
        os.system(command)
