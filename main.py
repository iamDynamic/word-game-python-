Words = {
    "javascript" : "I’m the language of the web, running in browsers everywhere.",
    "python" : "I'm named after a snake, but coders love me",
    "subway": "You travel underground, zipping through city tunnels",
    "Counter-Strike" : "A famous game where you defuse bombs or protect them",
    "App Store" : "A digital shop on iPhones, full of games and tools.",
    "WhatsApp":"I’m a green icon where people chat with friends around the world",
    "Telegram":"I’m a chat app with channels and a focus on privacy ",
    "Fortnite":"“A battle royale where you build, shoot, and do dance emotes.",
    "Valorant": "A shooter by Riot Games where agents use abilities.",
    "Calculator": "For math wizards and students alike, I make numbers add up.",
    "Settings": "I help you change preferences and personalize your device.",
    "Photo": "Where memories are stored, edited, and shared.",
    "Hangman": "Guess wrong and you’ll build a stick figure in trouble.",
    "Serendipity": "An unexpected, pleasant surprise.",
    "Galaxy": "You might live in one; it’s filled with stars and planets.",
    "Whisper": "A very quiet way to talk, so only a few can hear.",
    "Flicker": "A light that’s not steady, almost as if it’s unsure.",
    "Ember": "After a fire burns out, I glow in red or orange.",
    "Spiral": "I curve endlessly around a central point.",
    "Telescope":"An instrument used to observe distant objects in space.",
    "Eclipse":"An event where one celestial body moves into the shadow of another.",
    "Kaleidoscope":"A toy that shows changing patterns of colors when viewed through its lens.",
    "first person shooter":"A genre of games where players view the action through the eyes of the protagonist.",
}

def startGame():
    for key,value in Words.items():
     print("__________________")
     print(value)
     entry = input("enter the guess:")
     if entry == key:
         print(f"your answer is correct: {key}")
         print("__________________")
     elif entry == "close" :
         print("you have finish the game")
         print("__________________")
         break
     
     else:
           print(f"your answer is not correct {key}")
           print("__________________")
           
           

startGame()
