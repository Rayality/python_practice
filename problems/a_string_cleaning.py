def change_confirmation():
    response = str.upper(input("Do you want to keep the changes? 'Y' or 'N'\n"))
    while response != "Y" and response != "N":
        response = str.upper(input("Must answer with: 'Y' or 'N' \n"))
    if response == 'Y':
        return True
    return False


def replace_a_character(item, char, replacer=''):
    modified_list = []
    modified_string = ''
    if type(item) == type([]):
        for count, user_string in enumerate(item):
            newser_string = user_string.replace(char, replacer)
            modified_list.append(newser_string)
            print(f"Index #{count}: {newser_string}")
        if change_confirmation() == True:
            return modified_list
    else:
        modified_string = item.replace(char, replacer)
        print(modified_string)
        if change_confirmation() == True:
            return modified_string
    return item


def splitter(item):
    separator = input("Which character/s will split the string? (split choice/s will be removed in the process) ")
    if type(item) == type([]):

        for ind, inner_item in enumerate(item):
            try:
                this = inner_item.strip()
                this = this.split(separator)
            except:
                print(f"INPUT: {separator}  NOT FOUND IN:  {inner_item}")
                continue

            for in_inner_item in this:
                item[ind] = (in_inner_item)
                print(in_inner_item)
        return item

    else:
        try:
            copy = item
            new_list = copy.split(separator)
        except:
            print("No separator chosen/found.")
            return item
        for item in new_list:
            print(item)
        if change_confirmation():
            return new_list
        return item


def insert_in_each_string(chars_string):
    if type(chars_string) == type([]):
        for this in chars_string:
            print(this)
        print("REMINDER: Choices are applied to each string section.")
        new_list = chars_string
        insert_item = input("What string would you like to insert?\n")
        insert_indicator = input(f"After which characters would you like to insert {insert_item}?\n")
        index_or_all = int(input(f"""Are we inserting a new string after all occurances of {insert_indicator}, or at the (x) occurance?: (leave blank for all)\n"""))
        if index_or_all is not None:
            for string in chars_string:
                new_string = ""
                if insert_indicator in string:
                    insert_index = string.find(insert_indicator) + len(insert_indicator)
                    for char in string[:insert_index]:
                        new_string += char
                    new_string += insert_item
                    if index_or_all == 0:
                        for char in string[insert_index:]:
                            new_string += char
                    new_list.append(new_string)
                    index_or_all -= 1
                else:
                    new_list.append(string)
        else:
            for string in chars_string:
                new_string = ""
                if insert_indicator in string:
                    insert_index = string.find(insert_indicator) + len(insert_indicator)
                    for char in string[:insert_index]:
                        new_string += char
                    new_string += insert_item
                    for char in string[insert_index:]:
                        new_string += char
                    new_list.append(new_string)
                else:
                    new_list.append(string)
        return new_list


def delete_an_element(items):
    new = items
    for count, item in enumerate(items):
        print(f"Element #{count}: {item}")
    try:
        element_number = int(input("Which element (by number) would you like to remove? "))
        removed = new.pop(element_number)
        print(new)
        print("Removed:", removed)
    except:
        print("Input was not a number.")
        return items
    if change_confirmation() == True:
        return new
    return items


def information():
    inquiry = str.upper(input("Which option do you need explained?"))
    if (inquiry == 'R' or inquiry == 'E'):
        print("""
                Remove and Replace are the same function. When remove is chosen, the replacing character is ''.\n
                Remove/Replace will take a single input of one or more characters ('a' or 'word').\n
                It will then search your current string and take out any occurance of the first input and replace it.\n
                Remove will replace it with nothing '' and not leave a space behind. eg('word' with input of 'o' will return 'wrd').\n
                The function does not remove the other case variant. ('a' will not remove 'A')\n
                The string method of .replace() is used with the second arguement being an empty string '' if Remove was chosen.
                """)

    elif (inquiry == 'S'):
        print("""
                Split will take a single input of one or more characters ('a' or 'word').\n
                The current string will be split into sections and put into a list.\n
                It will be split at every occurance of your input, while removing the input.\n
                Example: "original string" input: 'i'   output: ['or', 'g', 'nal', 'str', 'ng']\n
                This is the string method .split()
                """)
    # elif (inquiry == 'D'):
    # elif (inquiry == 'X'):


def make_string():
    stop_input = "Ex-it"
    print("Spaces are added before each input. Automatically handles multiple line inputs.")
    output = ""
    item = input("Type or paste your input.")
    while item != stop_input:
        output += (" " + item)
        item = input(f"Type {stop_input} to finish: ")

    return output


def clean_element_values():
    current_item = input("String to be cleaned or leave blank to make a string: ")
    options = """
                'M' - Make a string from multiple lines.
                'N' - iNsert a character or string.
                'R' - Remove a character or string.
                'E' - Replace a character or string.
                'S' - Split the string into sections.
                'D' - Delete an element in an already split string.
                'I' - information.
                'X' - Exit program.
                """
    reply = ''
    print(options)
    while reply != 'X':
        print(options)
        reply = str.upper(input("What would you like to do?\n"))

        if reply == 'R':
            print(current_item)
            char = input("What would you like to remove?\ninput: ")
            current_item = replace_a_character(current_item, char)

        elif reply == 'M':
            current_item = make_string()

        elif reply == 'I':
            information()

        elif reply == 'N':
            current_item = insert_in_each_string(current_item)

        elif reply == 'E':
            print(current_item)
            char = input("What would you like to replace?\nInput 1: ")
            new_char = input(f"What would you like to replace {char} with?\nInput 2: ")
            current_item = replace_a_character(current_item,char,new_char)

        elif reply == 'S':
            if type(current_item) != type('S'):
                print("It seems to have been split already.")
                continue
            current_item = splitter(current_item)

        elif reply == 'D':
            if type(current_item) != type([]):
                print("This function is for removing an element from a string that has been split.\nTry the replace or remove options.")
                continue
            current_item = delete_an_element(current_item)

        elif reply == 'X':
            break

    if type(current_item) == type([]):
        print('[', sep='', end='')

        for item in current_item:
            print(f"{item},")

        print(']', sep='', end='')
        return 1

    else:
        print(f"Result: \n{current_item}")
        return True

clean_element_values()
