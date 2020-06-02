main=[]
subject = ["Americans", "Indians"]
verb = ["Play", "watch"]
objects = ["Baseball","cricket"]

for i in subject:
    for j in verb:
        for k in objects:
            main.append(i+" "+j+" "+k)

for i in main:
    print(i)
