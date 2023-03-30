# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# def minimum_value(num1,num2):
#     value1 = int(num1)
#     value2 = int(num2)
#     if value1 <= value2:
#         return value1
#     else:
#         return value2
# min = minimum_value(input("num1 \n"),input("num2 \n"))
# print('The minimum of the two values is', min)

def total_song_knowers(num_villagers, attendees_lists):
    amt_uniq_songs = 1
    ph = 0
    vs = {}
    new_days_songs = {0}
    out = []
    for day in attendees_lists:
        new_days_songs.clear()
        for attended in day:
            if attended == 0:
                new_days_songs.add(amt_uniq_songs)
                amt_uniq_songs += 1
                continue
            songs = vs.setdefault(attended,[])
            songs = list(songs)
            for song in songs:
                new_days_songs.add(song)
        nds = list(new_days_songs)
        for attendee in day:
            vs[attendee] = nds
    for i in range(num_villagers):
        known = list(vs.get(i))
        print
        known = len(known)
        if known>ph:
            out.clear()
            ph = known
            out.append(ph)
        elif known == ph:
            out.append(ph)
    return len(out)




    #giving single digits now. len(shared songs)


    # #outside variable to track new songs.
    # song = 0
    # #dictionary to hold a Villager : his known songs
    # vs = {}
    # #place holder for most songs known
    # ph = 0
    # #list for those who know all the songs
    # rockstars = []
    # todays_known_songs = {}

    # for day in attendees_lists:
    #     todays_known_songs.clear()
    #     for attended in day:

    #         # listing songs this villager knows.
    #         their_songs = list(vs.get(attended))

    #         # adding all this villagers songs
    #         for song in their_songs:
    #             todays_known_songs.add(song)

    #         # if minstrel attends, add a new song.
    #         if attended == 0:
    #             song += 1
    #             todays_known_songs.add(song)
    #         # dropping out of this for loop
    #     # to do the following checks, after each villager
    #     # adds their songs.

    #     # updating the songs known by each villager.
    #     tks = list(todays_known_songs)
    #     for attendee in day:
    #         vs.update(attendee, tks)
    #         # checking for rockstars
    #         known = len(list(vs.get(attendee)))
    #         if known > ph:
    #             ph = known
    #             rockstars.clear
    #             rockstars.append(attendee)
    # return
