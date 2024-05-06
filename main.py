# File: main.py

import random
import inflect # type: ignore
import webbrowser

inflect_engine = inflect.engine()

names = []
overall_scores = {}
track_record = {}
episode = 1

assets = {
  
}

settings = {
  "finalists" : 3,
  "rigged" : True,
  "format" : "Regular"
}

double_shantay = False
      
# Prompt user: Rigged or fair?
valid = False
while not valid:
  rigged_prompt = input("Rigged or fair? (r/f):")
  if rigged_prompt == "r" or rigged_prompt == "f":
    valid = True
    if rigged_prompt == "r":
      settings["rigged"] = True
      settings["rigged_priority"] = []
    elif rigged_prompt == "f":
      settings["rigged"] = False
      
# Prompt user: Queen names
valid = False
while not valid:
  queen_prompt = input("Queen name:")
  if queen_prompt != "" and queen_prompt != " " and not queen_prompt in names:
    names.append(queen_prompt)
  elif queen_prompt == "":
    if len(names) < 6:
      print("Need at least 6 queens.")
    else:
      valid = True
      
# Prompt user: Season format
valid = False
while not valid:
  format_prompt = input("Season format? (r - regular/a - allstars):")
  if format_prompt == "r" or format_prompt == "a":
    valid = True
    if format_prompt == "r":
      settings["format"] = "Regular"
    elif format_prompt == "a":
      settings["format"] = "Allstars"
      
# Prompt user: Advanced rigged preferences
if settings["rigged"] == True:
  valid = False
  while not valid:
    rigged_prompt = input("(Rigged setting) Most likely to win? (Enter name):")
    if rigged_prompt in names:
      valid = True
      settings["rigged_priority"].append(rigged_prompt)

  valid = False
  while not valid:
    rigged_prompt = input("(Rigged setting) Least likely to win? (Enter name):")
    if rigged_prompt in names:
      if rigged_prompt == settings["rigged_priority"][0]:
        print("Most likely to win can't be least likely to win.")
      else:
        valid = True
        settings["rigged_priority"].append(rigged_prompt)

# Prompt user: Amount of finalists?
valid = False
while not valid:
  if settings["format"] == "Regular":
    finalist_prompt = input("Amount of finalists: (3-5)")
    if finalist_prompt.isdigit():
      finalist_prompt = int(finalist_prompt)
      if finalist_prompt > 2 and finalist_prompt < 6:
        valid = True
        settings["finalists"] = finalist_prompt
  elif settings["format"] == "Allstars":
    input("Amount of finalists is automatically set to 4 with allstars format.")
    settings["finalists"] = 4
    valid = True
     
# Track Record setup
for x in names:
  overall_scores[x] = 0
  track_record[x] = []

print()
      
# Print all the queen names
print('\n'.join(map(str, names)))

input()

# Normal episode cycle
while len(names) > settings["finalists"]:
  # Each queen is given a random score, indicating their placement in the episode
  scores = {}
  for x in names:
    scores[x] = random.randint(4, 18)
    track_record[x].append("SAFE")
    
  # Rigged properties
  if settings["rigged"] == True:
    most_likely = settings["rigged_priority"][0]
    least_likely = settings["rigged_priority"][1]
    
    if most_likely in names:
      scores[most_likely] = random.randint(7, 20)
    
    if least_likely in names:
      scores[least_likely] = random.randint(2, 16)
  
  for x, y in scores.items():
    overall_scores[x] += y
  
  # Sort the scores from best to worst so we can find the placements easily
  scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
  
  double_win = False

  if settings["format"] == "Regular":
    if random.randint(1, 5) == 1:
      top_two_profile_1 = scores[0][0]
      top_two_profile_2 = scores[1][0]
      print(top_two_profile_1+", "+top_two_profile_2+" condragulations, you are the top two of the week!")

      print("Nobody is going home tonight!")

      input()

      print("And now, the top two queens will lipsync for the win..")

      input()

      if random.randint(1, 2) == 1:
        track_record[top_two_profile_1][episode-1] = "WIN"
        track_record[top_two_profile_2][episode-1] = "TOP 2"
        print(top_two_profile_1+", you're a winner baby!")
      else:
        track_record[top_two_profile_2][episode-1] = "WIN"
        track_record[top_two_profile_1][episode-1] = "TOP 2"
        print(top_two_profile_2+", you're a winner baby!")
    else:
      # The winner is the first item, the one with the highest score, or the first two if it's a double win
      if random.randint(1, 4) == 1:
        double_win = True
        winner_profile_1 = scores[0][0]
        winner_profile_2 = scores[1][0]
        print(winner_profile_1+" and "+winner_profile_2+" both win the challenge!")
        track_record[winner_profile_1][episode-1] = "WIN"
        track_record[winner_profile_2][episode-1] = "WIN"
      else:
        winner_profile = scores[0][0]
        print(winner_profile+" wins the challenge!")
        track_record[winner_profile][episode-1] = "WIN"

      input()

      # Highs and lows are placements given to queens for extra critiques and placements on the track record
      if double_win == True:
        if len(names) > 4:
          high_profile = scores[2][0]
          print(high_profile+" receives positive feedback for the challenge.")
          track_record[high_profile][episode-1] = "HIGH"

          input()
        
        if len(names) > 5:
          high_profile = scores[3][0]
          print(high_profile+" receives positive feedback for the challenge.")
          track_record[high_profile][episode-1] = "HIGH"

          input()
        
        if len(names) > 6:
          low_profile = scores[len(scores)-3][0]
          print(low_profile+" receives negative feedback for the challenge.")
          track_record[low_profile][episode-1] = "LOW"
      else:
        if len(names) > 3:
          high_profile = scores[1][0]
          print(high_profile+" receives positive feedback for the challenge.")
          track_record[high_profile][episode-1] = "HIGH"

          input()
        
        if len(names) > 4:
          high_profile = scores[2][0]
          print(high_profile+" receives positive feedback for the challenge.")
          track_record[high_profile][episode-1] = "HIGH"

          input()
        
        if len(names) > 5:
          low_profile = scores[len(scores)-3][0]
          print(low_profile+" receives negative feedback for the challenge.")
          track_record[low_profile][episode-1] = "LOW"

          input()
    
      # The bottom twos are the last two items in the list.
      bottom_two_profile_1 = scores[len(scores)-1][0]
      print(bottom_two_profile_1+" is in the bottom for this challenge.")

      input()
      
      bottom_two_profile_2 = scores[len(scores)-2][0]
      print(bottom_two_profile_2+" is in the bottom for this challenge.")

      input()

      # Randomize and compare the scores, and eliminate the queen with the lowest score

      bottom_two_profile_1_score = overall_scores[bottom_two_profile_1] - random.randint(1, 6)
      bottom_two_profile_2_score = overall_scores[bottom_two_profile_2] - random.randint(1, 6)
      
      difference = 0

      if overall_scores[bottom_two_profile_1] > overall_scores[bottom_two_profile_2]:
        difference = overall_scores[bottom_two_profile_1] - overall_scores[bottom_two_profile_2]
      else:
        difference = overall_scores[bottom_two_profile_2] - overall_scores[bottom_two_profile_1]

      if difference < 5 and overall_scores[bottom_two_profile_1] > 50 and double_shantay == False:
          print(bottom_two_profile_1+", shantay you stay.")
          input()
          print(bottom_two_profile_2+", shantay you also stay!")
          double_shantay = True
      else:
        if bottom_two_profile_1_score > bottom_two_profile_2_score:
          print(bottom_two_profile_1+", shantay you stay.")
          input()
          print(bottom_two_profile_2+", sashay away.")
          track_record[bottom_two_profile_1][episode-1] = "BTM2"
          track_record[bottom_two_profile_2][episode-1] = "ELIM"
          names.remove(bottom_two_profile_2)
        else:
          print(bottom_two_profile_2+", shantay you stay.")
          input()
          print(bottom_two_profile_1+", sashay away.")
          track_record[bottom_two_profile_2][episode-1] = "BTM2"
          track_record[bottom_two_profile_1][episode-1] = "ELIM"
          names.remove(bottom_two_profile_1)
  elif settings["format"] == "Allstars":
    # The winner is the first item, the one with the highest score
    top_two_profile_1 = scores[0][0]
    top_two_profile_2 = scores[1][0]
    print("I've selected the best queens from this challenge!")
    input()
    print(top_two_profile_1+"..")
    input()
    print(top_two_profile_2+"..")
    input()
    print("Condragulations, you are the top two of the week!")

    input()

    # Highs and lows are placements given to queens for extra critiques and placements on the track record
    if len(names) > 5:
      high_profile = scores[2][0]
      print(high_profile+" receives positive feedback for the challenge.")
      track_record[high_profile][episode-1] = "HIGH"

      input()
    
    if len(names) > 6:
      high_profile = scores[3][0]
      print(high_profile+" receives positive feedback for the challenge.")
      track_record[high_profile][episode-1] = "HIGH"

      input()
    
    if len(names) > 7:
      low_profile = scores[len(scores)-3][0]
      print(low_profile+" receives negative feedback for the challenge.")
      track_record[low_profile][episode-1] = "LOW"

      input()

    # The bottom twos are the last two items in the list.
    bottom_two_profile_1 = scores[len(scores)-1][0]
    print(bottom_two_profile_1+" is in the bottom for this challenge.")

    input()
    
    bottom_two_profile_2 = scores[len(scores)-2][0]
    print(bottom_two_profile_2+" is in the bottom for this challenge.")

    input()

    print("Now.. "+top_two_profile_1+", "+top_two_profile_2+", the time has come.. for you to lipsync.. for your legacy!")
    input()
    print("Ladies, I've made my decision.")
    input()

    top_two_lipsync_winner_profile = ""

    if random.randint(1, 2) == 1:
      top_two_lipsync_winner_profile = top_two_profile_1
      track_record[top_two_profile_1][episode-1] = "WINNER"
      track_record[top_two_profile_2][episode-1] = "TOP 2"
    else:
      top_two_lipsync_winner_profile = top_two_profile_2
      track_record[top_two_profile_2][episode-1] = "WINNER"
      track_record[top_two_profile_1][episode-1] = "TOP 2"

    print(top_two_lipsync_winner_profile+", you're a winner baby!")

    input()

    print("Now, the time has come.. for a queen to get the chop. The queen "+top_two_lipsync_winner_profile+" has chosen to eliminate is..")

    input()

    eliminated_queen = ""

    if random.randint(1, 2) == 1:
      eliminated_queen = bottom_two_profile_1
      track_record[bottom_two_profile_2][episode-1] = "BTM2"
      track_record[bottom_two_profile_1][episode-1] = "ELIM"
      names.remove(bottom_two_profile_1)
    else:
      eliminated_queen = bottom_two_profile_2
      track_record[bottom_two_profile_1][episode-1] = "BTM2"
      track_record[bottom_two_profile_2][episode-1] = "ELIM"
      names.remove(bottom_two_profile_2)

    print(eliminated_queen+". I'm sorry my dear, but you must sashay away..")

  input()
    
  print('\n'.join(map(str, names)))

  input()

  episode += 1
  
# Final episode
final_lipsync_progressing_amount = random.randint(2, 3) if settings["finalists"] == 3 else 2
final_lipsync_progressors = []

for x in names:
    track_record[x].append("TBA")

print("Welcome to the finale! Our final " + inflect_engine.number_to_words(settings["finalists"]) + " will now perform their finale performances!")

input()

print("Let's take a look at out finalist's track records:")

for x in names:
  print(x.upper())
  queen_track = track_record[x]
  for y in queen_track:
    print(y)
  print("")

input()

print("And now, the audience members will vote for their favourite performance..")

audience_scores = {}
audience_total = 0

for x in names:
  queen_score = random.randint(20, 100)

  if settings["rigged"] == True:
    if x == most_likely:
      queen_score = random.randint(50, 100)
    elif x == least_likely:
      queen_score = random.randint(5, 45)

  audience_scores[x] = queen_score
  audience_total += queen_score

sorted_audience_scores = sorted(audience_scores.items(), key=lambda item: item[1], reverse=True)

[('a', 1), ('b', 5)]
for x in sorted_audience_scores:
  queen_name = x[0]
  queen_score = x[1]

  queen_percentage = round((queen_score / audience_total) * 100)
  audience_scores[queen_name] = queen_percentage

input()

if settings["finalists"] == final_lipsync_progressing_amount:
  print("Now, for the first time in Feature history, all our finalists are moving on to the final lipsync! That's right! All " + inflect_engine.number_to_words(final_lipsync_progressing_amount) + " queens will move on to the final lipsync.")
  final_lipsync_progressors = names.copy()
else:
  print("Now, this is where " + inflect_engine.number_to_words(settings["finalists"]) + " becomes " + inflect_engine.number_to_words(final_lipsync_progressing_amount) + "..")
  
  # The first queen moving to the final lipsync is whoever receives the most votes from the audience. The rest goes to the best in the final performance.
  sorted_overall_scores = sorted(overall_scores.items(), key=lambda item: item[1], reverse=True)
  index = random.randint(0, 1)
  first_progressor = sorted_overall_scores[index][0]
  final_lipsync_progressors.append(first_progressor)
  
  for x in sorted_audience_scores:
    # [("Aquatica", 30), ]
    if x[0] == first_progressor:
      del sorted_audience_scores[sorted_audience_scores.index(x)]

  for x in range(final_lipsync_progressing_amount-1):
    index = 0
    progressor = sorted_audience_scores[index][0]
    final_lipsync_progressors.append(progressor)
    del sorted_audience_scores[index]

  print("The queens moving on to the final lipsync are..")

  input()

  for x in final_lipsync_progressors:
    print(x+"!")
    input()

  eliminated_queens = []

  for x in names:
    if x not in final_lipsync_progressors:
      eliminated_queens.append(x)
      track_record[x][episode-1] = "ELIM"

  print("Which means, " + ", ".join(eliminated_queens) + ", I'm sorry, but I must ask you to sashay away.")

input()

print("And now, it's time for the final lipsync!")

input()

print("Ladies, I've made my decision..")

input()

print("The winner of Feature, is..")

input()

finalist_probabilities = {}

for x in final_lipsync_progressors:
  if settings["rigged"] == True:
    if x == most_likely:
      finalist_probabilities[x] = random.randint(35, 95)
    elif x == least_likely:
      finalist_probabilities[x] = random.randint(5, 20)
    else:
      finalist_probabilities[x] = random.randint(10, 55)
  else:
    finalist_probabilities[x] = random.randint(5, 95)

sorted_probabilities = sorted(finalist_probabilities.items(), key=lambda item: item[1], reverse=True)
season_winner = sorted_probabilities[0][0]

track_record[season_winner][episode-1] = "WINNER"

print(season_winner + "!")

if input() == "g":
  for x in final_lipsync_progressors:
    if x != season_winner:
      track_record[x][episode-1] = "RUNNER UP"

  file = open("feature.html", "w")

  color = '#{:06x}'.format(random.randint(0, 256**3))

  msg = f"""
  <html>
  <body style="background-color:{color};"><h1 style="color:white; font-family:verdana; text-align:center; font-size:200%">Feature's Drag Race</h1></body>
  """

  converted_track_record = track_record.items()

  for x in range(episode):
    actual_episode_number = x + 1

    msg += f"""
    <body style="background-color:{color};"><h1 style="color:white; font-family:verdana; text-align:center; font-size:160%">Episode {actual_episode_number}</h1></body>
    """

    placements = {}

    for y in converted_track_record:
      n = y[0] # The queen's name ('a')
      r = y[1] # The queen's track record (['WIN', 'SAFE', 'ELIM'])

      if len(r) >= actual_episode_number: # If the queen was in the episode we are creating..
        placements[n] = r[x]

    for z in placements:
      msg += f"""<body style="background-color:{color};"><h1 style="color:white; font-family:verdana; text-align:center; font-size:110%">{z}: {placements[z]}</h1></body>
      """

  file.write(msg)
  file.close()
  webbrowser.open_new_tab("feature.html")

