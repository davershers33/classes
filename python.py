class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name= str(name)
        self.age= int(age)
        self.tracks=list(tracks)
        self.score= float(score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print(Bob)

def change_name(self, new_name):
        self.name= new_name

def change_age(self, new_age):
        self.age= new_age

def add_track(self, new_track):
        self.tracks= new_track

def get_score(self, score):
        self.score= score

# Expected methods
change_name(new_name="Peter")
change_age(new_age=34)
add_track(new_track="UI/UX")
get_score(score=45)