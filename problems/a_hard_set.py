# ________________________________________________________________SECRET_MESSAGE_________________________________________________________
# You and your friend decide to meet up in a breakout room,
# but you don't want other people to know which
# breakout room you're going to until after you've chosen it.

# To do this, you devise a way to send a secret message.
# You choose four unique letters, like "PLOD".
# Then, you construct a string that has those letters in it, in order,
# with other letters possible between the letters that you chose.
# You send the four unique letters and the secret message to your friend.

# When your friend gets the four letters and the string,
# they throw out as many letters as they can to leave
# only all of the "PLOD" values that they can.
# Then, they count how many "PLOD" occurrences there are in the secret message.
# That's the number of the breakout room that the two of you should meet in.


# Given two strings, code and message,
# complete the function breakout_room that returns
# the count of the number of times that code occurs in message.

# Constraints:

# code has four unique uppercase letters
# 1 <= len(message) <= 100000
# message has only uppercase letters
# Example:

# Let's say that you receive these values from your friend.
# You scan the string and find all of the ASDF values in it in that order.

# code:    ASDF
# message: SODIFJOSDIFJASOIDFASLWEARWOERIMSOEIDENRMFASD
#                      AS  DFAS               D    F
# Your code would return 2.


def breakout_room(code, message):
    count = 0
    char = 0
    for i in range(len(message)):
        if message[i] == code[char]:
            char += 1
            if char == 4:
                count += 1
                char = 0
    return count


# ________________________________________________________________SECRET_MESSAGE_________________________________________________________


# #_________________________________________________________________TRAVELING MINSTREL______________________________________________________________________
# Every evening villagers in a small village gather around a big fire and sing songs.

# A visitor to the community is the traveling minstrel.
# Every evening, if the minstrel is present,
# he sings a brand new song that no villager has heard before,
# and no other song is sung that night.
# In the event that the minstrel is not present,
# other villagers sing without him and exchange all songs that they know.

# Given the list of villagers present for some number of consecutive evenings,
# you should calculate the total number of villagers that know all of the songs.

# For example, let's say there are 5 villagers in the village,
# numbered 1, 2, 3, 4, and 5.
# Let's say the minstrel is represented by the number 0.
# Here's a record of each evening:

# Evening #	Attendees	Who knows all the songs	    Reason
# 1	            2, 4	        2, 4	            2 and 4 know all the songs

# 2	           0, 1, 2	        2	                Only 2 knows all the songs sung

# 3	           1, 3, 4	    1, 2, 3, 4	            1 knows the song from evening 2,
#                                                   and four knows the songs from evening 1,
#                                                   sharing them they now know all the songs

# 4	            1, 2	    1, 2, 3, 4	            Nothing changes

# 5	            0, 5		                        5 now knows a new song that no one else knows and
#                                                   doesn't know any other songs

# 6	            3, 5	        3, 5	            3 and 5 share their songs and now know all of them

# The result is 2, just the villagers 3 and 5 know all of the songs.

# Given the number of villagers num_villagers
# and a list of lists attendees_lists that record the attendees each evening,
# where 0 is the minstrel and all other numbers are the villagers,
# complete the function total_song_knowers to calculate
# the total number of villagers that know all the songs.


def total_song_knowers(num_villagers, attendees_lists):
    # amount of unique songs available.
    # starts with 1 song called '0'
    amt_uniq_songs = 1
    villagers = {}
    # populate the dictionary with "villager : songs_known"
    while num_villagers:
        villagers[num_villagers] = set()
        num_villagers -= 1

    while attendees_lists:
        todays_songs = {0}  # <-- start the set with 1 song called '0'

        # adds a unique song if minstrel is present today.
        # Then remove minstrel to shorten the later operations
        if 0 in attendees_lists[0]:
            amt_uniq_songs += 1
            todays_songs = {amt_uniq_songs}
            attendees_lists[0].remove(0)
            # changing the villager's set to a new object
            # Now we can update it without changing the previous day
            for attended in attendees_lists[0]:
                set_change = todays_songs.union(villagers[attended])
                villagers[attended] = set_change

        # else: add the villagers known songs to "todays songs"
        # and give a deep copy of "todays songs" to the villager
        else:
            for attended in attendees_lists[0]:
                todays_songs.update(villagers[attended])
                villagers[attended] = todays_songs

        # Remove the day so the next day is at attendees_lists[0].
        attendees_lists.pop(0)

    # determines how many villagers know every song
    knows_all = 0
    for villager in villagers:
        if len(villagers[villager]) == amt_uniq_songs:
            knows_all += 1
    return knows_all


# #_________________________________________________________________TESTS______________________________________________________________________

days = [[0, 1], [1, 2, 3], [3, 1, 0]]
people = 3
days2 = [[0, 2], [1, 0], [1, 0, 3, 4]]
people2 = 4
days3 = [[0, 2, 4, 3], [4, 5], [5, 6, 7], [5, 1], [1, 5, 7, 0]]
people3 = 7
print("expected 3: returned: ", total_song_knowers(people3, days3))
print("expected 2: returned: ", total_song_knowers(people, days))
print("expected 0: returned: ", total_song_knowers(people2, days2))
# # the tests from learn.-----------------------------------

# #_________________________________________________________________TRAVELING MINSTREL______________________________________________________________________


# =======================Tide_difference==================================
# Asha has been stranded on an island for many days.
# He's grown terribly bored with his situation.
# He's started to find ordinary things immensely fascinating.

# Today, he's interested in the waves he sees.
# He notes that at certain times of the day,
# the water level either increases or decreases.
# Realizing this phenomenon is due to tides,
# he's now most fervent about determining the
# difference in water level between high tide and low tide.

# He's started measuring the water level throughout the day
# using a high-precision measuring device (that he had when he got marooned),
# such that each reading is a unique integer,
# that is, no two readings are the same.

# He knows that after measuring the absolute minimum reading at low tide,
# the transition to the absolute maximum reading representing the water level
# at high tide consists of a strictly increasing sequence of water level readings.

# He's interested in the difference between the absolute maximum
# and absolute minimum readings: the water level difference between the low and high tides.

# He knows it's possible that he made a mistake in writing down some readings.
# In the case where the sequence between the low tide reading and
# high tide reading is not strictly increasing,
# then he knows that he messed up and will throw away that day's measurements.

# Once he gets back to the mainland, he shares all of his daily measurements with you.
# He asks if you can help him calculate the difference between the low tide and the high tide for one of the days.

# Given a series of measurements, where each measurement is a unique number,
# in chronological order over a day,
# complete the function tide_difference to determine what the difference
# is between the low tide and high tide measures.

# If the values between the low tide and the high tide do not always increase, then return None.

# If there's no high tide after the low tide, return None.

# Example 1:

# Look at these measurements where the low tide and the high tide are in quotes:

# 3, '1', 4, 6, '7', 5

# The difference is 6.

# Example 2:

# Look at these measurements where the low tide and the high tide are in quotes
# and a bad reading is in / /:

# 3, '1', 4, 6, /5/, '7', 2

# This is bad data and the function should return None.

# Example 3:

# Look at these measurements:

# 5, 4, 3, 2, 1

# There is no high tide reading after the low tide. This is bad data and the function should return None


def tide_difference(measurements):
    low = min(measurements)
    high = max(measurements)
    difference = high - low
    low_index = measurements.index(low) + 1
    high_index = measurements.index(high)
    section = slice(low_index, high_index)

    if low_index > high_index:
        return None

    previous_number = low

    for num in measurements[section]:
        if num < previous_number:
            return None
        previous_number = num
    return difference


# ----------------TESTS---------------
# a = [3,1,4,6,7,5] # returns 6
# b = [3,1,4,6,9,2] # returns 8
# c = [3,1,4,6,5,7,2] # returns None
# d = [5,4,3,2,1]# returns None
# print(tide_difference(a))
# print(tide_difference(b))
# print(tide_difference(c))
# print(tide_difference(d))

# =======================Tide_difference===================================

# =======================SAT without studying==================================

# This year, the SAT is made up of multiple choice questions, each with three answers: A, B, or C.
# Three friends, Azami, Baz, and Caris, all take the SAT on the same day.
# However, they didn't study and, rather,
# want to leave their scores up to the Fates.
# Azami will fill out the answer sheet using the sequence A, B, C, A, B, C, A, B, C, ...

# Baz will fill out the answer sheet using the sequence B, A, B, C, B, A, B, C, B, A, B, C, ...

# Caris will fill out the answer sheet using the sequence A, A, C, C, B, B, A, A, C, C, B, B, ...

# Given an answer key, which of the test takers gets the highest score and what is it?

# Given the input answer_key,
# determine which of the students Azami, Baz, or Caris gets the best score
# based on the sequences that they'll use to fill out the form.

# Azami will repeat A, B, C for all of the questions
# Baz will repeat B, A, B, C for all of the questions
# Caris will repeat A, A, C, C, B, B for all of the questions
# Constraints: 1 <= len(answer_key) <= 100

# Example:

# Take a look at the following input and how the students would respond:

# Answer key:    A B B A A C C A C B C A A
# Azami guesses: A B C A B C A B C A B C A
# Baz guesses:   B A B C B A B C B A B C B
# Caris guesses: A A C C B B A A C C B B A
# If you tally them up, you can see that
# Azami got 6 right,
# Baz got 0 right,
# and Caris got 4 right.
# That means that you'd return 6 and "Azami".


def best_student_and_score(answer_key):
    azami_guesses = "ABC"
    baz_guesses = "BABC"
    caris_guesses = "AACCBB"
    acount = [0, "Azami"]
    bcount = [0, "Baz"]
    ccount = [0, "Caris"]
    for ind, char in enumerate(answer_key):
        cletter = caris_guesses[ind % 6]
        bletter = baz_guesses[ind % 4]
        aletter = azami_guesses[ind % 3]
        if char == aletter:
            acount[0] += 1
        if char == bletter:
            bcount[0] += 1
        if char == cletter:
            ccount[0] += 1
    winner = max(acount, bcount, ccount)
    return winner[0], winner[1]


# answers = "ABBAACCACBCAA"
# print(best_student_and_score(answers))

# =======================SAT without studying==================================

# ===========================gold coin=========================================
# There's an old game played by a group of kids.
# One gets a chocolate gold coin, but keeps it secret.
# Then, all the kids in the group play rock-paper-scissors.
# If you're holding the gold coin and your opponent wins rock-paper-scissors,
# then you surreptitiously give the gold coin to them.
# Otherwise, you hold on to the gold coin.

# As many things do, this game has taken the adult world by storm.
# You're going to be on the leading edge of the fad
# with the first tournament Web site set up to track the gold coins tournaments.

# Each round of the game has 26 players,
# labeled "A" through "Z".
# You're given the starting_player who has the gold coin,
# and a list of matches where each entry is a
# string of two letters denoting the two players in the match,
# the first the winner and the second the lower.
# Complete the function outcome to return
# the label of the player that has the gold coin at the end of the tournament.

# Constraints: 1 <= len(matches) <= 100

# Example:

# Your function gets the value "Z" for starting_player, which means "Z" has the gold coin.
# For matches, your input list looks like this:
# [ "ZA", "CD", "BZ", "SE", "FA", "LB"]

# First match: ZA - Z wins and keeps the coin
# Second match: CD - neither has the coin
# Third match: BZ - B wins the coin from Z
# Fourth match: SE - neither has the coin
# Fifth match: FA - neither has the coin
# Sixth match: LB - L wins the coin from B


def outcome(starting_player, matches):
    winner = starting_player
    for match in matches:
        if winner in match[0]:
            continue
        elif winner in match[1]:
            winner = match[0]
    return winner


# start = "Z"
# matches = [ "ZA", "CD", "BZ", "SE", "FA", "LB"]
# print(outcome(start, matches))
# =======================gold coin==================================

# =======================flip flop==================================
# Your auntie gives you a puzzle for your birthday.
# It's a box with one button and a screen.
# Intrigued by it, you press the button and see an "X" appear on the screen.
# You press the button, again, and the "X" is replaced by "O".
# You press it, again, and the "O" is replaced by "OX".
# You keep pressing it and get "OXO", "OXOOX".

# After playing around with it for a while,
# you realize that every time you press the button,
# it changes all of the "X" letters to "O" letters,
# and changes all of the "O" letters to the letters "OX".

# Here's that sequence again:

# Start:
# Press: X
# Press: O      (The X becomes an O)
# Press: OX     (The O becomes OX)
# Press: OXO    (Of OX, the first O becomes OX and the X
#                becomes an O)
# Press: OXOOX  (Of OXO,
#                 the first O becomes OX,
#                 the X becomes O, and
#                 the second O becomes OX)
# The sequence has you intrigued.
# You decide to write a program to figure out how many "X" and "O" letters
# there are on the screen after you push it a certain number of times.

# Given the number of times to push the button num_pushes,
# complete the function calculate_num_letters so that it returns
# both the number of Xs and Os.

# Constraints: 1 <= num_pushes <= 20


def calculate_num_letters(num_pushes):
    print("number of pushes:", num_pushes)
    a = "X"
    b = "O"
    output = ""

    if num_pushes == 1:
        output = a

    elif num_pushes == 2:
        output = b

    else:
        while num_pushes - 2:
            output = b + a
            a = b
            b = output
            num_pushes -= 1

    return (output.count("X"), output.count("O"))


# =======================flip flop==================================


# =====================DNA TRANSCRIPTION================================
# DNA is made up of two twisted strands that encode genes
# using long combinations of four bases: Adenine, Cytosine, Guanine, and Thymine.
# The strands are complementary to one another,
# meaning that Adenine and Thymine are always opposite each other,
# and Cytosine and Guanine are always opposite each other, like this:

# A double strand of DNA:
# ATCAAGGCCTATTCCGGGAAAGG
# TAGTTCCGGATAAGGCCCTTTCC

# In order for the information in a gene to be used,
# it has to be transcribed into a strand of RNA.
# During this process, a portion of one strand of DNA is transcribed.
# This portion is known as the transcription unit.
# The start of the sequence to be transcribed is signaled by
# a sequence of bases known as a promoter,
# and the end is signaled by a sequence known as the terminator.
# For our purposes, the promoter is the sequence TATAAT,
# which begins 10 bases before the start of the transcription unit,
# and the terminator consists of two distinct, complementary,
# reversed sequences of at least length 6 that cause
# the RNA molecule to coil back on itself and pinch off the transcribed strand.
# If TATAAT appears twice on a strand,
# only the first occurrence counts as the promoter.
# An example is shown below.

# AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC
# AGATTATATAATGATA "GGATTTAGATTGACCC" -|GTCATGCA|- AGTCCA -|TGCATGAC|-AGC

# In this example, the promoter and terminator sequences are in -||-,
# and the transcription unit is between quotes.

# The first step is to find the promoter, specifically the sequence TATAAT.

# Starting at the first T in the promoter,
# count forward 10 characters and that's where the transcription unit starts,
# in this case the first G in quotes.

# After the first letter of the transcription unit,
# search the remainder of the string for two sequences of letters
# at least six characters long that,
# when the first is matched up to the reverse of the second,
# it forms a valid double strand of DNA
# where A matches with T and G matches with C:

# GTCATGCA
# CAGTACGT  (the reverse of the second sequence)
# This is the terminator.

# The transcription unit is the characters including
# the first letter of the transcription unit found in step 2 all the way up to,
# but not including, the first letter of the terminator found in step 3.

# The resulting RNA will be complementary to the transcription unit,
# except that in RNA Uracil takes the place of Thymine.
# Here's an example of how to turn the transcription unit into RNA:

# Transcription unit: GGATTTAGATTGACCC
# Complement:         CCTAAATCTAACTGGG
# Replace T with U:   CCUAAAUCUAACUGGG
# The final string is the RNA CCUAAAUCUAACUGGG for the gene.

# Your job is to write a function that performs this calculation.

# Here are some sample inputs and outputs for you to test your function as you write it.
# The promoter, transcription unit, and terminator are marked for each strand for you to better be able to see it.

# Input:  AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC
#               |-P--|    |------TU------||--T---|      |--T---|
# Output: CCUAAAUCUAACUGGG

# Input:  AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA
#                                 |-P--|    |----TU------||--T---|                 |--T---|
# Output: UAGCGCUGCUUUAU

# Input:  TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT
#         |-P--|    |------TU---------||-T--|    |-T--|
# Output: CUCUCUGGCUCACAAAUUC


def rna_transcription(dna):
    # finding the Translation Unit start and discard characters before that
    tran_unit_start = dna.find("TATAAT") + 10
    remainder = str(dna[tran_unit_start:])

    # turning the remaining string into a complimented version
    # then reversing it to find the terminator pair in the "for loop"
    compliment = str.maketrans("ATGC", "TACG")
    comp_remainder = remainder.translate(compliment)
    rvr_comp_remainder = comp_remainder[::-1]

    for i in range(len(remainder)):
        # getting a string section of 6 characters
        j = i + 6
        section = remainder[i:j]

        # if that section has a reversed complimentary match,
        #       it is a terminator pair
        if section in rvr_comp_remainder[:-j]:
            # setting the translation unit to be
            # the full string up until the first index of the terminator pair.
            full_tran_unit = comp_remainder[:i]
            break

    # changing the letters "T" into "U"
    rna = full_tran_unit.translate({84: 85})
    return rna


# ----------------------TESTS------------------

# Input1 = "TATAATGCAGTGGTTCCCCGCGGAACATTCCGCGGGGAAACTAG"
# # Output: 'GUUAGCUAG'

# Input2 = "AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA"
#                             #     |-P--|    |----TU------||--T---|                 |--T---|
# # Output: UAGCGCUGCUUUAU-UAGCGCUGCUUUAUA

# Input1 = "TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT"
# #         |-P--|    |------TU---------||-T--|    |-T--|
# # Output: CUCUCUGGCUCACAAAUUC
# print(rna_transcription(Input1))

# ==================DNA TRANSCRIPTION======================

# ______________LAUNDRY___________________
# There are a lot of software development conferences that you can attend.
# Normally, when you go to one, they give you a free T-shirt!

# Samir really likes going to conferences because he hates doing laundry.
# Samir only does his laundry when all of his t-shirts are dirty.
# As he goes to more and more conferences,
# this allows Samir to delay having to do laundry for longer periods of time.

# Samir starts with a certain number of t-shirts.
# He wears one clean shirt every day,
# after which it becomes dirty.
# If the day begins and Samir has only dirty shirts,
# then he will do his laundry, which makes all of his shirts clean again.
# If Samir goes to a conference, then he gets one new clean shirt.
# Samir only gets a new shirt from the conference after putting on a clean shirt.

# For example, you want to determine how many times Samir does laundry over a 10-day period given that:

# Samir starts with one clean shirt

# Samir attends an event on the third day and the seventh day

# Day 1, Samir wakes up and wears his one clean shirt

# Day 2, Samir wakes up and has no clean shirts, does laundry, and wears his one clean shirt

# Day 3, Samir wakes up and has no clean shirts, does laundry, and wears his one clean shirt, and gets a new shirt

# Day 4, Samir wakes up and has one clean shirt, one dirty shirt, and wears his one clean shirt

# Day 5, Samir wakes up and has no clean shirts, does laundry, wears one clean shirt, and folds his other clean shirt

# Day 6, Samir wakes up and has one clean shirt, one dirty shirt, and wears his one clean shirt

# Day 7, Samir wakes up and has no clean shirts, does laundry, wears one clean shirt, folds his other clean shirt, and gets a new shirt

# Day 8, Samir wakes up and has two clean shirts, one dirty shirt, and wears one of the clean shirts

# Day 9, Samir wakes up and has one clean shirt, two dirty shirts, and wears his one clean shirt

# Day 10, Samir wakes up and has no clean shirts, does laundry, wears one clean shirt, and folds the two other clean shirts

# Samir does laundry 5 times.

# Given the number of clean shirts that Samir has num_shirts,
# the number of days that you're interested in monitoring num_days,
# and a list of days on which there are events event_days,
# complete the function num_laundry_days to return
# the number of times that Samir will have to do laundry during num_days.

# Samir begins this time with all clean t-shirts
# Each day Samir wears a clean shirt, which becomes dirty
# Each day Samir goes to a conference, he gets one new clean shirt
# When Samir has no clean t-shirts, he does his laundry,
# which makes all his t-shirts clean again
# Constraints:
# 1 <= num_shirts <= 100
# 1 <= num_days <= 1000
# 1 <= len(event_days) <= 100


def num_laundry_days(num_shirts, num_days, event_days):
    laundry_days = 0
    dirty_shirts = 0
    clean_shirts = num_shirts

    for today in range(1, num_days + 1):
        if clean_shirts == 0:
            laundry_days += 1
            clean_shirts = dirty_shirts
            dirty_shirts = 0

        if today in event_days:
            clean_shirts += 1
        clean_shirts -= 1
        dirty_shirts += 1

    return laundry_days


# print(num_laundry_days(1,10,[10]))
# print(num_laundry_days(1,10,[2,5,9]))

# ____________________LAUNDRY____________


# __________________PIPE_OUTPUTS_________
# One day, Rube Goldberg  was asked to design the drain pipes for an apartment building.
# He did so with his usual creativity.
# Then, rather than turning in a diagram to his benefactors,
# he gave them some lists of numbers.

# "The first number", he said, "is the number of apartments in the building.
# Each can handle eight gallons of water per minute.
# The rest of the numbers are when pipes split or combine."

# "If you see one number," he continued,
# "then that pipe joins the pipe to its right.

# "If you see two numbers,
# then the first number is the number of the pipe splits into two pipes.
# The second number is how much of the flow goes into the left pipe.
# The remainder will go into the second pipe.
# "After each step, the pipes are renumbered."

# start: 3             1 |8|            2 |8|            3 |8|      numbers beside the pipes are the pipe number.
#                        | |             |   |             | |      pipes are renumbered after each step.
# List of numbers:     1 |8|          2 |4| |4| 3        4 |8|
#   2  4                  \ \          / /  | |            | |
# ( split pipe 2           \ \        / /   | |            | |
#   left: 4                 \ \      / /    | |            | |
#   right: 8 - 4 )           \ \   / /      | |            | |
#  1                        1 | 12  |     2 |4|          3 |8|
# ( join pipe 1 to             \    |       | |            | |
#   the right )                  \  \       | |            | |
#  1                               \ \      | |            | |
# ( join pipe 1 to                  \ \     | |            | |
#   the right )                   1  |   16   |          2 |8|
#  1 2                               |   /\   |            | |
#  ( split pipe 1                    |  /  |  |            | |
#   left: 2                        1 |2|   |14| 2        3 |8|
#   right: 16 - 2)                                                  answer: [2, 14, 8]

# Given the number of pipes num_pipes and a list of steps,
# complete the function pipe_outputs to return a list that contains
# the flow of each pipe in the order
# starting with the first pipe to the last pipe.

# At the beginning, each of the num_pipes has a flow of 8
# In the list of steps, each step is a list
# If the step has one value in it,
# then it joins that pipe with the one to its right
# If the step has two values in it,
# then the first value is the pipe to split,
# and the second value is the flow that goes into the pipe to the left,
# while the remainder of the flow goes into the pipe to the right
# The input from the example above would look like this:

# num_pipes = 3
# steps = [[2, 4], [1], [1], [1, 2]]


def pipe_outputs(num_pipes, steps):
    plumbing = [8] * num_pipes
    for step in steps:
        pipe = step[0] - 1
        split = len(step) - 1
        if split:
            flow_left = step[1]
            plumbing[pipe] -= flow_left
            plumbing.insert(pipe, flow_left)
        else:
            flow_right = plumbing.pop(pipe)
            plumbing[pipe] += flow_right
    return plumbing


# ____________________PIPE_OUTPUTS______________________

# _____________________OG TEXT________OG TEXT_________
# Before smart phones, when you wanted to text someone,
# you had to press the same number over and
# over again to get a letter from the keypad.
# {  1       2       3  }
# {         abc     def }

# {  4       5       6  }
# { ghi     jkl     mno }

# {  7       8       9  }
# { pqrs    tuv    wxyz }

# the number 2 has three letters associated with it: A, B, and C.
# Originally, you would press the 2 button once to get the letter A,
# push the 2 button twice to get the letter B,
# and push the 2 button three times to get the letter C.

# At some point, someone tried to make it easier
# by including a dictionary in the phone.
# You could just type the numbers once,
# and the phone would try to guess the word for you.

# For example, let's say the phone's dictionary contained
# the words "ARROW", "BOTOX", "DOMES", and "FOODS".

# If you typed the numbers 26869,
# then the phone would come up with the word BOTOX for you.

# If you typed the numbers 27769,
# then the phone would come up with the word ARROW for you.

# If you typed the numbers 36637,
# it would come up with both the words "DOMES" and "FOODS".

# Given that mapping of numbers to letters and a list of valid words,
# it's up to you to figure out how many of those words
# could be created from the digits someone types into the phone.


def translate(words, digits):
    words_list = words
    digis = str(digits)
    letters_on_num = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    count = 0
    for word in words_list:
        if len(word) != len(digis):
            continue
        word = word.lower()
        passed = True
        for i, num in enumerate(digis):
            if word[i] not in letters_on_num[num]:
                passed = False
                break
        if passed:
            count += 1
    return count


# ------------- tests ----------------
# ['TOMO', 'MONO', 'DAK'], 6666 === 1
# print(translate(["TOMO", "MONO", "DAK"], 6666) == 1)

# ['DOM', 'FON', 'TOM'], 366 === 2
# print(translate(["DOM", "FON", "TOM"], 366) == 2)

# ['JA', 'LA'], 52 === 2
# print(translate(['JA', 'LA'], 52) == 2)
# ____________________OG TEXT_________OG TEXT_________


# __________________________________________________________SLOTS WITH CLASSES____________________________________________________

# Ken travels a lot. When he's in Nevada waiting for his airplane,
# he likes to play the slot machines in the airport.
# There are only three slot machines, and Ken is the only player.

# Each slot machine takes one quarter.
# Ken usually has some loose change in his pocket from the toll booths
# that he encounters in his rental car.

# His strategy is simple. He starts at the first slot machine
# and drops in a quarter, pulls the lever,
# and if any quarters come out, he collects them.
# Then, he moves to the second slot machine and does the same thing.
# Then, he moves to the third slot machine and does the same thing.
# Once he's done with the third slot machine, he moves back to the first slot machine.
# He just keeps going until he runs out of quarters.

# What Ken doesn't know is that the airport has rigged the slot machines.

# The first slot machine pays 20 quarters every 27th time it's played.
# The second slot machine pays 50 quarters every 100th time it's played.
# The third slot machine pays 7 quarters every 8th time it's played.
# How many times can Ken play before he runs out of quarters?

# Given the value num_quarters,
# complete the function calculate_plays to return
# the number of times Ken plays the slot machines before running out of quarters.

# Ken plays the first slot machine, then the second, then the third,
# then back to the first, and keeps going until he runs out of quarters.

# The first slot machine pays 20 quarters every 27th time it's played.
# The second slot machine pays 50 quarters every 100th time it's played.
# The third slot machine pays 7 quarters every 8th time it's played.

# Constraints: 1 <= num_quarters <= 1000


class SlotMachine:
    def __init__(self, num_for_payout, payout_ammount):
        self.total_plays = 0
        self.plays = 0
        self.payout = num_for_payout
        self.payout_ammount = payout_ammount

    def play_routine(self, quarters):
        if quarters > 0:
            quarters -= 1
            self.plays += 1
            self.total_plays += 1
            if self.plays == self.payout:
                self.plays = 0
                quarters += self.payout_ammount
        return quarters


def class_calculate_plays(num_quarters):
    first = SlotMachine(27, 20)
    second = SlotMachine(100, 50)
    third = SlotMachine(8, 7)
    kens_quarters = num_quarters
    while kens_quarters > 0:
        kens_quarters = first.play_routine(kens_quarters)
        kens_quarters = second.play_routine(kens_quarters)
        kens_quarters = third.play_routine(kens_quarters)

    return first.total_plays + second.total_plays + third.total_plays


# onek = 1000 # plays should equal = 3211
# hundo = 100 #plays should equal = 189
# fivehundo = 500 #plays should equal = 1487
# print(calculate_plays(onek),"-- 1000 coin start")
# print(calculate_plays(hundo),"-- 100 coin start")
# print(calculate_plays(fivehundo),"-- 500 coin start")

# ___________________________________________________SLOTS WITH CLASSES_____________________________________________________________________


# ________________SLOTS WITHOUT CLASSES________________


def calculate_plays(num_quarters):
    num_plays_m1 = 0
    num_plays_m2 = 0
    num_plays_m3 = 0
    total_plays = 0
    kens_quarters = num_quarters
    while kens_quarters:
        # play the first machine
        # using the loop condition as the quarter check
        kens_quarters -= 1
        num_plays_m1 += 1
        total_plays += 1
        # payout on the 27th play and reset the count
        if num_plays_m1 == 27:
            num_plays_m1 = 0
            kens_quarters += 20
        # quarter check 2nd machine (Zero will return a false)
        if kens_quarters:
            kens_quarters -= 1
            num_plays_m2 += 1
            total_plays += 1
            # payout on the 100th play and reset the count
            if num_plays_m2 == 100:
                num_plays_m2 = 0
                kens_quarters += 50
        # quarter check 3rd machine (Zero will return a false)
        if kens_quarters:
            kens_quarters -= 1
            num_plays_m3 += 1
            total_plays += 1
            # payout on the 8th play and reset the count
            if num_plays_m3 == 8:
                num_plays_m3 = 0
                kens_quarters += 7
    return total_plays


# _________________________________________________________PLAYING SLOTS____________________________________________________
