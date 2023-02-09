print("Hello motherfucker ")
score = 0 
tries = 0
add = 1
play = input("Do you want to play my game? :) \n")
def DRY(add):
    print("Correct answer")
    score += 1
    tries += 1
    print(score ,"/" ,tries)
def incorrect(tries):
    print("Incorrect answer")
    tries += 1
    print(score ,"/" ,tries)


if play.lower() != "yes":
    print("cagon")
    quit()
print("Okay lets play ")
RAM = input("what does RAM stands for? \n")
if RAM.lower() == "random access memory":
    DRY(add)
else:
    incorrect(tries)
Mundial = input("cuantos mudiales gano argentina? \n")
if Mundial.lower() == "2":
    DRY(add)
else:
    incorrect(tries)
mundi = input("En que continente queda Tanzania? \n")
if mundi.lower() == "africa":
    DRY(add)
else:
    incorrect(tries)
hierve = input("A cuantos grados hierve el agua? \n")
if hierve.lower() == "100":
   DRY
else:
    incorrect(tries)
canto = input("A que se dedicaba Fidel Nadal? \n")
if canto.lower() == "cantar" or "cantante" or "cantor" or "musico" or "a cantar":
    DRY(add)
else:
   incorrect(tries)
resp = score / tries
if resp == 1:
    print("Has ganado !!!")
else:
    print("Tus respuestas correctas fueron: ", score ,"/" ,tries)

