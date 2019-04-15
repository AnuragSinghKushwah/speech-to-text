# importing the pyttsx library
import pyttsx3

# initialising Text to Speech Engine
engine = pyttsx3.init()

# Sample Text to Test It
sample_text = """Fundraising has always been something of a black box. 
                High-flying companies make it seem like a breeze, but most entrepreneurs lose sleep over it. 
                My first startup was called Pursuit.com and although we successfully raised a seed round, 
                it was incredibly tough (we were eventually aqui-hired by Facebook). 
                DocSend is my second startup, and it has taught me a lot about the process — not only because of our own fundraising, 
                but because the product itself reveals big pitching trends in a unique way.
                Since 2014, over 100,000 users have shared over 2.2 million links through our document tracking and sharing platform, 
                and these documents have received over 220 million views. Thousands of founders share their funding decks with prospective investors every day, 
                in addition to our product’s other uses for sales, business development and customer success. 
                To get insights about all this activity, we have a long-running partnership with Harvard Business School, 
                where we’ve been analyzing the anonymized fundraising data of startups attempting to raise a Seed or an A round."""

# testing
# engine.say(" Hello Akshay, How are you ")
engine.say(sample_text)

engine.runAndWait()