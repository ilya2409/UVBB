with open('hello.py') as f:
    print(sum(1 for _ in f))