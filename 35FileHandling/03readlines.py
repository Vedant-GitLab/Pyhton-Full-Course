f = open('35FileHandling/file.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    
    if not line:
        break
    m2 = line.split(",")[1]
    m1 = line.split(",")[0]
    m3 = line.split(",")[2]
    print(f"marks of student {i} in maths is : {m1}")
    print(f"marks of student {i} in english is : {m2}")
    print(f"marks of student {i} in physics is : {m3}")

    print(line)