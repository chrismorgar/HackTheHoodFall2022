full_name = "Christian Moreno"
nickname = "Chris"
age = 22
has_used_python = True

hobbies = ["playing video games", "cycling", "skating", "nature", "napping", "traveling"]

fav_things = {
  "movie": "In Time",
  "food": "Gyoza",
  "hobby": hobbies[0],
  "anime": "DoroHeDoro",
  "number": 4
}
print(
    f"Hello world! My name is {full_name}, but many of my friends call me {nickname}. I am {age} years old."
)
print()
print(f"Has Python Experience: {has_used_python}")
print()

for key in fav_things.keys():
    print(f"My favorite {key} is {fav_things[key]}.")

print()
print(f"Here are some of my other hobbies: {hobbies}")
print()

all_vars = dict(vars())