from collections import deque

records = int(input())
ready_students = deque()
successful = deque()

for _ in range(records):
    user_input = input().split(" ")
    if user_input[0] == "READY":
        ready_students.append(user_input[1])
    elif user_input[0] == "EXTRA":
        student = ready_students.pop()
        ready_students.appendleft(student)
    elif user_input[0] == "PASSED":
        student = ready_students.popleft()
        successful.append(student)
        
for student in range(len(successful)):
    print(successful.popleft())
