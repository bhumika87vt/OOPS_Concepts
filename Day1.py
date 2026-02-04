# Class and object
class Instagram:
    def __init__(self,title, description,comments,creator_name,location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.creator_name=creator_name
        self.location=location
        self.comments=comments

    def display_title(self):
        print("The title of the reel is", self.title)

    def display_description(self):
        print("The description ofn the reel is",self.description)

    def display_likes(self):
        print("the number of likes",self.likes)

    def display_dislikes(self):
        print("the number of dislikes",self.likes)

    def display_creator_name(self):
        print("The creator name is ",self.creator_name)

    def display_location(self):
        print("The location is ",self.location)
    
    def liked(self):
        self.likes+=1
    
    def disliked(self):
        if self.likes>0:
            self.likes-=1

    def display_comments(self):
        print("The comments are:")
        for comment in self.comments:
            print("-",comment)

    def delete_last_comment(self):
        if len(self.comments)>0:
            removed_comments=self.comments.pop()
            print("Removed comments",removed_comments)


reel1=Instagram("dancing","trending reels",["super dance","Rocked it","Good dance"],"Reel_creator","Bangalore")
reel1.display_title()
reel1.liked() 
reel1.liked() 
reel1.liked()
reel1.disliked() 
reel1.display_likes()
reel1.display_dislikes()
reel1.display_comments()
reel1.display_creator_name()
reel1.display_location()
reel1.delete_last_comment()
reel1.display_comments()

reel2=Instagram("finance minister conference","finance minister conference with friends",
                ["good message","nice","thought was good"],"minister","Bangalore urban")
reel2.display_title()
reel2.liked() 
reel2.liked()
reel2.disliked()
reel2.display_likes()
reel2.display_dislikes()
reel2.display_comments()
reel2.display_creator_name()
reel2.display_location()
reel2.delete_last_comment()
reel2.display_comments()

print(id(reel1))
print(id(reel2))