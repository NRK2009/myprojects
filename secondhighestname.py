if __name__ == '__main__':
    student = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name]=score
name = []
marks = list(student.values())
looper = set(marks)
for i in looper:
    if marks.count(i) > 1:
        for key, value in student.items():
            if value == i:
                name.append(key)
name.sort()

for i in name:
    print(i)