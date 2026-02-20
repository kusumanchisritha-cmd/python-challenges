raw = input("Enter song durations: ")
raw = raw.replace("[", "").replace("]", "")
parts = raw.replace(",", " ").split()

durations = list(map(int, parts))
for d in durations:
    if d<=0:
        print("Invalid duration")
        exit()
    elif any(durations.count(d) > 1 for d in durations):
        print("Category: Repetitive Playlist")
        print("Recommendation: Add variety")
        exit()
    else:
        total =sum(durations)
        songs=len(durations)
        if total<300:
            category="Too short Playlist"
            recommendation="Add more songs"
        elif total>3600:
            category="Too long  Playlist"
            recommendations="Reduce songs"
        elif any(durations.count(d) > 1 for d in durations):
            category="Repetitive Playlist"
            recommendations="Add variety"
        else:
            category="Balanced Playlist"
            recommendations="Good listening sessions"

print("Total Duration:",total)
print("Songs:",songs)
print("Category:",category)
print("Recommendations:",recommendations)