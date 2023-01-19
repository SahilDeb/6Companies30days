def invalidTransactions(transactions):
    r = dict()
    invalid = []

    for t in transactions:
        tokens = t.split(",")
        name = tokens[0]
        time = int(tokens[1])
        city = tokens[3]

        if time not in r:
            r[time] = {name: [city]}
        else:
            if name not in r[time]:
                r[time][name] = [city]
            else:
                r[time][name].append(city)

    for t in transactions:
        tokens = t.split(",")
        name = tokens[0]
        time = int(tokens[1])
        amount = int(tokens[2])
        city = tokens[3]

        if amount > 1000:
            invalid.append(t)
            continue

        # search if any time is in the range of curr time +- 60 mins
        for j in range(max(0, time - 60), time + 61):
            if j not in r:
                continue

            if name not in r[j]:
                continue

            # if for same name, there is more than 1 city or found city name != curr city name
            if len(r[j][name]) > 1 or r[j][name][0] != city:
                invalid.append(t)
                break
    return invalid


a1 = ["alice,20,800,mtv", "alice,50,100,beijing"]
# a2 = ["alice,20,800,mtv", "bob,50,1200,mtv"]
# a3 = ["alice,20,800,mtv", "alice,50,1200,mtv"]
print(invalidTransactions(a1))
