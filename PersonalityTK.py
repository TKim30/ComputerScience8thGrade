import pyautogui as pg
import webbrowser as wb
import time as t
points = 0

pg.alert("This questionaire is case sensative. Example: If your favorite game is Fortnite, you must type into the box 'Fortnite' and not 'fortnite'.")
t.sleep(1)
show = pg.prompt("What is your favorite show? ")
if show == "The Office": 
    pg.alert("I love Dwight!")
    points += 7
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=a0CEqewunGA")
    t.sleep(5)
elif show == "Rick and Morty":
    pg.alert("It's so confusing, but funny!")
    points += 6
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=xWpmZz28ZOg")
    t.sleep(5)
elif show == "Riverdale":
    pg.alert("BASIC!")
    points += 5
elif show == "How I Met Your Mother":
    pg.alert("Watch the sequel I made on Youtube called 'How I met my cat!'")
    points += 4
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=J7vYllpgq_8")
    t.sleep(5)
elif show == "Friends":
    points += 3
    pg.alert ("You would be friends (did you see what I did there) with my sister.")
elif show == "The Fresh Prince of Bel Air":
    pg.alert("Now this is a story all about how my life got flipped turned upsidown and I'd like to take a minute just sit right there I'll tell to you how I became a Prince of a town called Bel Air. In West Phillidelphia born and raised on the playground is where I spent most of my days. Chillen out maxing relaxing and cooling shooting some bball outside of the school. Now a couple of guys who were up to no good started making trouble in my neighborhood. I got in one little fight and my mom got scared she said your moving in with your auntie and uncle in Bel Air.  I begged her please, Don't make me go away she packed my suitcase and sent me on my way. She gave me kiss and then she gave me ticket I put my walkman on I thought I might as well kick it! First class man this is nice sipping orange juice out of a champange glass is this how the people of Bel Air live like hmmm this might be alright. I whistled for a cab and when it came near its liscene plate said fresh and had a dice in the mirror. If anything I could say that this cab was rare but I forgot nah forget yo homes to Bel Air. I pulled up to a house about 7 or 8 and I yelled to the cabbie yo holmes smell ya later. Looked at my kingdom I was finally there to sit on my throne as the Fresh Prince of Bel Air ")
    points += 2
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=1nCqRmx3Dnw")
    t.sleep(5)
else:
    pg.alert("Your favorite show is " + str(show))
    points += 1

food = pg.prompt("What is your favorite food? ")
if food == "Pizza":
    points += 7
    pg.alert("Generic, but its still so good")
elif food == "Ice Cream":
    points += 6
    flavor = pg.prompt("What is your favorite flavor? ")
    if flavor == "Chocholate":
        pg.alert("My favorite!")
    elif flavor == "Vanilla":
        pg.alert("To plain for me!")
    elif flavor == "Mint Chip":
        pg.alert("Its OK, I guess...")
    elif flavor == "Cookies and Cream":
        pg.alert("So creamy and delicous!")
    elif flavor == "Strawberry":
        pg.alert("Only if it has actually chunks of strawberry in it!")
    elif flavor == "Rocky Road":
        pg.alert("Santos Car!")
        t.sleep(3)
        wb.open("https://www.youtube.com/watch?v=LDU_Txk06tM")  
        t.sleep(5)
    else:
        pg.alert("Your favorite ice cream flavor is " + flavor)
elif food == "General Tso's":
    pg.alert("So good!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=-47GhOl9hB0")
    points += 5
    t.sleep(5)
elif food == "Steak":
    points += 4
    pg.alert("NY Strip is obviously the best, right?")
elif food == "Pie":
    points += 3
    pg.alert("Apple and blueberry are my favorite.")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=VFQsDAADPLM")
    t.sleep(5)
elif food == "Pasta":
    points += 2
    pg.alert("Depeneds on the sauce!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=NHiqsrYkcuk")
    t.sleep(5)
else:
    pg.alert("Your favorite food is " + str(food))
    points += 1

videogame = pg.prompt("What is your favorite video game? ")
if videogame == "Fortnite":
    points += 7
    pg.alert("How many wins you Epic gamer!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=8pU7d_XzQa4")
    t.sleep(5)
elif videogame == "PUBG":
    points += 6
    pg.alert("... leave!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=y98De45A94Y")
    t.sleep(5)
elif videogame == "2K":
    points += 5
    pg.alert("Park is the  best!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=KMZ07OpmwTw")
    t.sleep(5)
elif videogame == "Batllefield":
    points += 4
    pg.alert("I'm so exceited for the new one!")
elif videogame == "Clash Royale":
    points +=3
    pg.alert("Nerf the Royale Giant!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=Hx3YftzJP3I")
    t.sleep(5)
elif videogame == "Call of Duty":
    points += 2
    pg.alert("The new one is aight!")
else:
    pg.alert("Your favorite videogame is " + str(videogame))
    points += 1

subject = pg.prompt("What is your favorite subject? ")
if subject == "Math":
    pg.alert("Me too!")
    points += 7
elif subject == "History":
    pg.alert("My second favorite!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=xzAOhyOtfqc")
    t.sleep(5)
    points += 6
elif subject == "Computer Science":
    pg.alert("Coding = cool!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=F9GujgK0y2M")
    points += 5
    t.sleep(5)
elif subject == "English":
    pg.alert("Essays stink!")
    points += 4
elif subject == "Science":
    pg.alert("I love doing experiments!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=u0ZP152mALk")
    points += 3
    t.sleep(5)
elif subject == "Language":
    pg.alert("I take Spanish!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=NZBdDkF_ZX8")
    points += 2
    t.sleep(5)
else:
    pg.alert("Your favorite subject is " + str(subject))
    points += 1

sport = pg.prompt("What is your favorite sport? ")
if sport == "Lacrosse":
    position = pg.prompt("Same! What position? ")
    if position == "Goalie":
        pg.alert("We have so much in common")
    else:
        pg.alert("Oh... Cool!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=o5hsPBsGD44")
    points += 7
    t.sleep(5)
elif sport == "Hockey":
    pg.alert("One of my favorites!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=xEbfwIWQCe0")
    points += 6
    t.sleep(5)
elif sport == "Field Hockey":
    pg.alert("Do you like Pumkin Spice Lattes too!")
    points += 5
elif sport == "Baseball":
    pg.alert("Even the grass gets bored!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=XUOmkQPa7kk")
    points += 4
    t.sleep(5)
elif sport == "Soccer":
    pg.alert("Is upstairs!")
    points += 3
elif sport == "Basketball":
    pg.alert("Lebron James!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=eh8WqbbvnqY")
    points += 2
    t.sleep(5)
else:
    pg.alert("Your favorite sport is " + str(sport))
    points += 1

movie = pg.prompt("What is your favorite movie? ")
if movie == "Star Wars":
    pg.alert("My favorite is Rogue One!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=PfYnvDL0Qcw")
    points += 8
    t.sleep(5)
elif movie == "Deadpool":
    pg.alert("I have never seen it, but it seems sick!")
    points += 7
elif movie == "Talededga Knights":
    pg.alert("'Ima come at you like a spider monkey Chip'!")
    points += 6
elif movie == "Paul Blart Mall Cop":
    pg.alert("It has to be two, It really made me feel like I was hit by that milk truck too.")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=Bv0A2iINenA")
    points += 5
    t.sleep(5)
elif movie == "Iron Man":
    pg.alert("All money no powers.")
    points += 4
elif movie == "Mighty Ducks":
    pg.alert("'Ducks fly together!'")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=Bv0A2iINenA")
    points += 3
    t.sleep(5)
elif movie == "Finding Nemo":
    pg.alert("Iconic!")
    t.sleep(3)
    wb.open("https://www.youtube.com/watch?v=K7bNhYr3ves")
    points += 2
    t.sleep(5)
else:
    pg.alert("Your favorite movie is " + str(movie))
    points += 1

pg.alert("Your score was " + str(points))
