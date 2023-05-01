import instaloader
L = instaloader.Instaloader()
username = input("Enter an Instagram username: ")
profile = instaloader.Profile.from_username(L.context, username)

print(f"Name: {profile.full_name}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
print(f"Bio: {profile.biography}")

if profile.is_private:
    print("This account is private.")
else:
    print(f"Number of posts: {profile.mediacount}")
    for post in profile.get_posts():
        location = post.location
        if location is not None:
            print(f"Post {post.shortcode} is taken at {location.name} ({location.lat}, {location.lng})")
