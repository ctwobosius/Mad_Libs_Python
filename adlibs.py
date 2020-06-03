print("Hello World!")
# name = input() # introduce variables, that you want to take in user input
# print(name)
name = input("Enter your name! ") # reassign variable
# print(name)
# string = "Hello" # intro strings
msg = "Hello {n}!" # intro string formatting
print(msg.format(n=name))

fav_show = input("What's your favorite show? ")

msg = "Your favorite show is \"{s}\" and your name is {n}!" # multiple arguments to .format
print(msg.format(n=name, s=fav_show))

print("Mad Libs!") # putting it all together :)
story = "Hey Boss, {name} reporting in, so today we created {adj1} {noun_plural} that {adverb} code for us. And, uh, it just works. We think it's powered by {adj2} {adj3} {noun_plural2} that say \"{phrase}\". "
filled_in = story.format(
    name=input("Gimme a name! "), 
    adj1=input("How about an adjective? "), 
    noun_plural=input("Plural noun? "), 
    adverb=input("Adverb? "),
    adj2=input("Another adjective? "),
    adj3=input("Yet another adjective? "),
    noun_plural2=input("Another plural noun? "),
    phrase=input("Your favorite phrase? ")
)
print()
print("Here's the mad lib!")
print(filled_in)