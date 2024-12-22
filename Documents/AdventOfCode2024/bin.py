from collections import deque, defaultdict


def generate(s, n):
    for i in range(n):
        s = (s ^ s << 6) & 0xffffff
        s = (s ^ s >> 5) & 0xffffff
        s = (s ^ s << 11) & 0xffffff
        yield s


def task1(cnt):
    print(sum(list(generate(s, 2000))[-1] for s in map(int, cnt.splitlines())))

s = 123
sums = defaultdict(int)
diffs = deque(maxlen=4)
prev = s % 10
seen = set()
for n in (n % 10 for n in generate(s, 2000)):
    print(n)
    diffs.append(n - prev)
    print(diffs)
    prev = n
    if len(diffs) == 4 and (t:=tuple(diffs)) not in seen:
        seen.add(t)
        sums[t] += n

print(max(sums.values()))