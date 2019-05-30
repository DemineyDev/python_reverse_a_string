# Program that takes a string as input, reverses it and prints it out

def reverse_a_string(string_input):
    string_list = list(string_input)  # Split the string into a list
    string_list.reverse()    # Reverse the list in place
    print("".join(string_list))    # Join the characters of the list in to a string and print it out
    
reverse_a_string("Hello World!")  # Function works as expected
reverse_a_string("DemineyDev")