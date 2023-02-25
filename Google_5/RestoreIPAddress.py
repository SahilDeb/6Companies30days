def restoreIpAddresses(s: str):
    n = len(s)
    if n > 12:
        return []

    ipaddrs = set()
    for i in range(1, n-2):
        a = s[:i]
        if len(a) > 3:
            break
        for j in range(i+1, n-1):
            b = s[i: j]
            if len(b) > 3:
                break
            for k in range(j+1, n):
                c, d = s[j: k], s[k:]
                if len(c) > 3:
                    break

                if len(d) > 3:
                    continue

                combo = []
                for x in [a, b, c, d]:
                    if len(x) > 1 and x[0] == "0":
                        continue
                    if int(x) > 255:
                        continue
                    combo.append(x)

                if len(combo) != 4:
                    continue

                ipaddrs.add(".".join(combo))

    return list(ipaddrs)


s = "101023"
print(restoreIpAddresses(s))
