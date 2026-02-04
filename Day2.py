class Instagram:
    def __init__(self, title, description, creator_name, location, comments):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.comments = comments   # list of strings
        self.likes = 0

    def display_creator_name(self):
        print("Creator:", self.creator_name)

    def display_location(self):
        print("Location:", self.location)

    def display_comments(self):
        print("Comments:", self.comments)
       
            

    def liked(self):
        self.likes += 1

    def display_likes(self):
        if self.likes>0:
            print("Likes:", self.likes)


reel1 = Instagram(
    "dance",
    "dancing with friends",
    "Reel creator",
    "Bangalore",
    ["Super dance", "Rocked it", "Good dance"]
)

reel1.liked()
reel1.display_likes()
reel1.display_creator_name()
reel1.display_location()
reel1.display_comments()