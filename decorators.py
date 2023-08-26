def decorator (function):
    def modified_function():
        print("Before calling the function")
        function()
        print("After calling the function")
    return modified_function

# def greeting():
#     print("Hello dear user.")

# modified_greeting = decorator(greeting)
# modified_greeting()

@decorator
def greeting():
    print("Hello dear user, how are you doing?")

greeting()