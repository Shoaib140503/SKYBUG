import random

def random_string():
  random_list = [
    "Please try writing something more descriptive.",
    "Oh! it appears you wrote something I don't understand yet.",
    "Do you mind trying to rephrase that?",
    "I'm terribly sorry, I didn't quite catch that.",
    "I can't answer that yet, please try asking something else.",
    "I didn't understand that, instead here's a quote for you: Growing pain's a necessary evil. Difficult to go through, yes, but beneficial.",
    "I didn't understand that, instead here's a quote for you: Love is brightest in the dark.",
    "I didn't understand that, instead here's a quote for you: Pride is not the opposite of shame, but it's source. True humility is the only antidote to shame.",
    "I didn't understand that, instead here's a quote for you: You either die a hero or you live long enough to see yourself become the villain.",
    "I didn't understand that, instead here's a quote for you: Life happens wherever you are, whether you make it or not. Life's Just random, Everything is random.",
    "I didn't understand that, instead here's a quote for you: You have to look within yourself to save yourself from your other self, only then your true self will reveal itself. 😂",
    "I didn't understand that, instead here's a quote for you: Service to others is the rent we pay for our room in heaven.",
    "I didn't understand that, instead here's a quote for you: Discipline comes through self control. If you do not conquer self, you will be conquered by self.",
    "I didn't understand that, instead here's a quote for you: Whatever you do in this life, it's not legendary unless your friends are there to see it.",
    "I didn't understand that, instead here's a quote for you: Garibi jab darwaaze se andar aati hai, tab mohabbat khidki se bahar chali jaati hai.",
    "I didn't understand that, instead here's a quote for you: Beware of Allah's punishment and remember Allah's favours.",
    "I didn't understand that, instead here's a quote for you: Sometimes, the pain of life overrides the joy to the point that joy does not exist.",
    "I didn't understand that, instead here's a quote for you: The desire to be loved is the last illusion. Give it up and you will be free.",
    "I didn't understand that, instead here's a quote for you: Your hardwork might betray you but never betray your hardwork.",
    "I didn't understand that, instead here's a quote for you: Smartest people in the world don't have answers to everything but they know exactly what question to ask.",
    "I didn't understand that, instead here's a quote for you: When you are suffering, that's when you're most real.",
    "I didn't understand that, instead here's a quote for you: People want God to do everything for them but they don't realize is they have the power. You want to see a miracle? Be the miracle.",
    "I didn't understand that, instead here's a quote for you: The windshield is bigger than the rearview mirror for a reason, because what's in front of you is so much more important than what's behind you.",
    "I didn't understand that, instead here's a quote for you: Reality can be cruel and it often strikes without warning, one must always be prepared for this crossroads in life.",
    "I didn't understand that, instead here's a quote for you: A jack of all trades is a master of none but often times better than a master of one.",
    "I didn't understand that, instead here's a quote for you: There's no 4 years of work and 50 years of pleasure, find pleasure in pain if you want pleasure for eternity."
  ]

  list_count = len(random_list)
  random_item = random.randrange(list_count)

  return random_list[random_item]
