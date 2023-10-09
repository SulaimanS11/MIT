def find_last(s, sub):
    sub2 = sub[::-1]
    carl = "".join(reversed(s))
    kachow = carl.find(sub2)
    print(sub, carl, kachow)
    if sub in s:
        return len(s)-kachow-len(sub)
    else:
        return None


s = "waka waka   ey eyyy"
print(find_last(s, sub="y"))
print(s[18])
