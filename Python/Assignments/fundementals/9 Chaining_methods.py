class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
        print(self.is_rewards_member)

        return self

    def enroll(self):
        if self.is_rewards_member is True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not Enough Points")
        else:
            self.gold_card_points = self.gold_card_points - amount

        return self


michael = User("Michael", "Smith", "mSmith@yahoo.com", 45)

anna = User("Anna", "Jane", "aJane@yahoo.com", 30)

michael.spend_points(50).display_info().spend_points(200)
anna.enroll().spend_points(80).display_info().enroll()
