print("Hello welcome my name is jarvis .How can i help you?")
def greet():
    print("hi")
def how():
    print("I'm fine,thanks!")
def end():
    print("Goodbye!")
while str is not None:
    str=input()
    if str=="hello":
        greet()
    elif str=="how are you":
        how()
    elif str=="bye":
        end()
    else:
        print("I'm sorry I cannot understand you.")
