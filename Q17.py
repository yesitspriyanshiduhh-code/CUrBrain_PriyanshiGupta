product_ids = [4, 2, 4, 3, 2, 4]

counts = {}

for product_id in product_ids:
    if product_id not in counts:
        counts[product_id] = 0
    counts[product_id] += 1

most_frequent = product_ids[0]

for product_id in counts:
    if counts[product_id] > counts[most_frequent]:
        most_frequent = product_id
    elif (counts[product_id] == counts[most_frequent]
          and product_id < most_frequent):
        most_frequent = product_id

print(most_frequent)