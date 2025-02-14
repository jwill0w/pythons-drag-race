### Libraries
import random
import os
from collections import OrderedDict

### Globals
pooters = {} # Each item will be it's own dictionary; {Pootita : {Fashion : 1-15}}
eliminated_pooters = []
track_records = {} # Each item will be dedicated to a pooter; {Pootita : {1 : "WIN", 2: "SAFE"}}
challenges = ["Fashion", "Makeup", "Music", "Emotion", "Lust", "Acting"]
overall_scores = {}
finalists = random.randint(3, 4)
season_format = "Regular"

season_number = input("Enter season number:")

episode = 1
double_save = False

## Customization

# User adds all their desired pooters
while True:
    # Ask the user to input their pooter's name
    entry = input("Pooter #"+str(len(pooters)+1)+" (Leave blank to stop adding pooters): ")

    # Check if user wishes to finish entering pooters
    if entry == "":
        # Check if enough pooters have been added
        if len(pooters) > 5:
            print("All pooters have been added!")
            print("")
            break
    else:
        # Check if the pooter is valid
        if pooters.get(entry) == None:
            # Add pooter to pooters dictionary
            pooters[entry] = {}

            # Assign pooter's stats for the competition
            entry_dictionary = pooters[entry]
            entry_dictionary["Fashion"] = random.randint(1, 15)
            entry_dictionary["Makeup"] = random.randint(1, 15)
            entry_dictionary["Music"] = random.randint(1, 15)
            entry_dictionary["Emotion"] = random.randint(1, 15)
            entry_dictionary["Lust"] = random.randint(1, 15)
            entry_dictionary["Acting"] = random.randint(1, 15)

            overall_scores[entry] = 0
            track_records[entry] = {}

            #print("")
            #for y in pooters[entry]:
                #print(y+": "+str(pooters[entry][y]))

            choice = ""
            while choice != "y" and choice != "n":
                choice = input("Would you like to edit "+entry+"'s stats? (y/n): ")

                if choice == "y":
                    for x in entry_dictionary:
                        stat = ""
                        while stat == "":
                            stat = input(x+" (1-15): ")
                            try:
                                if int(stat) < 1 or int(stat) > 15:
                                    stat = ""
                            except:
                                stat = ""
                        entry_dictionary[x] = int(stat)

            print("Pooter has been successfully added.")
            print("")

# Predicted finalists
total_points = {}
for x in pooters:
    total_points[x] = 0
    for y in pooters[x]:
        total_points[x] += pooters[x][y]

sorted_points = sorted(total_points.items(), key=lambda item: item[1])

print("")

valid = False
while not valid:
    choice = input("Would you like to see the predicted finalists? (y/n)")
    if choice == "y":
        print("(Most likely to be) finalists:")

        for i in range(finalists):
            print(sorted_points[i-1][0])

        valid = True
        print("")
    elif choice == "n":
        valid = True
        print("")


# r = Regular, a = All-stars
while True:
    entry = input("Format (r/a): ")

    if entry == "r" or entry == "a":
        if entry == "a" and len(pooters) == 8:
            season_format = "All-stars"
            break
        elif entry == "r":
            break

# Output each pooter's statistics before starting (MAY NOT BE IN FINAL VER.)
'''
for x in pooters:
    print("-----")
    print(x)
    print("")
    for y in pooters[x]:
        print(y+": "+str(pooters[x][y]))
    print("-----")
    print("")
input()
'''

## Simulator

if season_format == "All-stars":
    stars = {}
    blocked = None

pooters_remaining = []

for x in pooters:
    pooters_remaining.append(x)
    if season_format == "All-stars":
        stars[x] = 0

challenge_weights = {}
used_challenges = []

for x in challenges:
    challenge_weights[x] = 0

while len(pooters_remaining) > finalists if season_format == "Regular" else episode != 12:
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
    print("Episode "+str(episode)+"!")
    input()

    sorted_challenges = sorted(challenge_weights.items(), key=lambda item: item[1], reverse=True)

    random_challenge = sorted_challenges[0][0]
    for x in challenge_weights:
        if x != random_challenge:
            challenge_weights[x] += random.randint(20, 35)
            challenge_weights[x] -= (challenge_weights[x] % 5)

    prefix = "an " if random_challenge[0] in "AEIOU" else "a "

    used_challenges.append(random_challenge)

    print("Today's challenge will be "+prefix+random_challenge+" related challenge!")
    input()

    episode_type = "Regular"

    if season_format == "Regular":
        if len(pooters_remaining) > 6 and random.randint(1, 8) == 1:
            episode_type = "DoubleWin"

        winner = None
        highs = None
        safe = None
        low = None
        bottoms = None
        eliminated_pooter = None

        scores = {}

        outstanding = []
        amazing = []
        decent = []
        poor = []
        terrible = []
        
        for x in pooters_remaining:
            score = random.randint(11, 13) # Range: 11 - 21
            pooter_multiplier = pooters[x][random_challenge] / 25
            new_score = round(score + (score * pooter_multiplier))
            scores[x] = new_score

            overall_scores[x] += score

            if new_score > 15:
                outstanding.append(x)
            elif new_score > 12:
                amazing.append(x)
            elif new_score > 9:
                decent.append(x)
            elif new_score > 6:
                poor.append(x)
            else:
                terrible.append(x)

        if len(outstanding) >= 1:
            print(", ".join(outstanding)+" had an outstanding performance!")
            input()

        if len(amazing) >= 1:
            print(", ".join(amazing)+" had an amazing performance!")
            input()

        if len(decent) >= 1:
            print(", ".join(decent)+" had a decent performance.")
            input()

        if len(poor) >= 1:
            print(", ".join(poor)+" had a poor performance..")
            input()

        if len(terrible) >= 1:
            print(", ".join(terrible)+" had a terrible performance..")
            input()

        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        if episode_type == "Regular":
            tops = [
            sorted_scores[0][0], 
            sorted_scores[1][0], 
            sorted_scores[2][0]
            ]

            bottoms = [
            sorted_scores[len(pooters_remaining)-1][0], 
            sorted_scores[len(pooters_remaining)-2][0], 
            sorted_scores[len(pooters_remaining)-3][0]
            ]

            overall_scores[sorted_scores[0][0]] += 6
            overall_scores[sorted_scores[1][0]] += 4
            overall_scores[sorted_scores[2][0]] += 4

            overall_scores[sorted_scores[len(pooters_remaining)-1][0]] -= 4
            overall_scores[sorted_scores[len(pooters_remaining)-2][0]] -= 5
            overall_scores[sorted_scores[len(pooters_remaining)-3][0]] -= 6

            if len(pooters_remaining) == 5:
                bottoms.pop(2)
            elif len(pooters_remaining) == 4:
                bottoms.pop(2)
                tops.pop(2)
        elif episode_type == "DoubleWin":
            tops = [
            sorted_scores[0][0], 
            sorted_scores[1][0], 
            sorted_scores[2][0] ,
            sorted_scores[3][0]
            ]

            overall_scores[sorted_scores[0][0]] += 6
            overall_scores[sorted_scores[1][0]] += 4
            overall_scores[sorted_scores[2][0]] += 4
            overall_scores[sorted_scores[3][0]] += 4

            bottoms = [
            sorted_scores[len(pooters_remaining)-1][0], 
            sorted_scores[len(pooters_remaining)-2][0], 
            sorted_scores[len(pooters_remaining)-3][0]
            ]

            overall_scores[sorted_scores[len(pooters_remaining)-1][0]] -= 4
            overall_scores[sorted_scores[len(pooters_remaining)-2][0]] -= 5
            overall_scores[sorted_scores[len(pooters_remaining)-3][0]] -= 6
        
        print("I've made some decisions.. mmhh..")

        input()

        tops_and_bottoms = []
        safe = []
        for x in pooters_remaining:
            if x in tops or x in bottoms:
                tops_and_bottoms.append(x)
            else:
                safe.append(x)
        random.shuffle(tops_and_bottoms)

        print(", ".join(tops_and_bottoms)+".. you are the tops and bottoms for today's challenge.")

        if len(safe) > 0:
            safe_prefix = "all of you" if len(safe) > 2 else "you"
            print(", ".join(safe)+".. "+safe_prefix+" are safe. Good work.")

        input()
        print("Now, let's go over my feelings about your performances today.")
        input()

        for x in tops_and_bottoms:
            if tops_and_bottoms.index(x) == 0:
                print("Let's start with "+x+".")
            else:
                print("On to "+x+"!" if random.randint(1, 2) == 1 else "Let's go down to "+x+".")
                
            if x in tops:
                print("You did really great today, I'm proud of you." if random.randint(1, 2) == 1 or tops.index(x) != 0 else "Wow, what a performance! Phenomenal work today.")
            else:
                print("I'm pretty disappointed tonight.." if random.randint(1, 2) == 1 else "I need you to really bring it next time.")
            input()

        print("Thank you pooters. I have made my decision.")

        input()

        if episode_type == "Regular":
            if episode != 1:
                if track_records[tops[0]][episode-1] == "WIN":
                    get = tops[0], tops[1]
                    tops[1], tops[0] = get

            winner = tops[0]

            print(winner+".. you're a winner baby!!")
            input()
        elif episode_type == "DoubleWin":
            winner = [tops[0], tops[1]]

            print(", ".join(winner)+".. you're both winners baby!!")
            input()

        highs = []
        for x in tops:
            if episode_type == "Regular":
                if x != winner:
                    highs.append(x)
            if episode_type == "DoubleWin":
                if winner.count(x) == 0:
                    highs.append(x)

        high_prefix = "all of you" if len(highs) > 2 else "you"
        print(", ".join(highs)+".. "+high_prefix+" are safe. Good work.")

        input()
        print("Which means "+", ".join(bottoms)+".. you are the bottoms of the day.")
        input()

        # Save someone from the bottom two.
        if len(bottoms) > 2:
            low = 0

            for x in overall_scores:
                if x in bottoms:
                    if overall_scores[x] > low:
                        low = overall_scores[x]

            for x in overall_scores:
                if x in bottoms:
                    if overall_scores[x] == low:
                        low = x

            print("Hmm..")
            input()
            print("..")
            input()

            print(low+", you are safe, but do better next time. GO!")
            bottoms.remove(low)
            input()
            print("Which means "+", ".join(bottoms)+".. you are the bottom two.")
            input()

        # The bottom two
        first_nominee = bottoms[0]
        second_nominee = bottoms[1]

        eliminated_pooter = None

        # Compare the bottoms and see who SHOULD be eliminated

        higher_score = None
        more_wins = None
        more_bottoms = None

        # Compare overall scores
        if overall_scores[first_nominee] > overall_scores[second_nominee]:
            higher_score = first_nominee
        elif overall_scores[first_nominee] < overall_scores[second_nominee]:
            higher_score = second_nominee

        first_nominee_wins = 0
        second_nominee_wins = 0

        first_nominee_bottoms = 0
        second_nominee_bottoms = 0

        # Compare wins
        for x in track_records[first_nominee]:
            if track_records[first_nominee][x] == "WIN":
                first_nominee_wins += 1

        for x in track_records[second_nominee]:
            if track_records[second_nominee][x] == "WIN":
                second_nominee_wins += 1
        
        if first_nominee_wins > second_nominee_wins:
            more_wins = first_nominee
        elif second_nominee_wins > first_nominee_wins:
            more_wins = second_nominee

        # Compare bottoms
        for x in track_records[first_nominee]:
            if track_records[first_nominee][x] == "BTM":
                first_nominee_bottoms += 1

        for x in track_records[second_nominee]:
            if track_records[second_nominee][x] == "BTM":
                second_nominee_bottoms += 1
        
        if first_nominee_bottoms > second_nominee_bottoms:
            more_bottoms = first_nominee
        elif second_nominee_bottoms > first_nominee_bottoms:
            more_bottoms = second_nominee
            
        print("..")
        input()

        # The final verdict, decide who has been eliminated
        if higher_score == None and more_wins == None and more_bottoms == None:
            if random.randint(1, 2) == 1:
                eliminated_pooter = first_nominee
                #print("Condition #1")
            else:
                eliminated_pooter = second_nominee
                #print("Condition #2")
        elif higher_score != None:
            if higher_score == first_nominee: # 1. If nominee 1 has a higher score ..
                if more_wins == first_nominee: # 2. .. and has more wins ..
                    eliminated_pooter = second_nominee # 3. .. then they are safe.
                    #print("Condition #3")
                else: # 2. .. and doesn't have more wins ..
                    if more_bottoms == first_nominee: # 3. .. and has more bottoms ..
                        eliminated_pooter = first_nominee # 4. .. then they are eliminated.
                        #print("Condition #4")
                    else: # 3. .. and has the same or less bottoms..
                        eliminated_pooter = second_nominee # 4. .. then they are safe.
                        #print("Condition #5")
            elif higher_score == second_nominee: # 1. If nominee 2 has a higher score ..
                if more_wins == second_nominee: # 2. .. and has more wins ..
                    eliminated_pooter = first_nominee # 3. .. then they are safe.
                    #print("Condition #6")
                else: # 2. .. and doesn't have more wins ..
                    if more_bottoms == second_nominee: # 3. .. and has more bottoms ..
                        eliminated_pooter = second_nominee # 4. .. then they are eliminated.
                        #print("Condition #7")
                    else: # 3. .. and has the same or less bottoms..
                        eliminated_pooter = first_nominee # 4. .. then they are safe.
                        #print("Condition #8")
        elif more_wins != None:
            if more_wins == first_nominee: # 1. If nominee 1 has more wins ..
                if more_bottoms == second_nominee: # 2. .. and has less bottoms ..
                    eliminated_pooter = second_nominee # 3. .. then they are safe.
                    #print("Condition #9")
                else: # 2. .. and has same or more bottoms ..
                    eliminated_pooter = first_nominee # 3. .. then they are eliminated.
                    #print("Condition #10")
            else: # 1. If nominee 2 has more wins ..
                if more_bottoms == first_nominee: # 2. .. and has less bottoms ..
                    eliminated_pooter = first_nominee # 3. .. then they are safe.
                    #print("Condition #11")
                else: # 2. .. and has same or more bottoms ..
                    eliminated_pooter = second_nominee # 3. .. then they are eliminated.
                    #print("Condition #12")
        elif more_bottoms != None:
            if more_bottoms == first_nominee: # 1. If nominee 1 has more bottoms ..
                eliminated_pooter = first_nominee # 2. .. then they are eliminated.
                #print("Condition #13")
            else: # 1. If nominee 2 has more bottoms ..
                eliminated_pooter = second_nominee # 2. .. then they are eliminated.
                #print("Condition #14")

        # Check whether it could be a double save
        if abs(overall_scores[first_nominee] - overall_scores[second_nominee]) < 20 and double_save == False:
            if first_nominee_wins > 0 and second_nominee_wins > 0:
                if first_nominee_bottoms < 2 and second_nominee_bottoms < 2:
                    eliminated_pooter = None
                    double_save = True

        # Deliver the blow ;)
        if eliminated_pooter == first_nominee:
            saved_pooter = second_nominee
        elif eliminated_pooter == second_nominee:
            saved_pooter = first_nominee
        else:
            saved_pooter = None

        if saved_pooter and eliminated_pooter:
            print(saved_pooter+", you have survived the Poot-Off. LEAVE!!!")
            input()
            print(eliminated_pooter+", I'm sorry but you did not make it through the Poot-Off. Now, shoo fly..")
        
            pooters_remaining.remove(eliminated_pooter)
            eliminated_pooters.append(eliminated_pooter)
        else:
            print("Oh fuck it..")
            input()
            print(first_nominee+", "+second_nominee+", you have BOTH survived the Poot-Off! Now VANISH!")

        input()

        print("Episode Summary <3")

        if type(winner) == list:
            print("Winners: "+", ".join(winner))
        else:
            print("Winner: "+winner)

        print("Highs: "+", ".join(highs))

        if len(safe) > 0:
            print("Safe: "+", ".join(safe))

        if low:
            print("Low: "+low)

        print("Bottoms: "+", ".join(bottoms))
        
        if eliminated_pooter:
            print("Eliminated: "+eliminated_pooter)
        else:
            print("Eliminated: Nobody!")

        if episode_type == "Regular":
            track_records[winner][episode] = "WIN"
        elif episode_type == "DoubleWin":
            for x in winner:
                track_records[x][episode] = "WIN"

        for x in highs:
            track_records[x][episode] = "HIGH"

        for x in safe:
            track_records[x][episode] = "SAFE"

        if low:
            track_records[low][episode] = "LOW"

        for x in bottoms:
            track_records[x][episode] = "BTM"

        if eliminated_pooter:
            track_records[eliminated_pooter][episode] = "ELIM"

        for x in pooters:
            if x not in pooters_remaining and track_records[x].get(episode) == None:
                track_records[x][episode] = "N/A"
    elif season_format == "All-stars":
        if episode == 8:
            print("As of this week, no more pooters will be blocked!")
            blocked = None
            input()

        if episode == 5:
            print("Today, the top two will receive 2 stars! One to keep, and one to give to a fellow pooter..")
            input()

        if episode == 11:
            print("Today, since this is our final challenge, the top two will receive 2 stars instead of 1!")
            input()

        first_top = None
        second_top = None
        highs = None
        safe = None

        scores = {}

        outstanding = []
        amazing = []
        decent = []
        poor = []
        terrible = []
        
        for x in pooters_remaining:
            score = random.randint(1, 15)
            pooter_multiplier = pooters[x][random_challenge] / 10
            new_score = round(score + (score * pooter_multiplier))
            scores[x] = new_score

            overall_scores[x] += score

            if score > 12:
                outstanding.append(x)
            elif score > 9:
                amazing.append(x)
            elif score > 6:
                decent.append(x)
            elif score > 4:
                poor.append(x)
            else:
                terrible.append(x)

        if len(outstanding) >= 1:
            print(", ".join(outstanding)+" had an outstanding performance!")
            input()

        if len(amazing) >= 1:
            print(", ".join(amazing)+" had an amazing performance!")
            input()

        if len(decent) >= 1:
            print(", ".join(decent)+" had a decent performance.")
            input()

        if len(poor) >= 1:
            print(", ".join(poor)+" had a poor performance..")
            input()

        if len(terrible) >= 1:
            print(", ".join(terrible)+" had a terrible performance..")
            input()

        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        tops = [
            sorted_scores[0][0],
            sorted_scores[1][0],
            sorted_scores[2][0],
            sorted_scores[3][0],
            ]
        
        safe = [
            sorted_scores[4][0],
            sorted_scores[5][0],
            sorted_scores[6][0],
            sorted_scores[7][0],
            ]
        
        print("I've made some decisions.. mmhh..")

        input()

        random.shuffle(tops)

        print(", ".join(tops)+".. you are the tops for today's challenge!")

        if len(safe) > 0:
            safe_prefix = "all of you" if len(safe) > 2 else "you"
            print(", ".join(safe)+".. "+safe_prefix+" are safe. Good work.")

        input()
        print("Now, let's go over my feelings about your performances today.")
        input()

        for x in tops:
            if tops.index(x) == 0:
                print("Let's start with "+x+".")
            else:
                print("On to "+x+"!" if random.randint(1, 2) == 1 else "Let's go down to "+x+".")
                
            if tops.index(x) <= 2:
                print("You're really showing us how amazing you are today!" if random.randint(1, 2) == 1 or tops.index(x) != 0 else "Wow, what a performance! Phenomenal work today.")
            else:
                print("Nice work today, I'm proud of you." if random.randint(1, 2) == 1 else "I can't believe we didn't see this on your original season! Perfection.")
            input()

        print("Thank you pooters. I have made my decision.")

        input()

        first_top = tops[0]
        second_top = tops[1]

        print(first_top+", "+second_top+", you are the top two All-stars of the week!")
        
        highs = [tops[2], tops[3]]

        input()

        if first_top != blocked:
            if episode != 11:
                stars[first_top] += 1
                print(first_top+", you will receive a star since you have not been blocked.")
                input()
            else:
                stars[first_top] += 2
                input()

        if second_top != blocked:
            if episode != 11:
                stars[second_top] += 1
                print(second_top+", you will receive a star since you have not been blocked.")
                input()
            else:
                stars[second_top] += 2

        if episode == 11:
            print("You have both been given 2 stars, since it is our last challenge!")
            input()

        if episode == 5:
            print("The two of you wil also be giving away an extra star to a fellow pooter..")
            input()
            print("So! "+first_top+", who will you give your extra star to?")
            input()
            print(first_top+": I will be giving my star to..")
            input()
            print("..")
            input()

            options = []

            for x in safe:
                options.append(x)

            for x in highs:
                options.append(x)

            options.append(second_top)

            receiving = random.choice(options)
            stars[receiving] += 1

            print(first_top+": "+receiving+"!")
            input()
            print("Alright! Now, "+second_top+", who will you give your extra star to?")
            input()
            print(second_top+": I will be giving my star to..")
            input()
            print("..")
            input()

            options = []

            for x in safe:
                options.append(x)

            for x in highs:
                options.append(x)

            options.append(first_top)

            second_receiving = random.choice(options)
            stars[second_receiving] += 1

            print(second_top+": "+second_receiving+"!")
            input()
            print("How sweet.. alright, let's move on. UGH.")

        print(", ".join(highs)+", you two are safe. Well done!")
        input()
        print("And now, the top two pooters will have a poot-off for the WIN!!")
        input()
        print("..")

        winner = None

        if random.randint(1, 2) == 1:
            winner = first_top
        else:
            winner = second_top

        input(winner+", you're a winner sweet-cheeks!")
        input()
        if episode < 8:
            print(winner+", the fate of the Poot-Plunger rests in your hands. Who will you give the plunge to?")
            input()
            print(winner+": I have chosen to give the Poot-Plunger to..")
            input()
            print("..")
            input()

            options = []

            for x in safe:
                options.append(x)

            for x in highs:
                options.append(x)

            blocked = random.choice(options)

            print(winner+": "+blocked+"..")
            input()
            print("So it has been done. "+blocked+", next week you can compete and even win, but you will not receive a badge..")
            input()

        if episode == 11:
            print("Now, tomorrow will be the finale, so I am going to announce the four pooters that will have earned the most stars, and will proceed to the finale Poot-Off smackdown!")
            input()

            four_finalists = []

            print("Let's take a look at our pooter's star count:")
            input()

            sorted_stars = sorted(stars.items(), key=lambda item: item[1], reverse=True)

            for x in sorted_stars:
                print(x[0]+": "+str(x[1]))

            input()

            # Check who should make it into the final four
            # Goes in order from most to least stars
            for x in sorted_stars:
                if len(four_finalists) < 4:
                    four_finalists.append(x[0])

            print("So, the pooters who will be moving on to the Poot-Off smackdown next episode are..")
            input()
            print(", ".join(four_finalists)+"!")
            input()

            eliminated = []

            for x in sorted_stars:
                if x[0] not in four_finalists:
                    eliminated.append(x[0])

        print("Episode Summary <3")

        print("Top Two: "+first_top+", "+second_top)
        print("Highs: "+", ".join(highs))
        print("Safe: "+", ".join(safe))
        print("Poot-Off Winner: "+winner)
        
        if blocked:
            print("Blocked: "+blocked)

        track_records[first_top][episode] = "TOP 2"
        track_records[second_top][episode] = "TOP 2"

        if first_top == winner:
            track_records[first_top][episode] = "WIN"
        else:
            track_records[second_top][episode] = "WIN"

        for x in highs:
            track_records[x][episode] = "HIGH"

        for x in safe:
            track_records[x][episode] = "SAFE"

        if episode == 11:
            print("Eliminated: "+", ".join(eliminated))

            for x in eliminated:
                track_records[x][episode] = track_records[x][episode]+" + ELIM"

        if episode == 5:
            track_records[receiving][episode] = track_records[receiving][episode]+" + GIFTED STAR"
            track_records[second_receiving][episode] = track_records[second_receiving][episode]+" + GIFTED STAR"

        if blocked != None:
            track_records[blocked][episode] = track_records[blocked][episode]+" + BLOCK"

        print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^")

        input()

        print("Star Count:")

        sorted_stars = sorted(stars.items(), key=lambda item: item[1], reverse=True)

        for x in sorted_stars:
            print(x[0]+": "+str(x[1]))

    random.shuffle(pooters_remaining)
    episode += 1

print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^")

input()

# Finale
print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
print("Episode "+str(episode)+"!")
input()

placements = {}

if season_format == "Regular":
    print("Today, we have reached the finale! We will be giving out the Very Important Poot reward, getting to know our finalists.. and of course, crowning a winner!")
    input()
    print("But first, let's welcome back our eliminated pooters! Please welcome..")
    for x in eliminated_pooters:
        print(x+"!")
        input()
    print("And last but certainly not least, welcome our finalists! We have..")
    input()
    for x in pooters_remaining:
        print(x+"!")
        input()
    print("We're going to have each of our finalists plead their case for the crown, and tell us why they should receive it!")
    input()
    for x in pooters_remaining:
        if pooters_remaining.index(x) == 0:
            print("Let's start with "+x+".")
        elif pooters_remaining.index(x) == len(pooters_remaining):
            print("And finally, "+x+"!")
        else:
            print("On to "+x+"!")
        print(x+", why should you take home the crown?")
        pooter_text = ""
        if random.randint(1, 3) == 1:
            pooter_text = "I think I should take the crown because I've been consistent throughout the competition, I've presented my skillset and shown I can adapt to whatever is thrown at me."
        elif random.randint(1, 3) == 2:
            pooter_text = "I WILL be taking the crown, I know I deserve it more than any of these girls, and I have shown that through my work."
        else:
            pooter_text = "I came here to show the kids watching this show that you CAN make it, no matter who you are or where you come from, and I've accomplished that. Please, consider me for the crown."
        print(x+": "+pooter_text)
        input()
    print("Wow, what powerful messages.. thank you girls. I've made some decisions.")
    input()
    print("I don't think I can decide with all "+str(finalists)+" of you here. So, with that said..")

    finalist_overall_scores = {}
    for x in pooters_remaining:
        finalist_overall_scores[x] = overall_scores[x]

    sorted_overall_scores = sorted_scores = sorted(finalist_overall_scores.items(), key=lambda item: item[1], reverse=True)
    continuing_pooters = []
    not_continuing_pooters = []

    best_performance = sorted_overall_scores[0]
    continuing_pooters.append(best_performance[0])
    sorted_overall_scores.remove(best_performance)

    best_performance = sorted_overall_scores[0]
    continuing_pooters.append(best_performance[0])
    sorted_overall_scores.remove(best_performance)

    input()
    print("..")
    input()
    print("The two moving on to the final Poot-Off are..")
    input()
    print("..")
    input()
    random.shuffle(continuing_pooters)
    print(".. and ".join(continuing_pooters)+"!")
    input()
    for x in pooters_remaining:
        if x not in continuing_pooters:
            not_continuing_pooters.append(x)
    print("Which means "+", ".join(not_continuing_pooters)+", I'm sorry, but you will not be taking the crown. I must ask you to shoo fly..")
    for x in not_continuing_pooters:
        pooters_remaining.remove(x)

    input()
    print("Now, before the final Poot-Off, it's time to crown our VIP!")
    input()
    print("The fans have voted for their favourite pooter, and we have reached a conclusion!")
    input()
    print("The winner of the VIP title is..")
    input()

    vip = random.choice(eliminated_pooters)
    for x in not_continuing_pooters:
        eliminated_pooters.append(x)
    print(vip+"!")
    input()
    print("Now that we've done that, I think it's finally time to have our Poot-Off!")
    input()
    print("..")
    input()
    print("DAMN! Well done ladies, I think I've made a decision..")
    input()
    print("..")
    input()
    print("The winner of Poothon: Season "+season_number+" is..")
    input()
    print("..")
    input()

    first_pooter = continuing_pooters[0]
    second_pooter = continuing_pooters[1]

    first_pooter_chance = 0
    second_pooter_chance = 0

    if first_pooter == best_performance:
        first_pooter_chance = random.randint(65, 120)
    else:
        first_pooter_chance = random.randint(40, 75)
        
    if second_pooter == best_performance:
        second_pooter_chance = random.randint(65, 120)
    else:
        second_pooter_chance = random.randint(40, 75)

    winner = first_pooter if first_pooter_chance > second_pooter_chance else second_pooter

    print(str.upper(winner)+"!!")
    input()

    track_records[winner][episode] = "WINNER"
    track_records[second_pooter if winner == first_pooter else first_pooter][episode] = "RUNNER-UP"

    placements[1] = winner
    placements[2] = second_pooter if winner == first_pooter else first_pooter
    for x in reversed(eliminated_pooters):
        placements[len(placements)+1] = x
        
    for x in not_continuing_pooters:
        track_records[x][episode] = "FINALELIM"

    for x in pooters:
        if x not in pooters_remaining and track_records[x].get(episode) == None:
            track_records[x][episode] = "GUEST"

    track_records[vip][episode] = "VIP"
    
else:
    print("Welcome to the finale! Today, our final four pooters will battle it out for the crown! There will be blood, tears, guts and- ..oh, we're not doing the hunger games? Ah, well, there will be 3 fierce poot-offs, supported by the four eliminated queens who didn't make the finale! 'Cause they suck! Kidding, but let's get this show on the road shall we? First, please welcome back:")
    input()
    for x in eliminated:
        print(x+"!")
        input()
    print("And now, let's introduce our final four! Please welcome:")
    input()
    for x in four_finalists:
        print(x+"!")
        input()

    options = []
    for x in four_finalists:
        options.append(x)
    
    print("We will have Pootita, our intern, spin a wheel to decide the Poot-Off challengers.")
    input()
    print("Let's do this! YEAH!! Pootita, SPIN THAT WHEEL!")
    input()
    print("Pootita: O-okay..")
    input()
    print("Pootita: Th-the first round will be..")
    input()
    print("Pootita: ..")
    input()

    random.shuffle(options)

    first_challenger = options[0]
    second_challenger = options[1]
    third_challenger = options[2]
    fourth_challenger = options[3]

    print("Pootita: "+first_challenger+"..")
    input()
    print("Pootita: vs..")
    input()
    print("..")
    input()
    print("Pootita: "+second_challenger+"..")
    input()
    print("OH HOW GIDDY! The first poot-off will be "+first_challenger+" vs. "+second_challenger+"!")
    input()
    print("That means the second poot-off will be "+third_challenger+" vs. "+fourth_challenger+"!")
    input()
    print("Now, let's get round 1 started! MMM!")
    input()

    # Round 1

    print("ROUND 1: "+str.upper(first_challenger)+" vs. "+str.upper(second_challenger))
    input()
    poot_off_winner = None
    poot_off_loser = None
    if random.randint(1, 2) == 1:
        poot_off_winner = first_challenger
        poot_off_loser = second_challenger
    else:
        poot_off_winner = second_challenger
        poot_off_loser = first_challenger
    print("That was soooo curnty!!! I have picked a winner..")
    input()
    print("..")
    input()
    print(poot_off_winner+", you WIN!!! MMH!!")
    input()
    print(poot_off_loser+", I'm sorry my sweet booby cake, but you didn't survive this poot-off. You must now shoo fly, but well done for a great season!")
    input()

    # Standings

    print("Poot-Off Smackdown Standings")
    print("Final Two: "+poot_off_winner+" vs. ___")
    print("Next: "+third_challenger+" vs. "+fourth_challenger)
    print("Eliminated: "+poot_off_loser)
    input()

    # Round 2

    print("ROUND 2: "+str.upper(third_challenger)+" vs. "+str.upper(fourth_challenger))
    input()
    second_poot_off_winner = None
    second_poot_off_loser = None
    if random.randint(1, 2) == 1:
        second_poot_off_winner = third_challenger
        second_poot_off_loser = fourth_challenger
    else:
        second_poot_off_winner = fourth_challenger
        second_poot_off_loser = third_challenger
    print("That was soooo curnty!!! I have picked a winner..")
    input()
    print("..")
    input()
    print(second_poot_off_winner+", you WIN!!! MMH!!")
    input()
    print(second_poot_off_loser+", I'm sorry my sweet booby fry, but you didn't survive this poot-off. You must now shoo fly, but well done for a great season!")
    input()

    # Standings

    print("Poot-Off Smackdown Standings")
    print("Final Two: "+poot_off_winner+" vs. "+second_poot_off_winner)
    print("Next: "+poot_off_winner+" vs. "+second_poot_off_winner)
    print("Eliminated: "+poot_off_loser+", "+second_poot_off_loser)
    input()

    print("OOH HOW EXCITING! Mmh.. The final poot-off will be between "+poot_off_winner+" and "+second_poot_off_winner+"!")
    input()
    print("Let's get our poot freak on! ..ah.. I should probably calm down a little..")
    input()
    
    print("ROUND 3: "+str.upper(poot_off_winner)+" vs. "+str.upper(second_poot_off_winner))
    input()
    winner = None
    runner_up = None

    if stars[poot_off_winner] > stars[second_poot_off_winner]:
        best_record = poot_off_winner
    else:
        best_record = second_poot_off_winner

    poot_off_winner_odds = 0
    second_poot_off_winner_odds = 0

    if poot_off_winner == best_record:
        poot_off_winner_odds = random.randint(60, 100)
        second_poot_off_winner_odds = random.randint(40, 75)
    else:
        poot_off_winner_odds = random.randint(40, 75)
        second_poot_off_winner_odds = random.randint(60, 100)

    if poot_off_winner_odds > second_poot_off_winner_odds:
        winner = poot_off_winner
        runner_up = second_poot_off_winner
    else:
        winner = second_poot_off_winner
        runner_up = poot_off_winner

    print("That was soooo curnty!!! I have picked a winner..")
    input()
    print("..")
    input()
    print("The.. the winner.. of Poot.. is..")
    input()
    print("..")
    input()
    print("Ahh.. ahaha!")
    input()
    print("..")
    input()
    print(str.upper(winner)+"! Y-YOU WIN!! HAAHAAA!!!!!!")
    input()
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    input()

    placements[1] = winner
    placements[2] = runner_up
    placements[3] = poot_off_loser+", "+second_poot_off_loser

    track_records[winner][episode] = "WINNER"
    track_records[runner_up][episode] = "RUNNER-UP"
    track_records[poot_off_loser][episode] = "ELIM"
    track_records[second_poot_off_loser][episode] = "ELIM"

    for x in pooters_remaining:
        if x not in four_finalists:
            track_records[x][episode] = "GUEST"

for x in placements:
    suffix = "th"
    if x == 1:
        suffix = "st"
    elif x == 2:
        suffix = "nd"

    print(str(x)+suffix+": "+placements[x])

ordered_track_records = OrderedDict(sorted(track_records.items(), reverse=True, key = lambda x : len(x[1]))).keys()

for x in ordered_track_records:
    print(x)
    for y in track_records[x]:
        print("EPISODE "+str(y)+": "+track_records[x][y])
    print("")

input()
input("Thanks for playing!")

file = open(r"D:\Downloads\pythons-drag-race-main\pythons-drag-race-main\track_record.html", "w")

file.write("<html>")
file.write("<head>")
file.write("<style>")
file.write("table, td, th {")
file.write("    border: 2px solid #111;")
file.write("    text-align: center;")
file.write("    background-color: #f8f8f8;")
file.write("	font-family: 	Trebuchet MS, sans-serif;")
file.write("}")
file.write("table {")
file.write("    border-collapse: collapse;")
file.write("    width: 40%;")
file.write("}")
file.write("th, td {")
file.write("    padding: 15px;")
file.write("}")
file.write("body {")
file.write("    background-color: #a900ab;")
file.write("}")
file.write("</style>")
file.write("</head>")

file.write("<body>")

file.write("<table>")

file.write("<tr>")
file.write("<th rowspan='2'>Name</th>")
for i in range(episode):
    file.write("<th>Episode "+str(i+1)+"</th>")

file.write("<tr>")

for challenge in used_challenges:
    file.write("<th>"+challenge+"</th>")

file.write("<th>Finale</th>")

file.write("</tr>")

ordered_track_records = OrderedDict(sorted(track_records.items(), reverse=True, key = lambda x : len(x[1]))).keys()

for x in placements:
    file.write("<tr>")
    file.write("<td>"+placements[x]+"</td>")

    for y in track_records[placements[x]]:
        opener = "<td>"

        item = track_records[placements[x]]

        text = item[y]

        if item[y] == "WIN":
            opener = "<td style='background-color: royalblue; color: white; font-weight: bold;'>"
        elif item[y] == "HIGH":
            opener = "<td style='background-color: lightblue;'>"
        elif item[y] == "LOW":
            opener = "<td style='background-color: salmon;'>"
        elif item[y] == "BTM":
            opener = "<td style='background-color: tomato;'>"
        elif item[y] == "ELIM":
            opener = "<td style='background-color: red; font-weight: bold;'>"
        elif item[y] == "FINALELIM":
            opener = "<td style='background-color: saddlebrown; color: white; font-weight: bold;'>"
            text = "ELIM"
        elif item[y] == "WINNER":
            opener = "<td style='background-color: yellow; font-weight: bold;'>"
        elif item[y] == "RUNNER-UP":
            opener = "<td style='background-color: darkgrey; font-weight: bold;'>"
        elif item[y] == "N/A":
            opener = "<td style='background-color: darkgrey;'>"
            text = ""
        elif item[y] == "GUEST":
            opener = "<td style='background-color: #5f5f5f; color: black;'>"
            text = "GUEST"
        elif item[y] == "VIP":
            opener = "<td style='background-color: lime; color: black; font-weight: bold;'>"
            text = "VIP"

        file.write(opener+text+"</td>")

file.write("</tr>")

file.write("</table>")

file.write("</html>")

file.close()
