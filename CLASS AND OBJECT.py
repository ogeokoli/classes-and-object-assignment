class Student:
    person = 'student'

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        # pass
Bob = Student("Bob", int(26), ["FE","BE"],float(20.90))

Bob.name = "Peter"
Bob.age = int(34)
Bob.tracks = ["FE", "BE", "UI/UX"]

print('Student details:')
print('The student\'s name is ', Bob.name)
print('age: ', Bob.age)
print('tracks: ', Bob.tracks)
print('score: ', Bob.score)



# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
