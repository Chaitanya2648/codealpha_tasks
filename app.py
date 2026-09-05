genre = input("enter the genre:")
mood = input("enter the mood:")
duration = int(input("enter the duration:"))

print("You Selected:")
print(f"Genre: {genre}")
print(f"Mood: {mood}")
print(f"Duration: {duration} seconds")

if (duration >= 5 and duration <= 30):
    print("Generating music...")

    prompt = f"Generate a {mood} {genre} instrumental music with suitable instruments and beats for {duration} seconds."

    print(prompt)

else:
    print("Please enter duration between 5 and 30 seconds")
    