n, m = map(int, input().split())

def step(k):
    pos = [0]
    for _ in range(k):
        d, t = input().split()
        step = -1 if d == 'L' else 1
        for _ in range(int(t)):
            pos.append(pos[-1] + step)
    
    return pos



A_pos = step(n)
B_pos = step(m)

answer = -1

for i in range(1, min(len(A_pos), len(B_pos))):
    if A_pos[i] == B_pos[i]:
        answer = i
        break

print(answer)