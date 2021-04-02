try:
    open("this.txt")
except Exception as e:
    print(e)
# open("this.txt")
print("program zinda hai")

# try:
#     file = open("this.txt", 'r')
# except EOFError as e:
#     print("eof error")
# except IOError as e:
#     print("we can handle this error")
# finally:
#     print("This will be printed irrespective of the exception occurrence")

# try:
#     print("I will try this code and will throw exception if there is any problem")
# except Exception as e:
#     print("I will run only if try block fails")
# else:
#     print("I will run only if there is no exception. Use this to run code which should"
#           "only execute if there is no exception")
# finally:
#     print("This will be printed in every case")
