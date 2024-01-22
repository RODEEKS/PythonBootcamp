places_in_ooty=["manjoor","conoor","denalai","kariamalai","denadu"]
print(places_in_ooty) #["manjoor","conoor","denalai","kariamalai","denadu"]
print(places_in_ooty[2]) #denalai
print(places_in_ooty[-3]) #denadu

places_in_ooty[-1]="DENAD"
print(places_in_ooty) #["manjoor","conoor","denalai","kariamalai","DENAD"]

places_in_ooty.append("Manjithala")
print(places_in_ooty) #['manjoor', 'conoor', 'denalai', 'kariamalai', 'DENAD', 'Manjithala']

places_in_ooty.extend(["Roshan","Deekshiga","Rithika","Melita"])
print(places_in_ooty) #['manjoor', 'conoor', 'denalai', 'kariamalai', 'DENAD', 'Manjithala', 'Roshan', 'Deekshiga', 'Rithika', 'Melita']