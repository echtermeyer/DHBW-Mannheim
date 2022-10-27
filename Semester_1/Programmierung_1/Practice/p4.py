string = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,"

subset = string[:100]
s_delete = set(["d", "s"])

s = set(subset)

res = s - s_delete

print(s)
print(res)