class InstagramAccount:
    def __init__(self,account_name,password):
        self.account_name=account_name
        self._private_reels=[]
        self.__archived_reels=[]
        self.__password=password

    def add_private_reels(self,reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self,is_follower):
        if is_follower:
            for reel in self._private_reels:
                print("Private reels:",reel)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self,reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reel(self,password):
        if password==self.__password:
            for reel in self.__archived_reels:
                print("Archived Reels:",reel)
        else:
            print("Access Denied! Only account holder can view archived reels")


    def get_archived_reel(self,password):
        if password==self.__password:
            return self.__archived_reels
        else:
            print("Access Denied!Wrong password")
            return None
        
    def set_password(self,old_password,new_password):
        if old_password == self.__password: 
            self.__password = new_password 
            print("Password updated successfully!") 
        else: 
            print("Wrong old password! Password not changed.")

account=InstagramAccount("ABC","8724")

account.add_private_reels("Travel Reel")
account.add_private_reels("Motivation Reel")

account.add_archived_reel("Technical Reels")
account.add_archived_reel("Dance Reel")

account.display_private_reels(True)
account.display_private_reels(False)

account.display_archived_reel("8724")
account.display_archived_reel("8742")

account.get_archived_reel("8724")

account.set_password("8724","7824")

account.display_archived_reel("7824")