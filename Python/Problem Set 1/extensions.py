user = input("File name: ").strip().lower()

extensions = user.split(".")[-1]

if extensions == "gif":
    print("image/gif")
elif extensions == "jpg" or extensions == "jpeg":
    print("image/jpeg")
elif extensions == "png":
    print("image/png")
elif extensions == "pdf":
    print("application/pdf")
elif extensions == "txt":
    print("text/plain")
elif extensions == "zip":
    print("application/zip")
else:
    print("application/octet-stream")

