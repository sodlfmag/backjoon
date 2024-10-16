import sys
def get_grade(grade):
    match grade:
        case 'A+':
            return 4.5
        case 'A0':
            return 4.0
        case 'B+':
            return 3.5
        case 'B0':
            return 3.0
        case 'C+':
            return 2.5
        case 'C0':
            return 2.0
        case 'D+':
            return 1.5
        case 'D0':
            return 1.0
        case 'F':
            return 0

arr = list(sys.stdin.read().splitlines())
arr = [list(i.split())for i in arr]

total_credit = 0
total_grade = 0

for i in range(len(arr)):
    if(arr[i][2] == 'P'):
        continue

    credit = float(arr[i][1])
    grade = get_grade(arr[i][2])
    
    total_credit += credit
    total_grade += grade * credit

print(total_grade / total_credit)