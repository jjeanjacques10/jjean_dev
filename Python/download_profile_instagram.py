import instaloader

insta = instaloader.Instaloader()
user = input("Enter Insta Username:")

insta.download_profile(user, profile_pic_only=True)
