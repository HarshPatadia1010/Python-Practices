#Print the poem text 
# used triple """ to print multiline in the print statement in same formate
print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
""")
#Install a module using pip and use it 
import pyttsx3

engine = pyttsx3.init()
engine.say("Twinkle, twinkle, little star,How I wonder what you are!Up above the world so high,Like a diamond in the sky.")

engine.runAndWait()


