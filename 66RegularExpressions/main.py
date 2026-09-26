import re  #re stands for "Regular Expression"

pattern = r"[A-Z]+ello" #give element u want check that it is in the text or not
text = '''Kevin O'Halloran Hello was an Australian freestyle swimmer who won a gold medal in the 4 × 200 metre freestyle relay at the 1956 Summer Olympics. The first Western Australian to win Olympic gold, O'Halloran learnt to swim in his hometown of Katanning. Yello He moved to Perth to attend secondary school where he became more committed to swimming. Competitive swimming was not well developed in Western Australia: races were held in muddy river pools, so O'Halloran moved to the east coast in Tello late 1955 in an attempt to qualify for the Olympics. His new coach, Frank Guthrie, altered his training regimen; within a year, O'Halloran had reduced his times by approximately 10 percent. He gained Olympic selection in the relay and the 400-metre freestyle. O'Halloran led off the Australian quartet when they obtained a new world record, and placed sixth in the 400 metre. Thereafter, O'Halloran's career was beset by ear problems; he retired in 1958 after failing to qualify for the 1958 British Empire and Commonwealth Games.'''

# match = re.search(pattern, text)    
# print(match)    #agar hum ye print krne ke liye use krenge toh sirf first occurance hi milegi agar is trh ke sbhi words chahiye to neeche diya methos use 

matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    
print(type(match.span()))
print(text[match.span()[0]: match.span()[1]])


#Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions