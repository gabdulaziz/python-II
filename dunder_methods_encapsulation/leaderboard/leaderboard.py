class Leaderboard:
    def __init__(self):
        self.entries = []

    def add(self, name, score):
        self.entries.append({"name": name, "score": score})
        self.entries.sort(key=lambda e: e["score"], reverse=True)

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return len(self.entries)

    def __contains__(self, name):
        return any(e["name"] == name for e in self.entries)

    def __str__(self):
        if not self.entries:
            return "🏆 Leaderboard is empty"
        result = "🏆 Leaderboard:\n"
        for i, entry in enumerate(self.entries, 1):
            result += f" {i}. {entry['name']} — {entry['score']}\n"
        return result.strip()


lb = Leaderboard()
lb.add("Alice", 300)
lb.add("Bob", 500)
lb.add("Charlie", 150)

print(len(lb))
print(lb[0])
print(lb[1])
print("Alice" in lb)
print("Dave" in lb)
print(lb)