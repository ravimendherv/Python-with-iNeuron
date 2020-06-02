a=5
try:
    a=a/0
    print("Done")
except Exception as e:
    print(e," this is the run time error.")