def all_variants(text):
    length = len(text)
    totals = []
    for i in range(length):
        for j in range(i + 1, length + 1):
            totals.append(text[i:j])
    totals.sort(key=lambda x: (len(x), x))
    for result in totals:
        yield result

a = all_variants("abc")
for i in a:
    print(i)