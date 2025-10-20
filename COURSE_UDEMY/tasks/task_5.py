#  ===========підрахунок голосів===================
votes = ['так', 'ні', 'так', 'так', 'утримався', 'ні', 'так']
results = []

votes.sort()
current_type = votes[0]
count =0

for vote in votes:
    if vote == current_type:
        count += 1
    else:
        results.append((current_type, count))
        count = 1
        current_type = vote

else:
    results.append((current_type, count))
print(results)
